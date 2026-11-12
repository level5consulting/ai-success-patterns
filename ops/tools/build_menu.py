#!/usr/bin/env python3
"""Rebuild the left menu on every page from the home page's PATTERNS list.
Usage: python3 ops/tools/build_menu.py [site_root]   (default: current directory)
Run it after publishing a pattern. Only patterns in PATTERNS (published) appear.
Names only, never numbers; Start here keeps its order with no step numbers (Greg, Nov 10).
The "agent" group shows as "Runs on its own" (plain language, accepted Nov 10). Safe to run twice."""
import json, os, re, subprocess, sys

root = sys.argv[1] if len(sys.argv) > 1 else '.'
home = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
js = re.search(r'const PATTERNS = (\[[\s\S]*?\n\]);', home).group(1)
P = json.loads(subprocess.run(['node', '-e', 'console.log(JSON.stringify(eval(require("fs").readFileSync(0,"utf8"))))'],
                              input=js, capture_output=True, text=True, check=True).stdout)
GROUPS = [('conv', 'In the chat'), ('agent', 'Runs on its own'), ('acc', 'Accuracy'), ('gov', 'Governance')]

def key(name):
    return re.sub(r'^(the|a|an)\s+', '', name.lower())

start = [(h, n.replace(' with an LLM Interview', '')) for h, n in
         re.findall(r'<a class="step" href="(patterns/[^"]+)">.*?<h3>([^<]+)</h3>', home, flags=re.S)]
if len(start) != 5:
    sys.exit('Start here: expected 5 steps, found %d' % len(start))

def menu(path):
    rel = os.path.relpath(path, root)
    up = '../' * rel.count(os.sep)
    here = rel.replace(os.sep, '/')
    is_home = here == 'index.html'
    old = open(path, encoding='utf-8').read()
    talk = re.search(r'<a class="talk"[^>]*>.*?</a>', old, flags=re.S).group(0)
    cur = ' aria-current=page'
    # which type is open
    open_cat = next((p['cat'] for p in P if p['page'] == here), None)
    if open_cat is None and here.startswith('patterns/'):
        m = re.search(r'<span class="tag tag-(conv|agent|acc|gov)">', old)
        open_cat = m.group(1) if m else None
    all_attr = ' data-cat="all"' if is_home else ''
    count = len(P)
    out = ['  <div class="navs">']
    out.append(f'    <nav aria-label="Main"><a href="{up}index.html#patterns"{all_attr}>All patterns <small>{count}</small></a></nav>')
    out.append('    <h4>Start here</h4>')
    links = ''.join(f'<a href="{up}{h}"{cur if h == here else ""}>{n}</a>' for h, n in start)
    out.append(f'    <nav aria-label="Start here" class="startnav">{links}</nav>')
    out.append('    <h4>Patterns by type</h4>')
    for cat, label in GROUPS:
        items = sorted([p for p in P if p['cat'] == cat], key=lambda p: key(p['name']))
        links = ''.join(f'<a href="{up}{p["page"]}"{cur if p["page"] == here else ""}>{p["name"]}</a>' for p in items)
        op = ' open' if cat == open_cat else ''
        out.append(f'    <details class="pgroup"{op}><summary>{label} <small>{len(items)}</small></summary><nav aria-label="{label} patterns">{links}</nav></details>')
    out.append('    <h4>More</h4>')
    more = [('In review', 'index.html#in-review'), ('Coming soon', 'index.html#backlog'), ('About', 'index.html#about'),
            ('Sessions', 'sessions/index.html'), ('Services', 'services/index.html')]
    links = ''.join(f'<a href="{up}{h}"{cur if h == here else ""}>{t}</a>' for t, h in more)
    out.append(f'    <nav aria-label="More">{links}</nav>')
    out.append(f'    {talk}')
    out.append('  </div>\n</aside>')
    return old, '\n'.join(out)

n = 0
for d, _, fs in os.walk(root):
    if any(x in d for x in ('/.git', '/mockups', '/ops')):
        continue
    for f in fs:
        if not f.endswith('.html'):
            continue
        p = os.path.join(d, f)
        s = open(p, encoding='utf-8').read()
        if '<aside class="rail">' not in s:
            continue
        old, new = menu(p)
        s2, c = re.subn(r'  <div class="navs">.*?</div>\n</aside>', lambda m: new, old, count=1, flags=re.S)
        if c != 1:
            sys.exit('No menu block in ' + p)
        if s2 != old:
            open(p, 'w', encoding='utf-8').write(s2)
        n += 1
print(f'{n} pages, {len(P)} patterns')
