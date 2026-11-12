# Pattern 24 - Dashboards That Answer a Question

**Category:** Governance (Greg, October 30, 2026)
**Maturity level:** Leadership (Greg, October 30, 2026)
**Status:** IN REVIEW page built November 4, 2026 (draft 2, approved by Greg November 4; awaiting publish). patterns/24-dashboards-that-answer-a-question.html.

**Where it came from:** BACKLOG.md, "Dashboards That Answer a Question (working title)" - AI builds dashboards full of tiles that answer nothing. Connections: Ore Is Not Gold (talk), Pattern 01, Pattern 11, Greg's EPMO audience. Also this project's own Plans in Motion and Patterns Tracker dashboards (Greg, October 29: "I need a better way to visualize all the plans I have in motion") - each built around one question.

**Lead (draft):** Ask AI for a dashboard and you'll get one in minutes: twelve tiles, four charts, every number it could find. It looks like insight. It answers nothing, because nobody said what decision it was for. Start from the decision the viewer has to make, and show only what would change it.

---

## Problem
**Every number, no answer**

We built very fancy dashboards with AI to demonstrate our SPM solutions. They looked great and had zero impact. Then we built a portfolio grader: it graded each portfolio A to F, with clear statements of what had to happen to improve the grade. One question - "how healthy is this portfolio, and what do we fix?" - beat every chart.

AI has made dashboards nearly free. Point it at a spreadsheet or a system and it will produce tiles, charts and trend lines in minutes - more than any analyst would have built in a week.

That's the trap. When building is free, nothing gets left out. The dashboard shows everything that can be counted, so the one number that matters sits next to eleven that don't. Leaders scroll, nod, and make the decision the way they would have anyway.

PMOs know this one well. Status dashboards with forty projects in green, yellow and red - and no answer to the only question the executive asked: "what do I need to do this week?"

Worse, an AI-built dashboard looks finished. Clean charts and confident labels make it easy to forget that nobody checked whether the numbers are right, or whether they mean what the label says.

The failure isn't using AI to build dashboards. It's building them before anyone has named the question.

## Value
**Fewer numbers, better decisions**

- **Decisions get made from the dashboard** - each one is built for a named decision and a named person.
- **Less to read** - only the figures that would change the decision make the main view, and it fits on one screen, phone included.
- **Numbers you can trust** - every figure shows where it came from, and it's checked against its source before first use and again after any change to its query.
- **Dashboards that retire** - when the decision is made or the question changes, the dashboard changes or is archived.
- *Measure it:* for each dashboard, can its owner say the decision it serves in one sentence? How many tiles were removed? How often is it opened before the meeting it was built for?

---

## Context (first pass)
**When this pattern applies**

Use it whenever someone asks AI for a dashboard, report or scorecard - especially for leaders and PMOs, where dashboards multiply fastest. It also applies to dashboards you already have: most will fail the one-sentence test.

It's not about chart design or a particular tool. A beautiful dashboard that answers the wrong question still fails.

## Solution (first pass)
**Name the decision, then build only what changes it**

**Step 1: Name the decision and the person.** Before asking AI for anything, write one sentence: who looks at this, and what do they decide from it? "The CIO decides each Monday which two projects get help." If you can't write it, you don't need a dashboard yet. If a dashboard serves several people, build one view per decision - or one page with the decision sentence at the top of each section.

**Step 2: List what would change the decision.** Ask: what would make them decide differently? Those are the only figures that belong. Everything else goes to a detail page or stays in the source system - findable, but off the main view.

**Step 3: Give AI the decision, not the data - and let it design.** Prompt with the sentence from Step 1 and the list from Step 2. Use AI for what it's good at: proposing the fewest figures that answer the question, designing the visuals and layout, and saying what it left out and why.

**Step 4: Have AI write the code, not the numbers.** The figures come from code or queries the AI writes against the source data - never from the AI's own arithmetic (Models Are Not Good at Everything). Each figure shows where it came from, and someone checks it against the source before first use and again after any change to its query (Research Partner, Not All-Knowing Oracle).

**Step 5: Retire it when the question changes.** Put the decision sentence at the top of the dashboard. When the decision is made or the question changes, update the dashboard, or archive it with the date and the decision it served.

---

## Notes (planned)
- **Ore is not gold:** more charts (ore) is not more insight (gold).
- **This library's own example:** the Patterns Tracker answers "what's published, in review and coming"; Plans in Motion answers "what needs me this week." Each started from one question.
- **Connections:** Begin with the End in Mind (the decision is the end in mind); The Productivity-to-Headcount Trap (measures that hold up); AI Friction (don't build what nobody needs); Models Are Not Good at Everything and Research Partner, Not All-Knowing Oracle (check the numbers).
- **Greg's example (October 30, 2026):** the portfolio grader now opens the Problem (red team change 1, accepted November 3).

## Use this pattern (first pass)
*Paste this into any AI system's custom instructions or at the start of a conversation to run Dashboards That Answer a Question.*

```
# Dashboards That Answer a Question

You are running Dashboards That Answer a Question, an AI Success Pattern (aisuccesspatterns.com/patterns/24-dashboards-that-answer-a-question.html).

The pattern's premise: AI makes dashboards nearly free, so they fill with every number that can be counted and answer nothing. Start from the decision the viewer has to make, and show only what would change it.

## Phase 1 - Name the decision
Before building anything, ask the user in one question: who will look at this, and what do they decide from it? Help them write it as one sentence. If they can't, say a dashboard may not be needed yet.

## Phase 2 - Find what would change it
Ask what would make that person decide differently. List those figures - usually three to six. Anything else goes to a detail page or stays in the source system.

## Phase 3 - Design the fewest figures
First ask how the person will see it - phone, wall screen, or a slide in a meeting - and design for that. Propose a layout and visuals with the decision sentence at the top and only the figures from Phase 2. Offer a grade with a "what to fix" line as a standard option. Say what you left out and why.

## Phase 4 - Write the code, then check the numbers
Write the queries or code that produce each figure from the source data - never compute figures in your head. For each figure, name its source and how to check it. If the data isn't available, say so.

## Behavior rules
- One question at a time
- No dashboard without a decision sentence
- Fewer figures is better; explain every cut
- Every number shows its source
```

---

## Questions for Greg - answered
Category Governance; level Leadership; portfolio grader example; red team approved (October 30, 2026). All 8 red-team changes accepted November 3, 2026.
