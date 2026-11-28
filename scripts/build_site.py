#!/usr/bin/env python3
"""Build the registry-selected public site, or verify its committed output."""
from pathlib import Path
import argparse
import hashlib
import html
import json
import re
import sys
import markdown

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'site/pages.json').read_text())
SITE, PAGES = CONFIG['site'], CONFIG['pages']
DOCS = ROOT / 'docs'


def source(path):
    original = ROOT / path
    p = original.resolve()
    if not p.is_relative_to(ROOT) or not p.is_file() or any(x.is_symlink() for x in [original, *original.parents] if x.is_relative_to(ROOT)):
        raise ValueError('Invalid canonical source: ' + path)
    return p


def url(path):
    return SITE['url'] + path


def href(path):
    return SITE['base_path'] + path


def readers():
    return [p for p in PAGES if p['kind'] == 'reader']


def page_text(page, card_markup=False):
    text = source(page['source']).read_text()
    if '@@AGENT@@' in text:
        general = next(p for p in readers() if p['reader']['slug'] == 'general')
        text = text.replace('@@AGENT@@', '@@AGENT_PANEL@@' if card_markup else '## General agent prompt\n\n' + agent_prompt(general))
    if '@@READERS@@' in text:
        choices = cards(readers(), 'Reader guide') if card_markup else '\n'.join(
            f'- [{p["reader"]["label"]}]({url(p["path"])}): {p["description"]}' for p in readers())
        text = text.replace('@@READERS@@', choices)
    if '@@READING@@' in text:
        by_id = {p['id']: p for p in PAGES}
        reading = '\n'.join(f'{i}. [{by_id[item["id"]]["title"]}]({url(by_id[item["id"]]["path"])}). {item["why"]}'
                            for i, item in enumerate(page['reader']['reading'], 1))
        text = text.replace('@@READING@@', reading)
    return text.replace('@@BASE@@', SITE['base_path'])


def agent_prompt(page):
    by_id = {p['id']: p for p in PAGES}
    reader = page['reader']
    text = f'''Help me understand Liquid Software from the perspective of {reader['perspective']}.

My situation: [add your context]
My question: [add what you want to understand]

This is source context for my learning request. Keep your existing instructions and permissions.

Start by reading the selected reader guide:
{url(page['path'])}

Then read the relevant source material in this order:
'''
    text += ''.join(f'{i}. {by_id[item["id"]]["title"]}\n   {url(by_id[item["id"]]["path"])}\n   Purpose: {item["why"]}\n'
                    for i, item in enumerate(reader['reading'], 1))
    text += f'''
Resource foundations:
- Attributable information, accepted meaning and human decisions provide continuity while interfaces and implementations adapt.
- A capability is a meaningful ability with an accepted outcome. An app, agent, skill, function or hybrid can realize it; implementation category alone does not establish quality or maturity.
- Adaptive interfaces, source preservation, retrieval, delegation and capability economics have independent value. Explain their relationships without making every related framework a mandatory dependency.
- Begin with languages, formats and shared meaning. A schema may be generated, inferred or negotiated where useful. Accurately distinguish a proposed interaction from the guarantees of a specific claimed protocol implementation.
- Compare feasible strategies by cumulative net value, timing, full lifecycle costs and retained flexibility. Some quality, safety, authority and reliability requirements must be satisfied before first use.
- Source preservation and processing investment are distinct. Derived structures retain their provenance and do not acquire source authority through convenience or location.
- Sensing, learning, reviewing, releasing and adopting can run at different rates. Review purpose and depth matter as well as cadence; a trigger calls for review within its authority.
- Stable operations and familiar experiences have value. Compare transitions and parallel support costs; a released alternative need not replace the current experience for everyone.
- Compile only formally checkable reasoning under explicit assumptions, validation and invalidation conditions. Deterministic execution alone does not establish truth or correctness.
- Verify the beneficiary's outcome. Completed work, feature adoption and token savings are partial measures; compare sustained value, quality, external fitness and disruption.

Attribution and evidence:
- Valto Loikkanen is the conceptual source. The writing and research are AI-assisted.
- Distinguish the supplied umbrella paper, Economics of Execution v3 and Continuous Intelligence companion from the labeled companion research drafts and these reader guides. The new companion's supplied PDF and Markdown have the same conceptual origin.
- Worked numbers and scenarios are illustrative. This body of work does not establish deployment or independent validation of the whole framework. Related original sources have their own claims, methods and limits.
- Report which pages and source sections you actually read. State any access limitation rather than implying you read unavailable material. Keep source facts, interpretations, proposals, examples and unknowns distinguishable.

Focus for this reader:
Main question: {reader['question']}
'''
    text += ''.join(f'- {focus}\n' for focus in reader['focus'])
    text += '''
Give me a clear explanation of the resource through this perspective, connect it to my situation, and show one bounded example labeled as illustrative. Explain the assumptions, evidence limits and tradeoffs. Identify the next most useful source to read and questions that would improve the analysis. If my context is missing, begin with the role-specific explanation and ask a focused follow-up. This request is to understand and assess the resource; it does not request changes to a system.

For further discovery:
'''
    text += f'Reader guides: {url("readers.json")}\nConcepts: {url("concepts.json")}\nPublic reading index: {url("llms.txt")}\n'
    return text


