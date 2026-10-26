# Pattern 20 - Iterate to the Destination

**Category:** Conversational (Coming Soon card, October 15, 2026)
**Maturity level:** Practice (proposed)
**Status:** FIRST DRAFT (overnight, October 25-26, 2026) - Problem, Value, first-pass Context and Solution, Notes plan, first-pass "Use this pattern." Not red-teamed (overnight Monday after Greg approves a team). Not built as HTML.

**Where it came from:** Shubham Dwivedi's comment on Greg's Pattern 02 post (October 14, 2026): "On some occasions, defining the exact value statement might not be feasible right at the beginning & in such cases, how would a value statement evolve with progress." Pattern 01 already points here: "When not to use it: exploratory work, where you can't name the destination until you've seen a few drafts."

**Lead (draft):** Sometimes you can't say what "done" looks like until you've seen a few attempts. Write down your best guess at the destination anyway, label it a guess, and rewrite it after every round - so the work moves toward something instead of in circles.

---

## Problem
**No destination, or a fake one**

Pattern 01 says to define what "done" looks like before you start. Most of the time that's right. But some work can't be defined up front: a new strategy, an early product idea, a problem nobody has framed yet. You don't know what good looks like until you've seen something that isn't it.

People handle this one of two ways, and both fail. Some skip the destination and just start prompting. The AI is happy to go wherever they point it, so they go around in circles - twenty drafts, each different, none better, and no way to tell when to stop.

Others write a destination anyway and treat it as fixed. Three rounds in, they've learned the real question is different, but the original goal is still steering the work. They end up with a polished answer to the wrong question.

The failure isn't starting without a clear destination. It's never writing down where you think you're going, so you can't tell whether you're getting closer.

## Value
**Exploration that converges**

- **Each round gets closer** - because each draft is judged against a destination, even a rough one.
- **What you learned is written down** - the changes to the destination are the record of what the exploration taught you.
- **You know when to stop** - when the destination stops changing and the draft meets it.
- **Sponsors see progress, not churn** - "here's how our definition of success has sharpened" is a status update; twenty unrelated drafts are not.
- *Measure it:* how many rounds until the destination stops changing, and how many drafts were thrown away entirely.

---

## Context (first pass)
**When this pattern applies**

Use it when you can't fill in Pattern 01's destination honestly before you start: new strategy or positioning, an early-stage product or service idea, research into a question nobody has framed, a first attempt at something your organization has never done.

It's also the right pattern when a sponsor says "I'll know it when I see it." Turn that into a written guess you can both react to.

When not to use it: when the destination is knowable and you're just skipping the work of writing it down. If you could fill in Pattern 01's format, audience, constraints and success criteria in five minutes, do that instead.

## Solution (first pass)
**Write the destination as a guess, then rewrite it every round**

**Step 1: Write your best-guess destination.** Use Pattern 01's four parts - format, audience, constraints, success criteria - and fill in what you can. Label it "Destination, version 1 - a guess." Blanks are fine; name them as questions.

**Step 2: Ask for options, not an answer.** In early rounds, ask the AI for two or three different takes, not one polished draft. Different options show you what you actually want faster than one draft you have to edit.

**Step 3: React, then rewrite the destination.** After each round, say what you liked, what you didn't, and why. Then update the destination - not just the draft. "Version 2: it's for the operations leaders, not the board" is the real progress.

**Step 4: Keep the versions.** Keep each version of the destination, with one line on what changed and why. That history is what you learned, and it's what you show a sponsor.

**Step 5: Lock it, then switch to Pattern 01.** When the destination stops changing for a round, lock it and say so. From there, the work is ordinary Pattern 01: drafts against a fixed destination until it's met.

---

## Notes (planned)
- **Companion to Pattern 01**, not a replacement. Pattern 01's "When not to use it" already links here; this page links back.
- **Connections:** Pattern 05, Avoid AI Slop (the interview can help write version 1); Pattern 16, The Staged Journey (destinations sharpen stage by stage); Pattern 12 (keep the versions as the record).
- **Greg's example:** [GREG: a real piece of work where the goal changed as you went - for example, the AI Success Patterns site itself, or the 5-act webinar that replaced the first 8-slide version.]
- **Contributor:** Shubham Dwivedi raised the question. Credit only with his consent (Greg to engage).

## Use this pattern (first pass)
*Paste this into any AI system's custom instructions or at the start of a conversation to run Pattern 20.*

```
# Iterate to the Destination

You are running Pattern 20: Iterate to the Destination from AI Success Patterns (aisuccesspatterns.com/patterns/20-iterate-to-the-destination.html).

The pattern's premise: sometimes you can't say what "done" looks like until you've seen a few attempts. Write the best guess at the destination anyway, label it a guess, and rewrite it after every round, so the work moves toward something instead of in circles.

## Phase 1 - Write destination version 1
Ask the user, in one question, what they're working on. Then draft "Destination, version 1 - a guess" with four parts: format, audience, constraints, success criteria. Fill in what you can from their answer and write the blanks as questions. Ask the user to correct it. Don't ask about every blank - one question at a time.

## Phase 2 - Offer options
Produce two or three short, clearly different takes that each fit the destination differently. Keep them short - sketches, not finished drafts. Ask which parts the user likes and why.

## Phase 3 - Rewrite the destination
From the user's reaction, write the next version of the destination. Show what changed in one line ("Version 2: audience is operations leaders, not the board"). Keep every earlier version in a short list. Then offer the next round of options against the new version.

## Phase 4 - Lock it
When a round ends with no change to the destination, say so and ask the user to lock it. Once locked, switch to drafting against the fixed destination (Pattern 01), and stop offering new directions unless the user reopens it.

## Behavior rules
- One question at a time
- Always show the current destination version before new options
- Options are short and different from each other - not three versions of the same thing
- Never quietly change the destination - every change is named
- The user decides when the destination is locked
```

---

## Sources
- Shubham Dwivedi, LinkedIn comment, October 14, 2026 (sources/shubham-dwivedi-iterate-to-destination.md). Idea only; no quote on the page without his consent.
- Pattern 01's existing "When not to use it" text on the live site.

## Questions for Greg
1. **Your example.** A real piece of work where the destination changed as you went. Candidates: the AI Success Patterns site itself; the webinar going from 8 slides to the 5-act arc; something from client work.
2. **Level.** Practice (proposed) or Foundation?
3. **Shubham.** Ask him whether he'd like credit for raising the question (and whether he'd review the draft)?
4. **Step 2, options instead of one draft.** Keep as a step, or fold into Step 3?
5. **Red team.** Proposed team: **Gary Novak (adversarial)** - COO who thinks "iterating" is an excuse for not knowing what you want and wants a fixed scope and date; **Anita Rao** - SAFe release train engineer who runs PI planning and lives with evolving goals; **Mei Chen** - product manager at an early-stage company; **Paul Okafor** - executive sponsor who has said "I'll know it when I see it." Approve or swap?
