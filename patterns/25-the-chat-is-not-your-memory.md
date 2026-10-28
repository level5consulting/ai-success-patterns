# Pattern 25 - The Chat Is Not Your Memory

**Category:** Conversational (Greg, October 26, 2026)
**Maturity level:** Practice (Greg, October 27, 2026)
**Start here:** Step 2 of the Start-here path, between 05 Avoid AI Slop and 15 The Night Shift (Greg, October 26, 2026)
**Number:** 25 - 21 to 24 are already assigned in the approved week plan (21 Redesign the Stream, 22 Ten People, One Idea, 23 AI Friction, 24 Dashboards That Answer a Question).
**Status:** FIRST DRAFT (overnight, October 26-27, 2026) - Problem, Value, first-pass Context and Solution, Notes plan, first-pass "Use this pattern." Greg's answers applied October 27; red-teamed overnight October 27-28 (records/red-team-25.md, findings only). Not built as HTML.

**Name:** Greg, October 26, 2026.

**Lead (draft):** Long AI work loses its memory. Sessions get compressed, restarted, or handed to a new tool, and the AI quietly forgets what you told it - then rebuilds it, confidently and wrong. Keep anything that has to survive the session somewhere outside the chat, and have every session start by reading it.

---

## Problem
**The AI forgets, and doesn't tell you**

A long AI session feels like working with someone who remembers everything you've said. It isn't. Conversations have limits. When they get long, older parts are summarized or dropped. When you start a new chat, switch tools, or come back next week, most of it is gone.

The dangerous part is that the AI doesn't say what it forgot. It fills the gap. The source you pasted on Monday comes back as a paraphrase with a wrong number. The decision you made on Tuesday gets made again, differently. The correction you gave it twice needs giving a third time. Each one sounds just as confident as the real thing.

Most people treat the chat as the record: the place their sources, decisions and context live. So when the chat forgets, the work forgets - and nobody notices until someone asks "where did that come from?" or "didn't we already decide this?"

I learned this the hard way building this library. On October 15, the handoff note I gave each new session misstated what had been published. A red team I'd run on Pattern 10 left no trace. Backlog items from the day before were nearly lost. And ten days after I wrote these rules down, the project's own handoff note was ten days and nine patterns out of date. I wrote the pattern and still didn't follow Step 5. That's how easy this failure is.

The failure isn't that AI has limited memory. It's keeping the only copy of the work's memory in the one place that's guaranteed to lose it.

## Value
**Work that picks up where it left off**

- **Nothing important lives only in the chat** - sources, decisions and corrections survive a long session, a restart, or a new tool.
- **Every session starts warm** - the AI reads the record first, so you stop re-explaining and re-deciding.
- **Fewer confident mistakes** - the AI works from the saved original, not its memory of it.
- **Anyone can pick it up** - a colleague, a new session, or an overnight run (Pattern 15) can continue the work from the record alone.
- *Measure it:* how often you re-explain context or re-make a decision you already made; how many errors trace back to a source or decision the AI "remembered" wrong.

---

## Context (first pass)
**When this pattern applies**

Use it for any AI work that runs longer than one sitting: a project over days or weeks, a long research or writing effort, a recurring workflow, anything you'll hand to someone else or run unattended.

It matters most when the work depends on things the AI can't re-derive: text you pasted, decisions you made, corrections you gave, and the reasons behind them.

It is not about which tool has the biggest memory. Built-in memory and project features help, but they decide on their own what to keep. This pattern is about keeping your own record of what matters.

## Solution (first pass)
**Give the work a written memory, outside the chat**

**Step 1: Pick one home for the work's memory.** A folder, a shared document, a project space, or a repository such as GitHub - somewhere that keeps versions and that you and the AI can both read. This library lives in GitHub; a shared folder works just as well. One home, not five.

**Step 2: Save sources word for word, right away.** When you paste an article, a post, or a document the work depends on, save the original before you do anything else with it. Summaries drift; originals don't.

**Step 3: Write decisions down with the date and the reason.** "October 23: name changed to X, because Y." When a decision gets questioned later, the record answers - not the AI's recollection.

**Step 4: Keep a running list of what's next.** The backlog lives in the record, not in the conversation. It's what the next session - or an overnight run - works from.

**Step 5: Start every session by reading the record, and end it by updating it.** Open with "read the handoff note first." Close with "update the record with what we decided and what's next." Check the record when the AI's account of the past doesn't match yours - and trust the record.

