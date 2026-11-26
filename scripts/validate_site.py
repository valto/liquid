#!/usr/bin/env python3
"""Check publication paths, metadata, immutable assets and the public selection."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT/'docs'
CONFIG = json.loads((ROOT/'site/pages.json').read_text())
SITE = CONFIG['site']


class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.links=[];self.meta={};self.canonical=[];self.h1=0;self.ld=[];self.in_ld=False;self.parts=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='meta':self.meta[a.get('name') or a.get('property')]=a.get('content')
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
        if tag in ['a','img','link']:
            target=a.get('src') or a.get('href')
            if target:self.links.append(target)
        if tag=='script':
            if a.get('type')!='application/ld+json':raise ValueError('Unexpected executable script')
            self.in_ld=True;self.parts=[]
    def handle_endtag(self,tag):
        if tag=='script' and self.in_ld:self.in_ld=False;self.ld.append(json.loads(''.join(self.parts)))
    def handle_data(self,data):
        if self.in_ld:self.parts.append(data)


def target(page_path,link):
    p=urlsplit(link)
    if p.scheme in ['mailto','data']:return None
    if p.scheme and (p.netloc!='valto.github.io' or not p.path.startswith(SITE['base_path'])):return None
    if p.path.startswith('/'):
        if not p.path.startswith(SITE['base_path']):raise ValueError('Project path escaped: '+link)
        path=DOCS/unquote(p.path.removeprefix(SITE['base_path']))
    else:path=page_path.parent/unquote(p.path)
    if not p.path:path=page_path
    if path.is_dir():path=path/'index.html'
    if not path.resolve().is_relative_to(DOCS.resolve()):raise ValueError('Link escaped public directory')
    return path,p.fragment


def main():
    errors=[];parsed={}
    for page in CONFIG['pages']:
        file=page['path']+'index.html' if page['path'].endswith('/') or not page['path'] else page['path']
        path=DOCS/file
        p=Page();p.feed(path.read_text());parsed[path.resolve()]=p
        if p.h1!=1:errors.append(file+': requires exactly one H1')
        if len(p.ids)!=len(set(p.ids)):errors.append(file+': duplicate fragment IDs')
        if p.canonical!=[SITE['url']+page['path']]:errors.append(file+': canonical mismatch')
        if p.meta.get('description')!=page['description']:errors.append(file+': description mismatch')
        for key in ['og:title','og:description','og:url','og:image','twitter:card']:
            if not p.meta.get(key):errors.append(file+': missing '+key)
        if len(p.ld)!=1:errors.append(file+': structured metadata missing')
        elif p.ld[0].get('datePublished')!=page.get('publication_date'):errors.append(file+': inferred publication date')
        if any(data.get('license')!=SITE.get('content_license') for data in p.ld):errors.append(file+': license metadata mismatch')
    for path,p in parsed.items():
        for link in p.links:
            try:resolved=target(path,link)
            except ValueError as e:errors.append(str(e));continue
            if resolved:
                dest,fragment=resolved
                if not dest.is_file():errors.append(str(path.relative_to(DOCS))+': broken '+link)
                elif fragment and dest.suffix=='.html' and fragment not in parsed.get(dest.resolve(),Page()).ids:errors.append('Missing fragment '+link)
    manifest=json.loads((DOCS/'build-manifest.json').read_text())
    actual={str(p.relative_to(DOCS)) for p in DOCS.rglob('*') if p.is_file()}
    if actual!=set(manifest)|{'build-manifest.json'}:errors.append('Public file set differs from build manifest')
    for path,digest in manifest.items():
        if hashlib.sha256((DOCS/path).read_bytes()).hexdigest()!=digest:errors.append('Asset hash differs: '+path)
    forbidden=['full-discussion-thread','conversation.json','github-implementation-plan','source-captures','browser.html','owner-clarifications']
    for name in actual:
        if any(x in name for x in forbidden):errors.append('Private/reference-only input included: '+name)
    for p in DOCS.rglob('*'):
        if p.is_symlink():errors.append('Symlink in deployment: '+str(p))
        if p.suffix in ['.html','.md','.json','.txt','.xml','.css'] and p.is_file():
            text=p.read_text()
            if re.search(r'/(?:home|Users)/[^/\s]+|/Volumes/[^/\s]+|BEGIN (?:RSA|OPENSSH) PRIVATE KEY',text):errors.append('Internal path or credential material: '+str(p.relative_to(DOCS)))
    for item in CONFIG['files']:
        if item.get('sha256') and hashlib.sha256((DOCS/item['destination']).read_bytes()).hexdigest()!=item['sha256']:errors.append('Published version changed: '+item['destination'])
    concepts=json.loads((DOCS/'concepts.json').read_text())['concepts'];ids={c['id'] for c in concepts}
    if len(ids)!=len(concepts):errors.append('Duplicate concept IDs')
    for c in concepts:
        if set(c.get('related_concepts',[]))-ids:errors.append('Unknown concept relationship')
    if errors:
        print('\n'.join(errors),file=sys.stderr);return 1
    print(f'Validated {len(parsed)} pages, {len(actual)} public files, {len(concepts)} concepts and immutable PDF hashes.')
    return 0


if __name__=='__main__':raise SystemExit(main())
