# Handoff drill edits - Nov 11, 2026 (held for publish)

Source: BACKLOG.md, "Ghost in the Workflow - add a handoff drill test". Idea from Giacomo Balli's reply (Nov 11). Greg's framing: "disaster recovery testing for people attrition." Greg agreed Nov 11 to the split: The AI Operations Manager owns the recurring drill; Ghost in the Workflow gets one line.

Working tree only, branch overnight-2026-11-11. Not committed.

## The AI Operations Manager (patterns/04-ai-operations-manager.html)

**1. Solution - new card in the cadence grid (after "Cross-Project Risk"):**

> **Handoff Drill** - Break one run on purpose; someone who didn't build it fixes it using only the record

**2. Solution - new paragraph right after the cadence grid:**

> **Run a handoff drill.** Think of it as disaster recovery testing for people attrition. On a set schedule, break one run on purpose and hand it to someone who didn't build it - an outside person or your newest hire, since in a small team everyone else had a hand in the build. They figure out what went wrong and get it running again using only the written record (see Ghost in the Workflow). Every question they have to ask the builder marks knowledge that lives only in someone's head. Log each gap, fix the record, and track the gaps until they're closed.

("Ghost in the Workflow" links to 12-ghost-in-the-workflow.html.)

**3. "Use this pattern" prompt - new line under Behavior rules:**

> - Schedule a handoff drill: break one run on purpose and have someone who didn't build it (an outside person or the newest hire) recover it using only the record; log every question they had to ask the builder as a gap, and track it until the record is fixed

**4. Notes - new last line:**

> Handoff drill idea from Giacomo Balli.

## Ghost in the Workflow (patterns/12-ghost-in-the-workflow.html and .md)

**Solution, end of Step 4 ("Test the record with someone who didn't build it"):**

> A record isn't done until it passes a handoff drill: someone who didn't build the workflow fixes a deliberately broken run using only the record. The AI Operations Manager runs these drills and tracks the gaps they find.

("The AI Operations Manager" links to 04-ai-operations-manager.html in both files.)

## Screenshots

records/shots-2026-11-11/ - aom-solution-handoff-drill-desktop.png, aom-solution-handoff-drill-phone.png, aom-notes-desktop.png, ghost-step4-handoff-drill-desktop.png (plus aom-lead, aom-when-to-use and aom-use-this-pattern for the plain-language edits).

## Not changed

- No skill or starter-pack copy of The AI Operations Manager prompt exists in the repo, so only the page prompt has the new line.
- Ghost in the Workflow's own "Use this pattern" prompt is unchanged.
