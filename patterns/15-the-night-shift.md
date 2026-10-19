# Pattern 15 - The Night Shift (working title)

**Category:** Agentic (proposed - AI works unattended on delegated tasks; confirm)
**Maturity level:** Practice (proposed - a repeatable way of working an individual or team can adopt; confirm)
**Status:** FIRST DRAFT (overnight, October 18-19, 2026) - Problem and Value, plus a first pass at Context and Solution. Not red-teamed (live red team with Greg). Not built as HTML. Not on the site.

**Lead (draft):** Most people only use AI while they're sitting with it, so AI moves at the speed of their calendar. Hand it the work that doesn't need you - research, checking, drafting, records - to run while you're away, and keep the decisions for the morning.

---

## Problem
**AI works only when you're watching**

Most professionals use AI the way they'd use a calculator: open it, ask, wait, read, ask again. The AI is fast, but the work still moves at the speed of the person sitting with it. Every hour they spend in meetings, on calls, or asleep is an hour the AI does nothing. The bottleneck isn't the model. It's the calendar.

The people who try to get past that tend to fail in the opposite direction. They hand AI a task, let it run unattended, and come back to find it changed things nobody approved: a document rewritten, a message sent, a file overwritten. One bad morning like that and most people go back to watching every step.

So the work splits into two bad options. Supervise everything, and AI can only go as fast as you can watch. Supervise nothing, and you've given away decisions that were never the AI's to make.

The missing piece is a clear line between the two kinds of work in almost every task: the work that needs judgment, and the work that only needs doing.

## Value
**Work moves while you're away, and every decision is still yours**

- **The work keeps moving when you don't.** Research, verification, drafting, and record-keeping get done overnight or while you're in meetings. You start the day reviewing finished work instead of starting it.
- **You spend your time on judgment.** Your hours go to the calls only you can make - what to accept, what to change, what to publish - not to the hours of preparation behind them.
- **Nothing changes without your approval.** Unattended work lands as drafts and findings behind a review, never as live changes. The speed doesn't cost you control.
- **The work is easy to review.** Each run ends with a short summary of what's ready and what needs a decision, so the morning review takes minutes, not hours.
- *Measure it:* elapsed days from idea to reviewed draft, before and after; share of overnight output accepted with no rework.

---

## Context (first pass)
**When this pattern applies**

This pattern applies when work has a lot of preparation behind a small number of decisions: research before a recommendation, checking sources before publishing, drafting before review, updating records after a change. It fits individuals with full calendars and teams whose AI use has stalled at "only when someone is watching."

It needs tools that can work unattended - an AI that can run a scheduled or delegated task and save its results somewhere you'll find them. And it needs a place for results to wait for you: a branch, a draft folder, a review queue.

It is not for decisions with real consequence, anything that can't be undone, or anything that goes straight to customers. Those stay with the person. It is also not the same as Pattern 04, The AI Operations Manager: 04 is recurring coordination work; this pattern is delegating substantive work and reviewing it later.

## Solution (first pass)
**Split the work by judgment, brief it to run cold, and review it in the morning**

**Step 1: Split the work by judgment.** Go through the task and sort each piece. Research, verification, drafting, record-keeping, and finding problems can run unattended. Decisions, naming, choosing which problems to fix, and publishing stay with you. Red teams are a good example: the findings can come overnight; the calls on them happen with you in the room (see Pattern 08).

**Step 2: Write each task as a standalone brief.** The AI will start cold, with no one to ask. Write what to do, where the inputs are, what to produce, and where to put it - the same brief you'd leave a capable colleague covering for you (see Pattern 01 and Pattern 02).

**Step 3: Nothing goes live while you're away.** Every result lands as a draft, a branch, or a document behind your approval. If a task can't be done without changing something live, it isn't a night-shift task.

**Step 4: Ask for findings, not changes.** For reviews and checks, have the AI propose numbered changes you can accept or reject, instead of applying them. You keep the judgment; it does the legwork.

**Step 5: End every run with a morning summary.** What's ready, what needs a decision, what it couldn't do and why. Then review piece by piece: accept, reject, or redirect.

**Step 6: Keep the record.** Log what ran, what it found, and what you decided, in the handoff record and the backlog, so overnight work never becomes a ghost (see Pattern 12).

---

## Notes (planned)
- **The real example:** This library. Launched Monday, October 12, 2026; within the week it was running overnight work cycles (backlog note says three by Friday - Greg to confirm the count):
  - Run 1 - handoff records for every pattern, a source-verification pass that found four errors on the live site, redrafts of Patterns 01-09, and a first draft of Pattern 13.
  - Run 2 - a value report across every pattern, red-team findings for 01-08, Embed the Expert prep, and speaking-venue research.
  - Each morning, Greg reviewed and decided piece by piece. Nothing went live without his approval.
- **Signs it's going wrong:** you start skipping the morning review; the AI starts changing things instead of proposing; briefs get vaguer and results need more rework.
- **Connections:** Pattern 04 (recurring coordination vs. delegated substantive work); Pattern 08 (findings overnight, calls live); Pattern 03 (source verification is ideal overnight work); Pattern 12 (records keep overnight work from becoming ghosts); Pattern 01 (each brief defines its own destination).

## Sources
- None external yet. The real example is Greg's own work on this library (October 12-18, 2026). Possible supporting research to look for if Greg wants it: studies on how long AI agents can work on tasks unattended, and data on how much of knowledge work is preparation vs. decision.

## Questions for Greg
1. **Name.** "The Night Shift" - keep it? It's memorable, but the pattern also covers "while you're in meetings," not only overnight. Alternatives: "Work While You're Away," "Delegate the Legwork."
2. **Category and level.** Agentic, Practice - confirm.
3. **The real example.** Use this library's first week as the Notes example (and a talk story)? It's the strongest evidence we have - and it's yours.
4. **How tool-specific to be.** Keep it tool-neutral ("an AI that can run a scheduled or delegated task"), or name the kinds of tools that support unattended work?
5. **Coming Soon card.** Add it to the site now, or wait until after the live red team?
6. **Your own line.** What surprised you most in the first week of working this way? One sentence in your words would anchor the Problem or the Notes.
