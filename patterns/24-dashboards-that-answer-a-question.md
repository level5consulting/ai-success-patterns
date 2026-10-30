# Pattern 24 - Dashboards That Answer a Question

**Category:** Governance (proposed - the card says Governance; Accuracy also fits)
**Maturity level:** Leadership (proposed)
**Status:** FIRST DRAFT (overnight, October 29-30, 2026). Not red-teamed. Not built as HTML.

**Where it came from:** BACKLOG.md, "Dashboards That Answer a Question (working title)" - AI builds dashboards full of tiles that answer nothing. Connections: Ore Is Not Gold (talk), Pattern 01, Pattern 11, Greg's EPMO audience. Also this project's own Plans in Motion and Patterns Tracker dashboards (Greg, October 29: "I need a better way to visualize all the plans I have in motion") - each built around one question.

**Lead (draft):** Ask AI for a dashboard and you'll get one in minutes: twelve tiles, four charts, every number it could find. It looks like insight. It answers nothing, because nobody said what decision it was for. Start from the decision the viewer has to make, and show only what would change it.

---

## Problem
**Every number, no answer**

AI has made dashboards nearly free. Point it at a spreadsheet or a system and it will produce tiles, charts and trend lines in minutes - more than any analyst would have built in a week.

That's the trap. When building is free, nothing gets left out. The dashboard shows everything that can be counted, so the one number that matters sits next to eleven that don't. Leaders scroll, nod, and make the decision the way they would have anyway.

PMOs know this one well. Status dashboards with forty projects in green, yellow and red - and no answer to the only question the executive asked: "what do I need to do this week?"

Worse, an AI-built dashboard looks finished. Clean charts and confident labels make it easy to forget that nobody checked whether the numbers are right, or whether they mean what the label says.

The failure isn't using AI to build dashboards. It's building them before anyone has named the question.

## Value
**Fewer numbers, better decisions**

- **Decisions get made from the dashboard** - each one is built for a named decision and a named person.
- **Less to read** - only the figures that would change the decision make the page.
- **Numbers you can trust** - every figure shows where it came from, and someone checked it.
- **Dashboards that retire** - when the decision is made or the question changes, the dashboard changes or goes away.
- *Measure it:* for each dashboard, can its owner say the decision it serves in one sentence? How many tiles were removed? How often is it opened before the meeting it was built for?

---

## Context (first pass)
**When this pattern applies**

Use it whenever someone asks AI for a dashboard, report or scorecard - especially for leaders and PMOs, where dashboards multiply fastest. It also applies to dashboards you already have: most will fail the one-sentence test.

It's not about chart design or a particular tool. A beautiful dashboard that answers the wrong question still fails.

## Solution (first pass)
**Name the decision, then build only what changes it**

**Step 1: Name the decision and the person.** Before asking AI for anything, write one sentence: who looks at this, and what do they decide from it? "The CIO decides each Monday which two projects get help." If you can't write it, you don't need a dashboard yet.

**Step 2: List what would change the decision.** Ask: what would make them decide differently? Those are the only figures that belong. Everything else goes to a detail page or nowhere.

**Step 3: Give AI the decision, not the data.** Prompt with the sentence from Step 1 and the list from Step 2. Ask it to propose the fewest figures that answer the question - and to say what it left out and why.

**Step 4: Check every number at the source.** Each figure shows where it came from. Someone checks it against the source before the dashboard is used (Pattern 19, Research Partner, Not All-Knowing Oracle; Pattern 10, Models Are Not Good at Math).

**Step 5: Retire it when the question changes.** Put the decision sentence at the top of the dashboard. When the decision is made or the question changes, update the dashboard or delete it.

---

## Notes (planned)
- **Ore is not gold:** more charts (ore) is not more insight (gold).
- **This library's own example:** the Patterns Tracker answers "what's published, in review and coming"; Plans in Motion answers "what needs me this week." Each started from one question.
- **Connections:** Pattern 01, Begin with the End in Mind (the decision is the end in mind); Pattern 11 (measures that hold up); Pattern 23, AI Friction (don't build what nobody needs); Pattern 10 and 19 (check the numbers).
- **Greg's example:** [GREG: a PMO or executive dashboard that showed everything and answered nothing - or one that worked because it answered one question.]

## Use this pattern (first pass)
*Paste this into any AI system's custom instructions or at the start of a conversation to run Pattern 24.*

```
# Dashboards That Answer a Question

You are running Pattern 24: Dashboards That Answer a Question from AI Success Patterns (aisuccesspatterns.com/patterns/24-dashboards-that-answer-a-question.html).

The pattern's premise: AI makes dashboards nearly free, so they fill with every number that can be counted and answer nothing. Start from the decision the viewer has to make, and show only what would change it.

## Phase 1 - Name the decision
Before building anything, ask the user in one question: who will look at this, and what do they decide from it? Help them write it as one sentence. If they can't, say a dashboard may not be needed yet.

## Phase 2 - Find what would change it
Ask what would make that person decide differently. List those figures - usually three to six. Anything else is detail or out.

## Phase 3 - Propose the fewest figures
Propose a layout with the decision sentence at the top and only the figures from Phase 2. Say what you left out and why.

## Phase 4 - Check the numbers
For each figure, name its source and how to check it. Never invent or estimate a number; if the data isn't available, say so. Calculations are done in code or the source system, not in your head.

## Behavior rules
- One question at a time
- No dashboard without a decision sentence
- Fewer figures is better; explain every cut
- Every number shows its source
```

---

## Questions for Greg
1. **Category.** Governance (the card) or Accuracy?
2. **Level.** Leadership (proposed) or Practice?
3. **Your example.** A dashboard that showed everything and answered nothing - or one that worked.
4. **Red team.** Proposed: **Diane Kowalski (adversarial)** - VP of finance who wants every metric visible "in case someone asks"; **Marcus Reyes** - EPMO director who owns forty project status dashboards; **Leah Brandt** - BI analyst who now builds dashboards with AI in an hour; **Tom Okafor** - COO who reads dashboards on his phone between meetings. Approve or swap?
