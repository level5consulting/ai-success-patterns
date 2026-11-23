#!/usr/bin/env python3
"""Weekly Morning Review record (The Chat Is Not Your Memory).

Reads the form's `reviews` documents (JSON files saved with ArtifactData list/out_dir)
and writes one Markdown file per week (Sunday to Saturday, named by that week's Monday):
  - full copy  -> <full_dir>/week-of-YYYY-MM-DD.md   (private: the Claude project doc morning-review/)
  - public copy -> <public_dir>/week-of-YYYY-MM-DD.md (records/morning-review/ on ops; private items left out)

Usage: python3 form_record.py <reviews_json_dir> <full_dir> <public_dir> [YYYY-MM-DD ...]
With dates, only the weeks containing those dates are written; without, every week.
"""
import json, glob, os, re, sys, datetime as dt

PRIVATE_ID = re.compile(r'mkt-|story|board|five$|outreach|upd-|maribeth|nysa|scott-baker|unger|parsons|resume|handout|comments')
PRIVATE_TEXT = re.compile(r'HubSpot|story bank|story-bank|customers repo', re.I)
UTC_TO_CT = dt.timedelta(hours=-6)  # CST; good enough for Oct-Mar. CDT (-5) before Nov 1.


def ct(ts):
    if not ts:
        return ''
    t = dt.datetime.fromisoformat(ts.replace('Z', '+00:00')).replace(tzinfo=None)
    off = dt.timedelta(hours=-5) if t < dt.datetime(2026, 11, 1, 7) else UTC_TO_CT
    t = t + off
    return t.strftime('%a %b %d, %I:%M %p CT').replace(' 0', ' ')


def clean(s):
    return (s or '').replace('—', ' - ').replace('–', '-').strip()


def item_date(doc_id, d):
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', doc_id)
    return dt.date(int(m[1]), int(m[2]), int(m[3]))


def week_monday(day):
    sunday = day - dt.timedelta(days=(day.weekday() + 1) % 7)
    return sunday + dt.timedelta(days=1)


def is_private(doc_id, d):
    return bool(PRIVATE_ID.search(doc_id)) or bool(PRIVATE_TEXT.search(json.dumps(d)))


def render(monday, docs, public):
    sunday = monday - dt.timedelta(days=1)
    saturday = monday + dt.timedelta(days=5)
    answered = [x for x in docs if x[1].get('status') == 'answered']
    qn = sum(len(x[1].get('answers') or {}) for x in answered)
    out = [f'# Morning Review record - week of {monday:%B} {monday.day}, {monday.year}',
           '',
           f'Nights {sunday:%a %b} {sunday.day} to {saturday:%a %b} {saturday.day}. Built from the Morning Review form '
           '(https://claude.ai/artifact/Qki5RDPiqT6N2orsZ9Vb4d) by ops/tools/form_record.py - The Chat Is Not Your Memory: '
           'the form is the inbox, this file is the record.',
           '']
    if public:
        out += ['Public copy: marketing, HubSpot, board, outreach, customer and story-bank items are left out. '
                'The full record is in the Claude project (morning-review/).', '']
    out += [f'**{len(docs)} items - {len(answered)} answered ({qn} answers), {len(docs) - len(answered)} still open.**', '']
    for doc_id, d in docs:
        qs = d.get('questions') or []
        ans = d.get('answers') or {}
        out.append(f'## {clean(d.get("title")) or doc_id}')
        meta = [f'`{doc_id}`']
        if d.get('night'):
            meta.append(f'night of {d["night"]}')
        if d.get('status') == 'answered':
            meta.append(f'answered {ct(d.get("answeredAt"))}')
        else:
            meta.append('OPEN')
        out += [' - '.join(meta), '']
        if d.get('summary'):
            out += [clean(d['summary']), '']
        if d.get('link'):
            out += [f'Link: [{clean(d.get("linkLabel")) or "Open it"}]({d["link"]})', '']
        for q in qs:
            a = ans.get(q['id']) or {}
            choice = clean(a.get('choice'))
            note = clean(a.get('note'))
            line = f'- {clean(q.get("text"))} -> ' + (f'**{choice}**' if choice else '_no choice_')
            if note:
                line += f' - note: "{note}"'
            out.append(line)
        out.append('')
    return '\n'.join(out).rstrip() + '\n'


def main():
    src, full_dir, pub_dir = sys.argv[1:4]
    only = {week_monday(dt.date.fromisoformat(x)) for x in sys.argv[4:]}
    weeks = {}
    for f in glob.glob(os.path.join(src, '*.json')):
        doc_id = os.path.basename(f)[:-5]
        d = json.load(open(f))
        d = d.get('data', d) if 'questions' not in d else d
        weeks.setdefault(week_monday(item_date(doc_id, d)), []).append((doc_id, d))
    os.makedirs(full_dir, exist_ok=True)
    os.makedirs(pub_dir, exist_ok=True)
    for monday, docs in sorted(weeks.items()):
        if only and monday not in only:
            continue
        docs.sort(key=lambda x: (x[1].get('order') or 0, x[0]))
        name = f'week-of-{monday.isoformat()}.md'
        open(os.path.join(full_dir, name), 'w').write(render(monday, docs, False))
        pub = [x for x in docs if not is_private(*x)]
        open(os.path.join(pub_dir, name), 'w').write(render(monday, pub, True))
        print(name, len(docs), 'items,', len(pub), 'public')


if __name__ == '__main__':
    main()