---

## Notes (planned)
- **This library is built this way:** sources/ exists "because context compression in long AI sessions loses pasted text"; records/ holds a handoff record per pattern, the overnight summaries and the red teams; BACKLOG.md carries every decision with a date; a handoff note opens each session.
- **The October 15 story and the stale handoff note (Greg, October 27, 2026):** both now told in the Problem, as a self-deprecating beat. The handoff note was then brought up to date (October 27-28).
- **Start-here placement:** after 05 (the interview fills the backlog) and before 15 (the night shift works from the record). Without this pattern, 15 starts cold every night.
- **Overlap to resolve:** Pattern 04, The AI Operations Manager, already says "Chat sessions don't remember on their own, so give the standing context a home" for a coordination role. When 25 publishes, link 04's line here; 25 is the general rule, 04 one use of it.
- **Distinct from:** Pattern 02, Onboard, Don't Program (builds context at the start - this says where it lives afterward); Pattern 12, Ghost in the Workflow (a record for an AI asset so it outlives its builder - this is the record for the work itself); Pattern 15 (keeping the record is one of its steps).
- **Connections:** Pattern 19, Research Partner, Not All-Knowing Oracle (saved originals make checking possible); Pattern 20, Iterate to the Destination (the destination's versions live in the record).

## Use this pattern (first pass)
*Paste this into any AI system's custom instructions or at the start of a conversation to run Pattern 25.*

```
# The Chat Is Not Your Memory

You are running Pattern 25: The Chat Is Not Your Memory from AI Success Patterns (aisuccesspatterns.com/patterns/25-the-chat-is-not-your-memory.html).

The pattern's premise: long AI work loses its memory. Conversations get compressed, restarted, or moved to a new tool, and the AI fills the gaps confidently and wrong. Keep anything that has to survive somewhere outside the chat, and start every session by reading it.

## Phase 1 - Find the record
Ask the user, in one question, where this work's record lives (a folder, a shared document, a project space, a repository). If there isn't one, help them pick one home and create a short handoff note with four headings: Sources, Decisions, Next, and Notes for the next session.

## Phase 2 - Read before working
If a record exists and you can read it, read it first and summarize it back in three lines: what the work is, the latest decisions, and what's next. If you can't read it, ask the user to paste the handoff note. Don't rely on your memory of earlier sessions.

## Phase 3 - Keep it as you go
During the session:
- When the user pastes a source the work depends on, remind them to save the original word for word in the record before you use it.
- When a decision is made, write it as one line with the date and the reason, ready to add to the record.
- If your recollection of an earlier decision or source differs from the record, say so and go with the record.

## Phase 4 - Update before ending
When the user wraps up, produce the update for the record: new sources to save, decisions made (dated, with reasons), and the next items. Keep it short enough to paste.

## Behavior rules
- One question at a time
- The record wins over your memory - always
- Never reconstruct a source from memory; ask for the original
- End every working session with the record update
```

---

## Sources
- The library's own practice: sources/README.md, records/, BACKLOG.md, the project handoff note.
- No external sources yet. Possible: vendor documentation on context windows and conversation summarization (to support "older parts are summarized or dropped") - verify at the vendor's own pages before use.

## Questions for Greg - answered October 27, 2026
1. Level: Practice.
2. October 15 story: tell it - now in the Problem.
3. Stale handoff note: use it as a self-deprecating beat, then fix it - both done.
4. Name GitHub as one option - done (Step 1).
5. Red team approved - ran overnight October 27-28.

## Original questions
1. **Level.** Foundation (proposed - it's Start-here step 2) or Practice?
2. **The October 15 story.** Tell it on the page (the handoff note that misstated what was published, the lost red team, the nearly lost backlog)?
3. **The stale handoff note.** Use it as a self-deprecating beat, or just fix the note?
4. **Name tools?** Mention GitHub by name as one option (it's how the library does it), or keep the page tool-neutral?
5. **Red team.** Proposed team: **Rachel Stone (adversarial)** - IT architect who says the vendors' memory features already solve this and the pattern is busywork; **Omar Haddad** - consultant juggling five client projects in AI chats; **Linda Park** - operations analyst who has never used GitHub and won't; **Victor Lang** - team lead who inherits a colleague's AI work when they leave. Approve or swap?