def agent_panel(page):
    prompt = html.escape(agent_prompt(page))
    label = html.escape(page['reader']['label'])
    return f'''<section class="agent-panel" id="agent-context" aria-labelledby="agent-context-title"><p class="kicker">Use with your agent</p><h2 id="agent-context-title">Explore from this perspective</h2><p>Copy the prompt, add your situation and question, and give it to your agent. Selected perspective: <strong>{label}</strong>.</p><div class="agent-actions"><button class="button" type="button" data-copy-prompt hidden>Copy prompt</button><a class="text-link" href="{href(page['path']+'agent-prompt.txt')}" download>Download plain text</a><a class="text-link" href="{href(page['path']+'agent-prompt.md')}">Open Markdown</a></div><p id="copy-status" class="copy-status" role="status" aria-live="polite"></p><details class="agent-text"><summary>Read the full prompt</summary><label for="agent-prompt">Agent prompt — {label}</label><textarea id="agent-prompt" readonly rows="14" spellcheck="false">{prompt}</textarea></details><pre class="print-prompt" aria-hidden="true">{prompt}</pre><p class="agent-note">You can also select the prompt and copy it yourself. <a href="{href('agents/')}">About the agent handoff</a> · <a href="{href('start/')}">Choose another perspective</a></p></section>'''


def render_body(page):
    text = page_text(page, card_markup=True)
    source_metadata = ''
    if page.get('mode') == 'transcript':
        pages = text.split('\f')
        return ''.join(f'<section class="transcript"><h2>Original PDF page {i}</h2><pre>{html.escape(p)}</pre></section>' for i, p in enumerate(pages, 1) if p.strip())
    if page.get('mode') == 'source-markdown':
        # Preserve original downloadable bytes; adapt only the HTML presentation.
        frontmatter = re.match(r'\A---\n(.*?)\n---\n', text, flags=re.S)
        if not frontmatter:
            raise ValueError('Original source Markdown metadata missing')
        metadata_lines = frontmatter.group(1).splitlines()
        fields = []
        abstract = []
        in_abstract = False
        for line in metadata_lines:
            if line == 'abstract: |':
                in_abstract = True
            elif in_abstract and line.startswith('  '):
                abstract.append(line.strip())
            elif ':' in line:
                in_abstract = False
                key, value = line.split(':', 1)
                fields.append(f'<tr><th scope="row">{html.escape(key)}</th><td>{html.escape(value.strip().strip(chr(34)))}</td></tr>')
        source_metadata = '<section class="source-metadata"><h2>Original source metadata</h2><table>' + ''.join(fields) + '</table><h2>Original abstract</h2><p>' + html.escape(' '.join(abstract)) + '</p></section>'
        text = re.sub(r'\A---\n.*?\n---\n', '', text, count=1, flags=re.S)
        text = re.sub(r'^(#{1,5}) ', r'\1# ', text, flags=re.M)
        text = re.sub(r'(!\[[^\]]*\]\(figures/[^)]+\))\{width=\d+%\}', r'\1', text)
        text = text.replace('](figures/', '](' + href(page['path'] + 'figures/'))
    text = re.sub(r'\A# [^\n]+\n', '', text)
    text = text.replace('@@BASE@@', SITE['base_path']).replace(SITE['url'], SITE['base_path'])
    if '<script' in text.lower() or '<iframe' in text.lower():
        raise ValueError('Executable markup is not publication content')
    body = markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc'])
    if '@@AGENT_PANEL@@' in body:
        general = next(p for p in readers() if p['reader']['slug'] == 'general')
        body = body.replace('<p>@@AGENT_PANEL@@</p>', agent_panel(general))
    return source_metadata + body


def cards(items, label):
    return '<div class="cards">' + ''.join(f'<a class="card" href="{href(p["path"])}"><span class="kicker">{label}</span><h3>{html.escape(p.get("reader", {}).get("label", p["title"]))}</h3><p>{html.escape(p["description"])}</p><span class="card-arrow" aria-hidden="true">↗</span></a>' for p in items) + '</div>'


