import re, html, json, sys
md = open('patterns/29-give-the-meeting-a-facilitator.md').read()
E = lambda t: html.escape(t, quote=False)
def inline(t):
    t = E(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t
def section(name):
    m = re.search(r'^## ' + re.escape(name) + r'\n(.*?)(?=^## |\n---\n)', md, re.S | re.M)
    return m.group(1).strip()
def blocks(b, ind='      '):
    out=[]; lines=b.split('\n'); i=0
    while i<len(lines):
        l=lines[i]
        if not l.strip(): i+=1; continue
        if l.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip('|').split('|')]); i+=1
            h=rows[0]; body=[r for r in rows[1:] if not set(''.join(r))<=set('-: ')]
            t=f'{ind}<div style="overflow-x:auto"><table class="sort-table"><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in h)+'</tr></thead><tbody>'
            t+=''.join('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>' for r in body)+'</tbody></table></div>'
            out.append(t); continue
        if l.startswith('### '):
            out.append(f'{ind}<h3>{inline(l[4:])}</h3>'); i+=1; continue
        if re.match(r'\d+\. ',l):
            items=[]
            while i<len(lines) and re.match(r'\d+\. ',lines[i]):
                items.append(re.sub(r'^\d+\. ','',lines[i])); i+=1
            out.append(f'{ind}<ol class="tight-list">'+''.join(f'<li>{inline(x)}</li>' for x in items)+'</ol>'); continue
        if l.startswith('- '):
            items=[]
            while i<len(lines) and (lines[i].startswith('- ') or lines[i].startswith('  - ')):
                if lines[i].startswith('- '): items.append([lines[i][2:],[]])
                else: items[-1][1].append(lines[i][4:])
                i+=1
            li=''.join(f'<li>{inline(a)}'+(('<ul class="tight-list">'+''.join(f'<li>{inline(x)}</li>' for x in sub)+'</ul>') if sub else '')+'</li>' for a,sub in items)
            out.append(f'{ind}<ul class="tight-list">{li}</ul>'); continue
        para=[]
        while i<len(lines) and lines[i].strip() and not re.match(r'(- |\||### |\d+\. )',lines[i]):
            para.append(lines[i]); i+=1
        out.append(f'{ind}<p>{inline(" ".join(para))}</p>')
    return '\n'.join(out)
chk = '<svg class="check" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5"/><path d="M5 8.5l2 2 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def titled(name):
    b=section(name); m=re.match(r'\*\*(.+?)\*\*\n',b); return m.group(1), b[m.end():].strip()
pt,pb=titled('Problem'); vt,vb=titled('Value'); st,sb=titled('Solution')
cb=section('When to use it'); nb=section('Notes')
vals=[l[2:] for l in vb.split('\n') if l.startswith('- ')]
vhtml='\n'.join(f'        <div class="value-item">\n          {chk}\n          <span>{inline(v)}</span>\n        </div>' for v in vals)
intro,_,rest=sb.partition('**Step 1')
rest='**Step 1'+rest
rest,_,after=rest.partition('\n### ')
after=('### '+after) if after else ''
steps=re.findall(r'\*\*Step (\d): (.+?)\*\* (.+?)(?=\n\n\*\*Step|\Z)', rest, re.S)
shtml='\n'.join(f'''        <div class="sequence-step">
          <span class="step-num">Step {n}</span>
          <div class="step-body">
            <div class="step-title">{inline(t)}</div>
            <div class="step-desc">
{blocks(d.strip(),'              ')}
            </div>
          </div>
        </div>''' for n,t,d in steps)
