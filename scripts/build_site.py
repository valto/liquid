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


def render_body(page):
    text = source(page['source']).read_text()
    if page.get('mode') == 'transcript':
        pages = text.split('\f')
        return ''.join(f'<section class="transcript"><h2>Original PDF page {i}</h2><pre>{html.escape(p)}</pre></section>' for i, p in enumerate(pages, 1) if p.strip())
    text = re.sub(r'\A# [^\n]+\n', '', text)
    text = text.replace('@@BASE@@', SITE['base_path']).replace(SITE['url'], SITE['base_path'])
    if '<script' in text.lower() or '<iframe' in text.lower():
        raise ValueError('Executable markup is not publication content')
    return markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc'])


def cards(items, label):
    return '<div class="cards">' + ''.join(f'<a class="card" href="{href(p["path"])}"><span class="kicker">{label}</span><h3>{html.escape(p["title"])}</h3><p>{html.escape(p["description"])}</p><span class="card-arrow" aria-hidden="true">↗</span></a>' for p in items) + '</div>'


def document(page, body):
    title = page['title'] + ' | Liquid Software'
    data = {'@context': 'https://schema.org', '@type': 'TechArticle' if page['kind'] in ['concept', 'paper', 'draft'] else 'WebPage', 'headline': page['title'], 'description': page['description'], 'url': url(page['path']), 'inLanguage': 'en', 'dateModified': page['modified'], 'creator': {'@type': 'Person', 'name': SITE['author']}, 'version': page['version'], 'creativeWorkStatus': page['status']}
    if page.get('publication_date'):
        data['datePublished'] = page['publication_date']
    content_license = page.get('content_license', SITE.get('content_license'))
    if content_license:
        data['license'] = content_license
    metadata = html.escape(page['description'], quote=True)
    nav = ''.join(f'<a href="{href(path)}"'+(' aria-current="page"' if page['path'] == path else '')+f'>{name}</a>' for name, path in [('Concepts','concepts/'),('Architecture','architecture/'),('Whitepapers','whitepapers/'),('Principles','principles/'),('Glossary','glossary/'),('Research','research/'),('About','about/')])
    downloads = ''
    if page.get('pdf'):
        downloads = f'<a class="button" href="{href(page["pdf"])}">Download PDF</a>'
    downloads += f'<a class="text-link" href="{href(page["markdown"])}">Read source text ↗</a>'
    attribution = html.escape(page.get('attribution', 'Conceptual source: Valto Loikkanen · AI-assisted synthesis and research'))
    if page['kind'] == 'draft':
        attribution += ' · Research draft; not independently peer reviewed'
    if page['path'] == '':
        heading = '<div class="hero"><p class="kicker">INFORMATION · INTELLIGENCE · HUMAN SOVEREIGNTY</p><h1>Liquid<br><span>Software</span></h1><p class="hero-subtitle">Beyond the Constraints of Software</p><p class="hero-thesis">Intelligence is the default capability.<br>Software is an optimization.</p><div class="hero-actions"><a class="button" href="'+href('whitepapers/00-beyond-the-constraints-of-software/')+'">Read the umbrella paper</a><a class="text-link" href="'+href('concepts/')+'">Explore the concepts ↗</a></div></div>'
    else:
        heading = f'<header class="article-header"><p class="kicker">{html.escape(page["status"].replace("-", " "))} · VERSION {html.escape(page["version"])}</p><h1>{html.escape(page["title"])}</h1><p class="dek">{metadata}</p><p class="byline">{attribution}</p><div class="hero-actions">{downloads}</div></header>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{metadata}"><link rel="canonical" href="{url(page['path'])}"><link rel="alternate" type="text/markdown" href="{href(page['markdown'])}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{metadata}"><meta property="og:type" content="article"><meta property="og:url" content="{url(page['path'])}"><meta property="og:image" content="{url('assets/og.png')}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{url('assets/og.png')}"><link rel="stylesheet" href="{href('assets/style.css')}"><script type="application/ld+json">{json.dumps(data,ensure_ascii=False).replace('</','<\\/')}</script></head><body><a class="skip" href="#main">Skip to content</a><div class="topbar"><a class="brand" href="{href('')}"><span class="brand-mark" aria-hidden="true">L</span>Liquid Software</a><nav aria-label="Primary">{nav}</nav></div><main id="main" class="shell">{heading}<article class="prose">{body}</article></main><footer class="shell"><div><strong>Liquid Software</strong><p>Information provides continuity.<br>Human decisions define the boundaries.</p></div><div><a href="{href('about/')}">Attribution & citation</a><a href="{href('concepts.json')}">Concept registry</a><a href="{href('llms.txt')}">Machine reading guide</a><a href="{SITE['repository']}">GitHub source</a><p>© 2026 Valto Loikkanen · {html.escape(SITE['status'].replace('-',' '))}</p></div></footer></body></html>'''


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
        file = page['path'] + 'index.html' if page['path'].endswith('/') or not page['path'] else page['path']
        output[file] = document(page, body).encode()
        text = source(page['source']).read_text().replace('@@BASE@@', SITE['base_path'])
        output[page['markdown']] = text.encode()
        full_text.append(f"# {page['title']}\nURL: {url(page['path'])}\nStatus: {page['status']}\nConceptual source: {SITE['author']}\n\n{text}")
    for item in CONFIG['files']:
        data = source(item['source']).read_bytes()
        if item.get('sha256') and hashlib.sha256(data).hexdigest() != item['sha256']:
            raise ValueError('Versioned asset changed: ' + item['source'])
        if item['destination'] in output:
            raise ValueError('Duplicate generated path')
        output[item['destination']] = data
    concepts = [{k:v for k,v in p.items() if k not in ['source','markdown','collection']} | {'url':url(p['path']),'conceptual_source':SITE['author']} for p in PAGES if p['kind'] == 'concept']
    output['concepts.json'] = (json.dumps({'schema_version':'1.0','concepts':concepts},indent=2,ensure_ascii=False)+'\n').encode()
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
