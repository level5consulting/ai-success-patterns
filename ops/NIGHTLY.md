# Nightly plan - read by the nightly run (Sunday-Thursday, ~11:30 PM CT)

The nightly scheduled task opens this file, finds tonight's section by date (America/Chicago), and does it. Anything not finished moves to the next night's section with a note. Each run edits this file on the `ops` branch for the following nights (Thursday night writes next week's plan here).

## Standing rules (Greg)
- Never merge to main without Greg's explicit "publish". Work on that night's branch `overnight-YYYY-MM-DD`, branched from main (or from an unmerged earlier overnight branch, so work carries forward).
- Commits: `git -c user.name="Greg Stellflue" -c user.email="greg.stellflue@level5iveconsulting.com" commit`, message ending with the Co-Authored-By / Claude-Session trailer.
- Morning Review form (https://claude.ai/artifact/Qki5RDPiqT6N2orsZ9Vb4d, collection `reviews`): one item per thing; every item links directly to each file (GitHub blob link) or carries the text itself; never a compare/diff view; posts and image prompts written out in the item; each decision its own question. Do not restyle the form. Read Greg's answers first and apply only what he accepted.
- Plans in Motion (https://claude.ai/artifact/FnwFR72FeCeDnUmJZVVgTQ): data is ops/data/plans.json. Every card for this week has a `link` (form URL + `#<doc id>` for decisions; GitHub blob or page URL otherwise). Move cards off "Needs Greg" once answered. Publish: upload the JSON as an asset, then update `datasets/plans` (source url + updated) with if_version.
- Plans in Motion link standard (Greg approved November 3, 2026) - one click to the actual thing:
  - Needs Greg, a decision: the exact Morning Review form item (form URL + #<doc id>).
  - Needs Greg, something to read or test: the exact file (GitHub blob link) or the page; posts and rants written into a form item and linked there.
  - On track: the work in progress - draft file, artifact, or live page.
  - Done: the finished result - live page, published post, final file; run record as fallback.
  - Update me: a form item asking for the status, with a note box.
  - Planned / Idea: where it's written down - week plan, BACKLOG, rant backlog.
  - Sessions: the session's folder on GitHub.
  - A decision always goes to the form; no diff views; nothing that lives only in a project doc or chat - put its text in a form item. Every card for this week has a link.
- Night Shift Tracker (https://claude.ai/artifact/MjuCxQgA7Uwa6uvueWtUPY): data is ops/data/night-runs.json, same upload-and-update method (`datasets/runs`).
- Patterns Tracker: ops/data/patterns.json (`datasets/patterns`).
- Page builder: `python3 ops/tools/buildpage.py ops/tools/cfgNN.json` (template patterns/19-research-partner-not-oracle.html; see cfg21.json).
- Writing: regular dashes, never em dashes. LinkedIn posts never end with a question; tagline "Bringing back the past to help our future." above the hashtags. Light backgrounds. Credits paraphrased, consent only. Pattern names must work said out loud at work.
- No Friday or Saturday runs. Up to 5 patterns into In Review a week, 2 published.
- If a step can't finish, write where it stopped in the run record (records/overnight-YYYY-MM-DD.md) and as a form item, then carry on with the next step.
- End every run: commit and push the overnight branch and the `ops` branch (data files and this plan), update the three trackers, and write the handoff in the project doc ai-success-patterns/handoff.md.

## Tuesday, November 3
1. Apply Greg's form answers (items 2026-11-02-rt24, -pmo-fixes, -p21, -p26, 2026-11-03-rant4). Branch from overnight-2026-11-02 if it isn't merged.
2. Build 23 AI Friction's In Review page and home card; remove it from Coming Soon.
3. Move 18 Avoid the Naughty List into In Review the same way.
4. Night Shift Tracker rebuild (Pattern 04) - propose, don't remove features; keep the form separate.
5. Plans in Motion: change the Session 2 card (P22) link from the slide deck to the Session 2 folder on GitHub (find where Session 2's files live - sessions/ and records/ - and link the folder that holds them; if they're spread out, gather them into one session folder on that night's branch and link it). Apply the same to any other session card.
6. Certification prep for Wed Nov 4 (Claude day): pick a more advanced Claude Academy course (Claude 101 was too basic); verify on Anthropic's pages; note it in the project doc learning/claude-certification-plan.md.

## Wednesday, November 4
1. PMO / EPMO starter pack - ChatGPT version (SKILL.md skills; check OpenAI's own pages for current install steps).
2. Draft AI Reads, Tools Copy.
3. Webinar Session 3 draft: Assemble the Team (Pattern 08), publishes Tue Nov 10, Greg records Mon Nov 9. Draft records/webinar-session-03.md from records/webinar-session-02.md (5 acts, ~10 min, Act III about half and live). Propose leader (Carla Brennan default), Act II failure, Act IV evidence (verified sources only), [GREG: ...] humor spots, page copy, slides outline, Taco Tuesday Ep 3 fit check (records/taco-tuesday-promos.md), and a red team (4 people, one adversarial). Questions in the form.
4. Certification prep for Thu Nov 5 (Copilot day).

## Thursday, November 5
1. PMO / EPMO starter pack - Copilot version.
2. Plan the other six starter packs (order for Greg to choose).
3. Webinar Session 3 red team: two rounds, findings only, records/red-team-webinar-03.md; each change its own form question (Accept / Reject / Accept with edits).
4. Next week's plan (records/week-plan-2026-11-09.md) and next week's sections in this file. Services LinkedIn post is tentatively next week.
5. Certification prep for Fri Nov 6 (ChatGPT day).

## Sunday, November 8
1. Webinar Session 3 finish: apply only the red-team changes Greg accepted; update the script; build the slides as a new Slides artifact matching Session 2 (https://claude.ai/artifact/Tk3Pb8mPNwRJtpXsy7h4jq: light backgrounds, Oswald and Public Sans, salsa-red accent, speaker notes); Act III paste-ins and prepared answers; Taco Tuesday Ep 3 and its LinkedIn post.
2. Stage the week's two publishes for Monday.
3. Certification prep for Mon Nov 9.
