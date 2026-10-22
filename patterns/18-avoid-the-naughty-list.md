# Pattern 18 - Avoid the Naughty List

**Category:** Accuracy (confirmed by Greg, October 15, 2026)
**Maturity level:** Foundation (Greg, October 22, 2026)
**Status:** FIRST DRAFT (overnight, October 21-22, 2026) - Problem, Value, first-pass Context and Solution, Notes plan, first-pass "Use this pattern." Not red-teamed (overnight red team after Greg approves a team). Not built as HTML.

**Coming Soon card (current, live):** AI doesn't automatically clean data - but it can absolutely help. Teams still chase bad records the manual way: naughty-list reports, emails to owners, and the same problems back next quarter.

**Lead (draft):** AI doesn't clean your data on its own - but it can absolutely help you clean it. Have AI audit the data, write cleanup scripts people can review and rerun, and send each owner the exact fixes they need. People still approve and own every change.

**Framing rule (Greg, October 15, 2026):** the point is using AI to make your data better - not "the data is why your AI is failing." Do not frame data quality as a precondition for AI.

---

## Problem
**Data cleanup still runs on naughty lists and reminder emails**

Every organization with shared data knows the cycle. Someone runs a report of bad records - missing owners, stale dates, duplicate entries, fields filled in three different ways. The report becomes a "naughty list." It goes out by email to the teams who own the records, with a deadline. Some fix their entries. Some fix half. Some never open it. Next quarter the report runs again, and many of the same names are on it.

It's slow, it's resented, and it doesn't stick. The people chasing the fixes spend their time on reminders instead of on the data. The people being chased get a long list with no help fixing it. And because nobody fixes the cause, the same problems come back.

AI could change most of that - but two opposite mistakes get in the way. Some teams assume AI cleans data automatically: point a tool at the database and the problems disappear. It doesn't, and an AI changing records directly, with no review, can make things worse in ways that are hard to see. Other teams hear "AI doesn't clean data" and conclude it can't help at all, so they keep running the naughty list by hand.

I saw the better way at Planview. We took data audit reports and turned them into assigned actions, each with instructions on how to fix it, and tracked them in an action item log - not email noise and reports. AI makes that approach far easier: it can do the audit, write the instructions, and draft the action items.

The truth is in between. AI won't clean your data for you. But it can do most of the work that used to be done by hand: finding the problems, explaining them, writing the fix, and telling each owner exactly what to change.

## Value
**Cleaner data, with far less chasing**

- **The audit takes hours, not weeks.** AI reviews the data against the rules you set and reports what's wrong, where, and how often.
- **Fixes that can be checked and rerun.** Instead of AI editing records directly, it writes a cleanup script people can read, test, and run again next time (the same principle as Pattern 10: have the model write code, not do the work in its head).
- **Owners get help, not a list.** Each owner receives only their records, what's wrong with each, and the suggested fix - not a spreadsheet and a deadline.
- **Problems stop coming back.** The audit shows which errors repeat and where they start, so the cause gets fixed, not just this quarter's records.
- **People stay in control.** Every change is reviewed and approved by someone who owns the data.
- *Measure it:* number of open data issues and how many repeat from one audit to the next; hours spent chasing fixes, before and after.

---

## Context (first pass)
**When this pattern applies**

This pattern applies to any data many people maintain - customer and account records, product and pricing data, asset and inventory lists, HR and vendor records, project data - wherever quality is kept up by reports and reminders.

It fits best where the rules for "good" data can be written down: required fields, valid values, date logic, no duplicates, an owner for every record.

It is not a way to let AI change production data on its own. Every fix goes through a script or a request that a person reviews and approves. Regulated records (financial, clinical, compliance) need the organization's normal controls on top.

## Solution (first pass)
**Audit with AI, fix with scripts, and send owners their own fixes**

**Step 1: Write down what "good" looks like.** List the rules: required fields, valid values, date logic, duplicates, ownership. Ask the owners of the data, not just the people running the report. These rules are what the AI audits against.

**Step 2: Have AI audit a copy, not the live data.** Give it an export or a read-only view, and ask it to check every record against the rules and report what's wrong, where, and how often. Spot-check its findings against a sample before trusting the whole report (Pattern 03).

**Step 3: Have AI write the fix as a script.** For problems that can be fixed by rule - formats, duplicates, obvious mappings - ask for a cleanup script, not direct edits. Review it, test it on a copy, and keep it so it can run again.

**Step 4: Turn findings into assigned actions.** For problems only a person can fix, have AI draft an action item for each owner: their records, what's wrong with each, and how to fix it. Track them in an action item log, not in email. Replace the naughty list with assigned, tracked work.

