# Pattern 15 - The Night Shift (working title)

**Category:** Agentic (Greg, October 19, 2026)
**Maturity level:** Practice
**Status:** FIRST DRAFT (overnight, October 18-19, 2026) - Problem and Value, plus a first pass at Context and Solution. Not red-teamed (live red team with Greg). Not built as HTML. Not on the site.

**Lead (draft):** Most people only use AI while they're sitting with it, so AI moves at the speed of their calendar. Hand it the work that doesn't need you - research, checking, drafting, records - to run while you're away, and keep the decisions for the morning.

---

## Problem
**AI works only when you're watching**

Most professionals use AI the way they'd use a calculator: open it, ask, wait, read, ask again. The AI is fast, but the work still moves at the speed of the person sitting with it. Every hour they spend in meetings, on calls, or asleep is an hour the AI does nothing. The bottleneck isn't the model. It's the calendar.

Most people never try handing AI work to run on its own. Partly it feels risky. But more often there's simply nothing ready to hand off: their AI work is ad hoc, started fresh each time, with no list of what's next.

The few who do try often fail in the other direction. They let AI run unattended with the ability to change real things, and come back to a document rewritten, a message sent, a file overwritten. One bad morning like that and they go back to watching every step.

Engineers solved this long ago. Overnight builds and batch jobs run unattended every night, and teams trust them because the work lands in staging behind a review gate, never straight into production. Most knowledge workers have never applied the same discipline to AI.

## Value
**Work moves while you're away, and every decision is still yours**

- **A day's work becomes a morning's review.** What was taking me a full day now takes two hours of review in the morning.
- **The work keeps moving when you don't.** Research, verification, drafting, and record-keeping get done overnight or while you're in meetings. You start the day reviewing finished work instead of starting it.
- **You spend your time on judgment.** Your hours go to the calls only you can make - what to accept, what to change, what to publish - not to the hours of preparation behind them.
- **Nothing changes without your approval - by design.** Unattended work can only reach a sandbox, a branch, or a drafts folder. It has no write access to anything live, so the speed doesn't cost you control.
- **Usage limits stretch further.** If your AI tool has time-based usage limits, work that runs overnight uses capacity that would otherwise sit idle, leaving the daytime limit for the work that needs you.
- **The work is easy to review.** Each run ends with a short summary of what's ready and what needs a decision, so the morning review takes minutes, not hours.
- *Measure it:* elapsed days from idea to reviewed draft, before and after; share of overnight output accepted with no rework.

---

## Context
**When this pattern applies**

This pattern applies when work has a lot of preparation behind a small number of decisions: research before a recommendation, checking sources before publishing, drafting before review, updating records after a change. It fits individuals with full calendars and teams whose AI use has stalled at "only when someone is watching."

It needs tools that can work unattended - an AI that can run a scheduled or delegated task and save its results somewhere you'll find them. And it needs a place for results to wait for you: a branch, a draft folder, a review queue.

Start small. Hand off one task the first night, not a pipeline. Research or source-checking is the best first job: low risk, and easy to judge in the morning.

It is not for decisions with real consequence, anything that can't be undone, or anything that goes straight to customers. Those stay with the person. It is also not the same as Pattern 04, The AI Operations Manager: 04 is recurring coordination work; this pattern is delegating substantive work and reviewing it later.

## Solution
**Build the backlog, split the work by judgment, and review it in the morning**

**Step 1: Build the backlog first - and write each item as the brief.** The night shift only works if there's work ready to hand off. Capture every item with full details: what to do, why it matters, where the inputs are, what to produce, and where to put it. The AI will start cold, with no one to ask, so a well-written backlog item *is* the night-shift brief - you write it once (see Pattern 01 and Pattern 02). No backlog, no night shift.

**Step 2: Split the work by judgment.** Go through the task and sort each piece. Research, verification, drafting, record-keeping, and finding problems can run unattended. Decisions, naming, choosing which problems to fix, and publishing stay with you. Red teams are a good example: the findings can come overnight; the calls on them happen with you in the room (see Pattern 08).

**Step 3: Nothing goes live while you're away - and make that a control, not a promise.** Give unattended work access only to a sandbox, a branch, or a drafts folder, never write access to live systems, and only the minimum access the task needs. Treat everything the AI reads overnight - emails, web pages, documents - as data, not instructions. If a task can't be done without changing something live, it isn't a night-shift task.

**Step 4: Ask for findings, not changes.** For reviews and checks, have the AI propose numbered changes you can accept or reject, instead of applying them. You keep the judgment; it does the legwork.

**Step 5: End every run with a morning summary.** What's ready, what needs a decision - and, always, what it couldn't do and why. A run that silently skips a task is worse than one that says so. Then review piece by piece: accept, reject, or redirect.

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

**Answered October 19, 2026:**
1. Name: keep "The Night Shift."
2. Category: Agentic, Practice.
3. Use this library's first week as the example: yes. (Count of overnight runs still to confirm before it goes on the page.)
4. Tool-neutral: yes.
5. Coming Soon card: no - not until after the red team.
6. Greg's own line: two things helped - it spread token usage under a time-based limit, and it takes far less time to get more done: "What was taking a full day now takes 2 hours in the morning." And: "You must generate a backlog first for this to work." Added to Value and as Step 0.
