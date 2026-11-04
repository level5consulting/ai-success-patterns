import re, html, json, sys
cfg = json.load(open(sys.argv[1]))
md = open(cfg['md']).read()
E = lambda t: html.escape(t, quote=False)
def inline(t):
    t = E(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
    return t
def sec(name):
    m = re.search(r'^## ' + name + r'[^\n]*\n\*\*(.+?)\*\*\n\n(.*?)(?=\n## |\n---)', md, re.S | re.M)
    return m.group(1), m.group(2).strip()
def paras(b):
    out = []
    for p in b.split('\n\n'):
        lines = p.split('\n')
        if all(l.startswith('- ') for l in lines):
            out.append('      <ul>' + ''.join(f'<li>{inline(l[2:])}</li>' for l in lines) + '</ul>')
        else:
            out.append(f'      <p>{inline(p)}</p>')
    return '\n'.join(out)
chk = '<svg class="check" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5"/><path d="M5 8.5l2 2 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
pt, pb = sec('Problem'); vt, vb = sec('Value'); ct, cb = sec('Context'); st, sb = sec('Solution')
vals = [l[2:] for l in vb.split('\n') if l.startswith('- ')]
vhtml = '\n'.join(f'        <div class="value-item">\n          {chk}\n          <span>{inline(v)}</span>\n        </div>' for v in vals)
intro, _, rest = sb.partition('**Step 1')
rest = '**Step 1' + rest
steps = re.findall(r'\*\*Step (\d): (.+?)\*\* (.+?)(?=\n\n\*\*Step|\Z)', rest, re.S)
def stepdesc2(d):
    out = []
    for p in d.strip().split('\n\n'):
        lines = p.split('\n')
        head = [l for l in lines if not l.startswith('- ')]
        items = [l[2:] for l in lines if l.startswith('- ')]
        if head: out.append(inline(' '.join(head)))
        if items: out.append('<ul class="tight-list">' + ''.join(f'<li>{inline(i)}</li>' for i in items) + '</ul>')
    return '<br><br>'.join(out).replace('<br><br><ul', '<ul')
shtml = '\n'.join(f'''        <div class="sequence-step">
          <span class="step-num">Step {n}</span>
          <div class="step-body">
            <div class="step-title">{inline(t)}</div>
            <div class="step-desc">{stepdesc2(d)}</div>
          </div>
        </div>''' for n, t, d in steps)
introhtml = paras(intro.strip()) if intro.strip() else ''
lead = re.search(r'\*\*Lead \(draft\):\*\* (.+)', md).group(1)
prompt = re.search(r'```\n(.*?)\n```', md, re.S).group(1)
body = f'''  <article class="pattern-body">
    <section class="section">
      <p class="section-label">Problem</p>
      <h2>{inline(pt)}</h2>
{paras(pb)}
    </section>
    <section class="section">
      <p class="section-label">Value</p>
      <h2>{inline(vt)}</h2>
      <div class="value-box">
{vhtml}
      </div>
    </section>
    <section class="section">
      <p class="section-label">Context</p>
      <h2>When this pattern applies</h2>
{paras(cb)}
    </section>
    <section class="section">
      <p class="section-label">Solution</p>
      <h2>{inline(st)}</h2>
{introhtml}
      <div class="sequence-steps">
{shtml}
      </div>
    </section>
    <section class="section">
      <p class="section-label">Notes</p>
      <h2>{E(cfg['notes_h2'])}</h2>
{cfg['notes_html']}
    </section>
{cfg.get('extra_html','')}  </article>
'''
s = open(cfg['template']).read()
s = re.sub(r'<title>.*?</title>', f"<title>{E(cfg['title'])}</title>", s, count=1)
s = re.sub(r'<span>Pattern \d+</span>', f"<span>Pattern {cfg['num']}</span>", s, count=1)
s = re.sub(r'<span class="pattern-num">PATTERN \d+</span>', f"<span class=\"pattern-num\">PATTERN {cfg['num']}</span>", s, count=1)
s = re.sub(r'<span class="tag tag-(conv|agent|acc|gov)">[^<]*</span>', f"<span class=\"tag tag-{cfg['catcls']}\">{cfg['cat']}</span>", s, count=1)
bars = {'Foundation': '<i class="on"></i><i class=""></i><i class=""></i>', 'Practice': '<i class="on"></i><i class="on"></i><i class=""></i>', 'Leadership': '<i class="on"></i><i class="on"></i><i class="on"></i>'}[cfg['level']]
s = re.sub(r'<span class="level-chip">.*?</span>(Foundation|Practice|Leadership)</span>', f'<span class="level-chip"><span class="level-bars" aria-hidden="true">{bars}</span>{cfg["level"]}</span>', s, count=1)
if 'tag tag-draft' not in s:
    s = s.replace(f"<span class=\"tag tag-{cfg['catcls']}\">{cfg['cat']}</span>", f"<span class=\"tag tag-{cfg['catcls']}\">{cfg['cat']}</span>\n      <span class=\"tag tag-draft\">In Review</span>", 1)
s = re.sub(r'<h1 class="pattern-title">.*?</h1>', f'<h1 class="pattern-title">{E(cfg["title"])}</h1>', s, count=1)
s = re.sub(r'<p class="pattern-lead">.*?</p>', lambda m: '<p class="pattern-lead">' + inline(lead) + '</p>', s, count=1, flags=re.S)
s = re.sub(r'  <figure class="graphic-zone[^"]*".*?</figure>', '''  <figure class="graphic-zone" aria-label="Pattern illustration placeholder">
    <svg class="graphic-icon" viewBox="0 0 48 48" fill="none" aria-hidden="true">
      <circle cx="24" cy="24" r="8" stroke="currentColor" stroke-width="2"/>
      <path d="M4 24h8M36 24h8M24 4v8M24 36v8" stroke="currentColor" stroke-width="2" stroke-dasharray="2 3" stroke-linecap="round"/>
    </svg>
    <span class="graphic-label">Illustration</span>
    <span class="graphic-caption">Visual coming.</span>
  </figure>''', s, count=1, flags=re.S)
s = re.sub(r'  <article class="pattern-body">.*?  </article>\n', lambda m: body, s, count=1, flags=re.S)
s = re.sub(r'(<h2>Use this pattern</h2>\s*<p>).*?(</p>)', lambda m: m.group(1) + E(cfg['strip']).replace("'", '&#39;') + m.group(2), s, count=1, flags=re.S)
s = re.sub(r'<span class="pm-title" id="pm-title">.*?</span>', f'<span class="pm-title" id="pm-title">Pattern {cfg["num"]} - {E(cfg["title"])}</span>', s, count=1)
s = re.sub(r'(<pre id="pm-skill-text">).*?(</pre>)', lambda m: m.group(1) + E(prompt) + m.group(2), s, count=1, flags=re.S)
rel = '\n'.join(f'''      <a href="{h}" class="related-card">
        <span class="related-num">PATTERN {n}</span>
        <span class="related-title">{E(t)}</span>
        <span class="related-rel">{E(r)}</span>
      </a>''' for h, n, t, r in cfg['related'])
s = re.sub(r'<div class="related-grid">.*?</div>\n  </aside>', lambda m: '<div class="related-grid">\n' + rel + '\n    </div>\n  </aside>', s, count=1, flags=re.S)
s = re.sub(r'aria-current=page', '', s)
s = s.replace(f'<a href="../index.html#patterns">{cfg["cat"]}</a>', f'<a href="../index.html#patterns" aria-current=page>{cfg["cat"]}</a>', 1)
if cfg.get('names_only', True):  # Names, not numbers (Greg, November 3, 2026): no pattern numbers visible to readers
    s = re.sub(r'\s*<span class="pattern-num">PATTERN \d+</span>', '', s, count=1)
    s = re.sub(r'(<span class="sep">›</span>\s*<span>)Pattern \d+(</span>)', lambda m: m.group(1) + E(cfg['title']) + m.group(2), s, count=1)
    s = re.sub(r'\s*<span class="related-num">PATTERN \d+</span>', '', s)
    s = re.sub(r'(<span class="pm-title" id="pm-title">)Pattern \d+ - ', r'\1', s, count=1)
open(cfg['out'], 'w').write(s)
print('built', cfg['out'], len(steps), 'steps', len(vals), 'values')