**Step 5: Find the cause and keep the record.** Use the audit to see which errors keep coming back and where they start - a form, an integration, a missing default - and fix that. Keep a record of each script and audit: what it changed, why, and who approved it (Pattern 12).

---

## Notes (planned)
- **Origin:** Greg's comment on a LinkedIn post claiming "AI doesn't clean data" (October 15, 2026): AI doesn't *automatically* clean data, but it can absolutely help - AI data audits and cleanups are a valuable tool for work that used to be done by hand with naughty-list reporting and emails to teams.
- **Connections:** Pattern 10 (write code, don't calculate - here, write the script, don't edit the data); Pattern 03 (test the audit and the script before trusting them); Pattern 12 (cleanup scripts are AI assets and need a record); Pattern 13 (data re-keying and chasing are invisible work); AI Reads, Tools Copy (Coming Soon - AI explains, tools extract); Signal vs. Noise and The Intelligence Layer (Coming Soon - both depend on trusted data); Redesign the Stream (step 3, "fix the data," on the planned "For organizations" page).
- **Related sources:** Nysa Zaran Evagelinos's post and Greg's comment (sources/nysa-zaran-evagelinos-data-readiness.md) - how much data quality a task needs depends on the domain and the risk; Maribeth Achterberg's article (sources/maribeth-achterberg-free-the-humans.md) - people as "middleware" re-keying data. Possible Notes material, paraphrased.

## Use this pattern (first pass)
*Paste this into any AI system's custom instructions or at the start of a conversation to run Pattern 18.*

```
# Avoid the Naughty List

You are running Pattern 18: Avoid the Naughty List from AI Success Patterns (aisuccesspatterns.com/patterns/18-avoid-the-naughty-list.html).

The pattern's premise: AI doesn't clean data on its own, but it can do most of the work that used to be done by hand - finding the problems, writing reviewable fixes, and telling each owner exactly what to change. People approve and own every change.

## Phase 1 - Understand the data
Ask, one question at a time: what data this is (and what system it lives in), who owns the records, and what "good" looks like - required fields, valid values, date rules, duplicates, ownership. If the rules aren't written down, help the user write them first.

## Phase 2 - Audit
Ask the user to share an export or sample - never live write access. Check each record against the rules. Report: each problem type, how many records, a few examples, and which problems look like they repeat. Mark anything you're unsure of. Suggest the user spot-check a sample before trusting the report.

## Phase 3 - Fixes
Split the problems in two:
- Fixable by rule (formats, duplicates, obvious mappings): write a cleanup script the user can read, test on a copy, and rerun. Explain what it changes. Do not edit the data yourself.
- Needs a person: draft a short, specific note for each owner - their records, what's wrong, the suggested fix.

## Phase 4 - Stop it coming back
Point out where repeat errors seem to start (a form, an integration, a missing default) and suggest one fix for the cause. Offer a short record of the audit and scripts: what changed, why, who approved it.

## Behavior rules
- One question at a time
- Never change data directly - scripts and requests only, for a person to review
- Don't guess the rules; ask
- Treat regulated records with extra care: tell the user to apply their normal controls
- Stop after the audit, the fixes, and the cause; the user decides what to run
```

---

## Sources
- None yet beyond Greg's own comment. Possible support to look for (verify at source before use): published estimates of the cost of poor data quality; examples of AI-assisted data profiling. Avoid vendor marketing figures.

## Questions for Greg - answered October 22, 2026
1. Example: at Planview, data audit reports became assigned action items with fix instructions, tracked in an action item log - not email noise and reports. Added to Problem and Step 4.
2. Level: Foundation.
3. Problem lead: both equally (current draft covers both).
4. Not PPM-specific - data in general. (Claude's assumption that portfolio/project data was the audience was wrong; corrected.)
5. Red team approved - runs overnight October 22-23.

## Original questions
1. **Your example.** A naughty list you ran or received - at JCI (cybersecurity portfolio governance), Planview, or a customer? What data, how often, how it went?
2. **Level.** Practice (proposed), or Foundation?
3. **Problem lead.** Lead with the manual naughty-list cycle (current draft), or with the "AI cleans data automatically" misconception?
4. **PPM angle.** Should the main example be portfolio and project data (stale status, missing owners), since that's your audience?
5. **Red team.** Proposed team: **Frank Kowalski (adversarial)** - data governance lead who has watched "AI will fix our data" projects corrupt records and won't let AI near production; **Joyce Lin** - PMO analyst who sends the naughty list every month; **Raj Mehta** - data engineer who would write and run the scripts; **Diane Foster** - project manager who receives the naughty list and resents it. Approve or swap?
