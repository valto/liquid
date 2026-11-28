#!/usr/bin/env node
/* Exercise visitor reading, handoff, fallback and print behavior in a real browser. */
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const config = JSON.parse(await fs.readFile(path.join(root, 'site/pages.json'), 'utf8'));
const readers = config.pages.filter(p => p.kind === 'reader');
const output = process.env.LIQUID_READER_CHECK_DIR || await fs.mkdtemp(path.join(os.tmpdir(), 'liquid-readers-'));
await fs.mkdir(output, { recursive: true });
const runtime = process.env.PLAYWRIGHT_CORE_PATH ? pathToFileURL(process.env.PLAYWRIGHT_CORE_PATH).href : 'playwright-core';
const { chromium } = await import(runtime);
const port = Number(process.env.LIQUID_PREVIEW_PORT || 18795);
const origin = `http://127.0.0.1:${port}`;
const base = origin + config.site.base_path;
const printOnly = process.argv.includes('--print-only');
const report = { mode: printOnly ? 'print-only' : 'complete', checkedAt: new Date().toISOString(), pages: [], prompts: [], fallback: [], print: [], downloads: [] };
let browser;
const server = spawn(process.env.PYTHON || 'python3', ['scripts/serve_preview.py', '--port', String(port)], { cwd: root, stdio: ['ignore', 'pipe', 'pipe'] });
try {
  await new Promise((resolve, reject) => {
    let stderr = '';
    const timeout = setTimeout(() => reject(new Error('Preview server did not start')), 10000);
    server.stderr.on('data', data => { stderr += data; });
    server.once('error', error => { clearTimeout(timeout); reject(error); });
    server.once('exit', code => { clearTimeout(timeout); reject(new Error(`Preview exited (${code}): ${stderr}`)); });
    server.stdout.on('data', data => {
      if (data.toString().includes('Preview:')) { clearTimeout(timeout); resolve(); }
    });
  });
  browser = await chromium.launch({ executablePath: process.env.CHROME_PATH || '/usr/bin/google-chrome', args: ['--no-sandbox'] });
  const context = await browser.newContext({ permissions: ['clipboard-read', 'clipboard-write'] });
  const page = await context.newPage();
  const pageErrors = [];
  page.on('pageerror', error => pageErrors.push(error.message));

  if (!printOnly) {
    for (const width of [1440, 390]) {
      await page.setViewportSize({ width, height: 900 });
      for (const item of config.pages) {
        const response = await page.goto(base + item.path, { waitUntil: 'networkidle' });
        assert.equal(response.status(), 200, item.path);
        assert.equal(await page.locator('h1').count(), 1);
        const layout = await page.evaluate(() => ({ viewport: document.documentElement.clientWidth, content: document.documentElement.scrollWidth }));
        assert.ok(layout.content <= layout.viewport + 1, `${item.path}: horizontal overflow at ${width}`);
        report.pages.push({ path: item.path, width });
        if (['', 'start/', 'agents/', 'readers/business-leaders/'].includes(item.path)) {
          await page.screenshot({ path: path.join(output, `${item.path.replaceAll('/', '-') || 'home'}${width}.png`), fullPage: true });
        }
      }
    }
    assert.deepEqual(pageErrors, []);

    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto(base);
    assert.equal(await page.locator('.card[href*="/readers/"]').count(), readers.length);
    await page.getByRole('link', { name: 'Start with your perspective', exact: true }).click();
    assert.equal(page.url(), base + 'start/');
    await page.locator('.card[href$="/readers/business-leaders/"]').click();
    assert.equal(page.url(), base + 'readers/business-leaders/');
    await page.getByRole('link', { name: 'Give this to your agent', exact: true }).first().click();
    assert.equal(new URL(page.url()).hash, '#agent-context');

    for (const item of [...readers, { path: 'agents/', reader: { slug: 'general' } }]) {
      await page.goto(base + item.path);
      const selected = readers.find(r => r.reader.slug === item.reader.slug);
      const expected = await fs.readFile(path.join(root, 'docs', selected.path, 'agent-prompt.txt'), 'utf8');
      assert.equal(await page.locator('#agent-prompt').inputValue(), expected);
      assert.ok(expected.includes(config.site.url + selected.path));
      assert.ok(expected.includes('My situation: [add your context]'));
      await page.getByRole('button', { name: 'Copy prompt', exact: true }).focus();
      await page.keyboard.press('Enter');
      await page.waitForFunction(() => document.querySelector('#copy-status').textContent.startsWith('Prompt copied.'));
      assert.equal(await page.evaluate(() => navigator.clipboard.readText()), expected);
      report.prompts.push({ path: item.path, selected: selected.reader.slug, keyboardCopy: true });

      const pending = page.waitForEvent('download');
      await page.getByRole('link', { name: 'Download plain text', exact: true }).click();
      const download = await pending;
      assert.equal(await fs.readFile(await download.path(), 'utf8'), expected);
      report.downloads.push({ path: item.path, exact: true });
      await page.evaluate(() => { window.__printCalls = 0; window.print = () => window.__printCalls++; });
      await page.locator('[data-print-guide]').click();
      assert.equal(await page.evaluate(() => window.__printCalls), 1);
    }

    for (const mode of ['denied', 'unavailable']) {
      const fallback = await browser.newContext();
      await fallback.addInitScript(mode => {
        Object.defineProperty(navigator, 'clipboard', { configurable: true, value: mode === 'denied' ? { writeText: async () => { throw new DOMException('Denied', 'NotAllowedError'); } } : undefined });
      }, mode);
      const p = await fallback.newPage();
      await p.goto(base + 'readers/business-leaders/');
      await p.getByRole('button', { name: 'Copy prompt', exact: true }).click();
      await p.waitForFunction(() => document.querySelector('#copy-status').textContent.startsWith('Automatic copying is unavailable.'));
      const selection = await p.locator('#agent-prompt').evaluate(el => ({ start: el.selectionStart, end: el.selectionEnd, length: el.value.length, focused: document.activeElement === el, open: el.closest('details').open }));
      assert.deepEqual(selection, { start: 0, end: selection.length, length: selection.length, focused: true, open: true });
      assert.equal(await p.getByRole('button', { name: 'Copy prompt', exact: true }).isEnabled(), true);
      report.fallback.push({ mode, selectedFullPrompt: true });
      await fallback.close();
    }

    const noScript = await browser.newContext({ javaScriptEnabled: false });
    const plain = await noScript.newPage();
    for (const route of ['agents/', 'readers/data-knowledge/']) {
      await plain.goto(base + route);
      assert.equal(await plain.locator('[data-copy-prompt]').isVisible(), false);
      await plain.getByText('Read the full prompt', { exact: true }).click();
      assert.equal(await plain.locator('#agent-prompt').isVisible(), true);
      assert.ok((await plain.locator('#agent-prompt').inputValue()).includes(config.site.url));
      assert.equal(await plain.getByRole('link', { name: 'Download plain text', exact: true }).isVisible(), true);
    }
    report.noJavaScript = { reading: true, manualPrompt: true, downloads: true };
    await noScript.close();

  }

  await page.emulateMedia({ media: 'print' });
  for (const item of [{ path: '', reader: null }, ...readers, { path: 'agents/', reader: null }]) {
    await page.goto(base + item.path);
    assert.equal(await page.locator('.topbar').isVisible(), false);
    if (item.reader) assert.equal(await page.locator('.agent-panel').isVisible(), false);
    if (item.path === 'agents/') {
      assert.equal(await page.locator('.print-prompt').isVisible(), true);
      assert.equal(await page.locator('.print-prompt').innerText(), await page.locator('#agent-prompt').inputValue());
    }
    const file = (item.path.replaceAll('/', '-') || 'home') + 'print.pdf';
    await page.pdf({ path: path.join(output, file), format: 'A4', printBackground: true, preferCSSPageSize: true });
    report.print.push({ path: item.path, file });
  }
  const index = await context.request.get(base + 'readers.json');
  const readerIndex = await index.json();
  assert.equal(readerIndex.readers.length, readers.length);
  for (const item of readerIndex.readers) {
    assert.ok(item.prompt_url.startsWith(config.site.url));
    assert.ok(item.reading.every(r => r.url.startsWith(config.site.url)));
  }
  assert.deepEqual(pageErrors, []);
  report.result = 'passed';
  await fs.writeFile(path.join(output, 'browser-check.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(`Passed (${report.mode}) ${report.pages.length} desktop/mobile page loads, ${report.prompts.length} keyboard copies and downloads, ${report.fallback.length} fallback modes, JavaScript-disabled checks: ${Boolean(report.noJavaScript)}, ${report.print.length} print outputs. Evidence: ${output}`);
} finally {
  if (browser) await browser.close();
  if (server.exitCode === null) {
    server.kill('SIGTERM');
    await new Promise(resolve => server.once('exit', resolve));
  }
}