lead=re.search(r'\*\*Lead \(draft\):\*\* (.+)', md).group(1)
prompt=re.search(r'```\n(.*?)\n```', md, re.S).group(1)
strip=re.search(r'## Use this pattern\n\*(.+?)\*\n', md).group(1)
body=f'''  <article class="pattern-body">
    <section class="section">
      <p class="section-label">Problem</p>
      <h2>{inline(pt)}</h2>
{blocks(pb)}
    </section>
    <section class="section">
      <p class="section-label">Value</p>
      <h2>{inline(vt)}</h2>
      <div class="value-box">
{vhtml}
      </div>
    </section>
    <section class="section">
      <p class="section-label">When to use it</p>
{blocks(cb)}
    </section>
    <section class="section">
      <p class="section-label">Solution</p>
      <h2>{inline(st)}</h2>
{blocks(intro.strip())}
      <div class="sequence-steps">
{shtml}
      </div>
{blocks(after)}
    </section>
    <section class="section">
      <p class="section-label">Notes</p>
      <h2>Note taking is not enough</h2>
{blocks(nb)}
    </section>
  </article>
'''
cfg=dict(title="Give the Meeting a Facilitator",cat="Governance",catcls="gov",level="Practice",num="29")
s=open('patterns/28-the-expertise-bridge.html').read()
s=re.sub(r'<title>.*?</title>', f"<title>{E(cfg['title'])}</title>", s, count=1)
s=re.sub(r'<span class="tag tag-(conv|agent|acc|gov)">[^<]*</span>', f"<span class=\"tag tag-{cfg['catcls']}\">{cfg['cat']}</span>", s, count=1)
bars={'Practice':'<i class="on"></i><i class="on"></i><i class=""></i>'}[cfg['level']]
s=re.sub(r'<span class="level-chip">.*?</span>(Foundation|Practice|Leadership)</span>', f'<span class="level-chip"><span class="level-bars" aria-hidden="true">{bars}</span>{cfg["level"]}</span>', s, count=1)
assert 'tag tag-draft' in s
s=re.sub(r'<h1 class="pattern-title">.*?</h1>', f'<h1 class="pattern-title">{E(cfg["title"])}</h1>', s, count=1)
s=re.sub(r'<p class="pattern-lead">.*?</p>', lambda m:'<p class="pattern-lead">'+inline(lead)+'</p>', s, count=1, flags=re.S)
s=re.sub(r'  <article class="pattern-body">.*?  </article>\n', lambda m: body, s, count=1, flags=re.S)
s=re.sub(r'(<h2>Use this pattern</h2>\s*<p>).*?(</p>)', lambda m: m.group(1)+E(strip).replace("'", '&#39;')+m.group(2), s, count=1, flags=re.S)
s=re.sub(r'<span class="pm-title" id="pm-title">.*?</span>', f'<span class="pm-title" id="pm-title">{E(cfg["title"])}</span>', s, count=1)
s=re.sub(r'(<pre id="pm-skill-text">).*?(</pre>)', lambda m: m.group(1)+E(prompt)+m.group(2), s, count=1, flags=re.S)
rel=[("02-onboard-dont-program.html","Onboard, Don't Program","How you build the facilitator"),("25-the-chat-is-not-your-memory.html","The Chat Is Not Your Memory","The record the agenda comes from"),("26-judge-the-outcome-not-the-craft.html","Judge the Outcome, Not the Craft","A person checks the decisions")]
relh='\n'.join(f'''      <a href="{h}" class="related-card">
        <span class="related-title">{E(t)}</span>
        <span class="related-rel">{E(r)}</span>
      </a>''' for h,t,r in rel)
s=re.sub(r'<div class="related-grid">.*?</div>\n  </aside>', lambda m:'<div class="related-grid">\n'+relh+'\n    </div>\n  </aside>', s, count=1, flags=re.S)
# breadcrumb title
s=s.replace('The Expertise Bridge', cfg['title'])
# category current in breadcrumb
s=s.replace('<a href="../index.html#patterns" aria-current=page>Accuracy</a>','<a href="../index.html#patterns" aria-current=page>Governance</a>')
if '.sort-table' not in s:
    s=s.replace('/* Use-this-pattern strip + modal */','''.sort-table{width:100%;border-collapse:collapse;margin:4px 0 14px;font-size:0.86rem;}
.sort-table th{text-align:left;font-family:var(--font-mono);font-size:0.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--fg-sub);border-bottom:1px solid var(--rule);padding:6px 8px;}
.sort-table td{border-bottom:1px solid var(--rule);padding:8px;vertical-align:top;color:var(--fg-mid);}
@media(max-width:600px){.sort-table{font-size:0.8rem;}.sort-table td,.sort-table th{padding:6px 4px;}}
/* Use-this-pattern strip + modal */''',1)
open('patterns/29-give-the-meeting-a-facilitator.html','w').write(s)
print(len(steps),'steps',len(vals),'values', 'leftover Bridge:', s.count('Expertise Bridge'), 'emdash', s.count('—'))