def document(page, body):
    title = page['title'] + ' | Liquid Software'
    data = {'@context': 'https://schema.org', '@type': 'TechArticle' if page['kind'] in ['concept', 'paper', 'draft'] else 'WebPage', 'headline': page['title'], 'description': page['description'], 'url': url(page['path']), 'inLanguage': 'en', 'dateModified': page['modified'], 'creator': {'@type': 'Person', 'name': SITE['author']}, 'version': page['version'], 'creativeWorkStatus': page['status']}
    if page.get('publication_date'):
        data['datePublished'] = page['publication_date']
    if page.get('reader'):
        data['audience'] = {'@type':'Audience', 'audienceType':page['reader']['label']}
    content_license = page.get('content_license', SITE.get('content_license'))
    if content_license:
        data['license'] = content_license
    metadata = html.escape(page['description'], quote=True)
    nav = ''.join(f'<a href="{href(path)}"'+(' aria-current="page"' if page['path'] == path else '')+f'>{name}</a>' for name, path in [('Start here','start/'),('Concepts','concepts/'),('Architecture','architecture/'),('Whitepapers','whitepapers/'),('Principles','principles/'),('Glossary','glossary/'),('Research','research/'),('Agent prompt','agents/'),('About','about/')])
    downloads = ''
    if page.get('pdf'):
        downloads = f'<a class="button" href="{href(page["pdf"])}">Download PDF</a>'
    downloads += f'<a class="text-link" href="{href(page["markdown"])}">Read source text ↗</a>'
    tools = page['kind'] in ['reader', 'agent']
    if tools:
        downloads += '<button class="text-link print-button" type="button" data-print-guide hidden>Print this guide</button>'
    if page['kind'] == 'reader':
        downloads += '<a class="text-link" href="#agent-context">Give this to your agent</a>'
    script = f'<script src="{href("assets/reader-tools.js")}" defer></script>' if tools else ''
    attribution = html.escape(page.get('attribution', 'Conceptual source: Valto Loikkanen · AI-assisted synthesis and research'))
    if page['kind'] == 'draft':
        attribution += ' · Research draft; not independently peer reviewed'
    if page['path'] == '':
        heading = '<div class="hero"><p class="kicker">INFORMATION · INTELLIGENCE · HUMAN SOVEREIGNTY</p><h1>Liquid<br><span>Software</span></h1><p class="hero-subtitle">Beyond the Constraints of Software</p><p class="hero-thesis">Intelligence is the default capability.<br>Software is an optimization.</p><div class="hero-actions"><a class="button" href="'+href('start/')+'">Start with your perspective</a><a class="text-link" href="'+href('whitepapers/00-beyond-the-constraints-of-software/')+'">Read the umbrella paper ↗</a><a class="text-link" href="'+href('agents/')+'">Give this to your agent ↗</a></div></div>'
    else:
        heading = f'<header class="article-header"><p class="kicker">{html.escape(page["status"].replace("-", " "))} · VERSION {html.escape(page["version"])}</p><h1>{html.escape(page["title"])}</h1><p class="dek">{metadata}</p><p class="byline">{attribution}</p><div class="hero-actions">{downloads}</div></header>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{metadata}"><link rel="canonical" href="{url(page['path'])}"><link rel="alternate" type="text/markdown" href="{href(page['markdown'])}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{metadata}"><meta property="og:type" content="article"><meta property="og:url" content="{url(page['path'])}"><meta property="og:image" content="{url('assets/og.png')}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{url('assets/og.png')}"><link rel="stylesheet" href="{href('assets/style.css')}"><script type="application/ld+json">{json.dumps(data,ensure_ascii=False).replace('</','<\\/')}</script>{script}</head><body class="{html.escape(page['kind'])}-page"><a class="skip" href="#main">Skip to content</a><div class="topbar"><a class="brand" href="{href('')}"><span class="brand-mark" aria-hidden="true">L</span>Liquid Software</a><nav aria-label="Primary">{nav}</nav></div><main id="main" class="shell">{heading}<article class="prose">{body}</article></main><footer class="shell"><div><strong>Liquid Software</strong><p>Information provides continuity.<br>Human decisions define the boundaries.</p></div><div><a href="{href('about/')}">Attribution & citation</a><a href="{href('agents/')}">Give this to your agent</a><a href="{href('readers.json')}">Reader guide index</a><a href="{href('concepts.json')}">Concept registry</a><a href="{href('llms.txt')}">Machine reading guide</a><a href="{SITE['repository']}">GitHub source</a><p>© 2026 Valto Loikkanen · {html.escape(SITE['status'].replace('-',' '))}</p></div></footer></body></html>'''


