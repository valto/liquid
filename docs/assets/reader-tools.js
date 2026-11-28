/* Optional copy and print controls; reading and downloads work without JavaScript. */
'use strict';

const copyButton = document.querySelector('[data-copy-prompt]');
if (copyButton) {
  const prompt = document.querySelector('#agent-prompt');
  const status = document.querySelector('#copy-status');
  copyButton.hidden = false;
  copyButton.addEventListener('click', async () => {
    copyButton.disabled = true;
    try {
      await navigator.clipboard.writeText(prompt.value);
      status.textContent = 'Prompt copied. Add your situation and question in your agent conversation.';
    } catch {
      prompt.closest('details').open = true;
      prompt.focus();
      prompt.select();
      status.textContent = 'Automatic copying is unavailable. The prompt is selected; copy it yourself or download the plain text.';
    } finally {
      copyButton.disabled = false;
    }
  });
}

document.querySelectorAll('[data-print-guide]').forEach(button => {
  button.hidden = false;
  button.addEventListener('click', () => window.print());
});