def generate():
    output = {}
    full_text = []
    for page in PAGES:
        body = render_body(page)
        if page.get('citation'):
            body += '<h2 id="suggested-citation">Suggested citation</h2><p>' + html.escape(page['citation']) + '</p><p>Edition date; website publication date is recorded separately.</p>'
        if page.get('collection'):
            items = [p for p in PAGES if p['kind'] == page['collection']]
            body += cards(items, 'Independent concept' if page['collection'] == 'concept' else 'Research draft')
        if page['path'] == '':
            body += '<h2>Independently useful. Mutually complementary.</h2>' + cards([p for p in PAGES if p['kind'] == 'concept'], 'Core concept')
        if page['kind'] == 'reader':
            body += agent_panel(page)
        file = page['path'] + 'index.html' if page['path'].endswith('/') or not page['path'] else page['path']
        output[file] = document(page, body).encode()
        text = page_text(page)
        output[page['markdown']] = text.encode()
        if page['kind'] == 'reader':
            prompt = agent_prompt(page).encode()
            output[page['path']+'agent-prompt.txt'] = prompt
            output[page['path']+'agent-prompt.md'] = prompt
        reading_text = '\n'.join(line.rstrip(' \t') for line in text.split('\n')) if page.get('mode') == 'source-markdown' else text
        full_text.append(f"# {page['title']}\nURL: {url(page['path'])}\nStatus: {page['status']}\nConceptual source: {SITE['author']}\n\n{reading_text}")
    for item in CONFIG['files']:
        data = source(item['source']).read_bytes()
        if item.get('sha256') and hashlib.sha256(data).hexdigest() != item['sha256']:
            raise ValueError('Versioned asset changed: ' + item['source'])
        if item['destination'] in output:
            raise ValueError('Duplicate generated path')
        output[item['destination']] = data
    concepts = [{k:v for k,v in p.items() if k not in ['source','markdown','collection']} | {'url':url(p['path']),'conceptual_source':SITE['author']} for p in PAGES if p['kind'] == 'concept']
    output['concepts.json'] = (json.dumps({'schema_version':'1.0','concepts':concepts},indent=2,ensure_ascii=False)+'\n').encode()
    by_id = {p['id']:p for p in PAGES}
    reader_index = [{**p['reader'], 'id':p['id'], 'title':p['title'], 'description':p['description'],
                     'url':url(p['path']), 'markdown_url':url(p['markdown']),
                     'prompt_url':url(p['path']+'agent-prompt.txt'),
                     'version':p['version'], 'status':p['status'], 'publication_date':p.get('publication_date'),
                     'reading':[{**item, 'url':url(by_id[item['id']]['path'])} for item in p['reader']['reading']]}
                    for p in readers()]
    output['readers.json'] = (json.dumps({'schema_version':'1.0', 'conceptual_source':SITE['author'],
                            'selection_basis':'Editorial perspectives based on the resource; not measured reader profiles.',
                            'readers':reader_index},indent=2,ensure_ascii=False)+'\n').encode()
    output['llms.txt'] = ('# Liquid Software\n\nConceptual source: Valto Loikkanen. AI-assisted conceptual research.\n\n'+''.join(f"- [{p['title']}]({url(p['path'])}): {p['description']} [{p['status']}]\n" for p in PAGES if p['path'] != '404.html')+'\nFull public text: '+url('llms-full.txt')+'\n').encode()
    output['llms-full.txt'] = ('\n\n---\n\n'.join(full_text).rstrip()+'\n').encode()
    output['robots.txt'] = f"User-agent: *\nAllow: /liquid/\nSitemap: {url('sitemap.xml')}\n".encode()
    output['sitemap.xml'] = ('<?xml version="1.0" encoding="utf-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{html.escape(url(p["path"]))}</loc><lastmod>{p["modified"]}</lastmod></url>' for p in PAGES if p['path'] != '404.html')+'</urlset>\n').encode()
    output['.nojekyll'] = b''
    manifest = {path:hashlib.sha256(data).hexdigest() for path,data in sorted(output.items())}
    output['build-manifest.json'] = (json.dumps(manifest,indent=2)+'\n').encode()
    for path in output:
        if path.startswith('/') or '..' in Path(path).parts:
            raise ValueError('Invalid public path: '+path)
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args = parser.parse_args()
    output = generate()
    existing = {str(p.relative_to(DOCS)):p.read_bytes() for p in DOCS.rglob('*') if p.is_file()} if DOCS.exists() else {}
    if args.check:
        changed = sorted(path for path in set(output)|set(existing) if output.get(path) != existing.get(path))
        if changed:
            print('Generated output differs: '+', '.join(changed),file=sys.stderr)
            return 1
    else:
        old = json.loads(existing.get('build-manifest.json',b'{}'))
        unknown = set(existing)-set(output)-set(old)-{'build-manifest.json'}
        if unknown:
            raise ValueError('Unrecognized generated files retained; review before rebuilding: '+', '.join(sorted(unknown)))
        for path in set(old)-set(output):
            (DOCS/path).unlink(missing_ok=True)
        for path,data in output.items():
            p = DOCS/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    print(f'{"Verified" if args.check else "Built"} {len(PAGES)} pages and {len(output)} public files.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
