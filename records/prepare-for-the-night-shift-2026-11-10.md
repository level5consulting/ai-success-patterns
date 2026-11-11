# Prepare for the Night Shift - proposed text (November 10, 2026)

Greg's idea (Nov 5): the afternoon step before an unattended run. Go through tonight's plan, find every step that would need a person, and do those together before the run starts, so the night runs with no one stepping in. Anything missed still runs, moved to the end of the night; the morning review catches it, and the miss teaches the next afternoon's check.

Nothing below is applied yet. Pages to change on publish: patterns/15-the-night-shift.html (Solution steps and the "Use this pattern" prompt), patterns/15-the-night-shift.md if it mirrors the page, and the four identical copies of the PMO skill:
- starter-packs/pmo-epmo-lead/claude/skills/the-night-shift/SKILL.md
- starter-packs/pmo-epmo-lead/chatgpt/skills/the-night-shift/SKILL.md
- starter-packs/pmo-epmo-lead/gemini/skills/the-night-shift/SKILL.md
- starter-packs/pmo-epmo-lead/chatgpt/plugin/home/.codex/plugins/ai-success-patterns-pmo/skills/the-night-shift/SKILL.md
(then rebuild the the-night-shift zips).

## (a) New Solution step for the pattern page

**Where:** right after "Track every run, and preview tonight's before it starts" and before "Split the work by judgment." The preview is when you see tonight's plan; this step is what you do with it. The steps after it move down one number.

**Step title:** Prepare for the Night Shift - do the people parts before you leave.

**Step text:**

With tonight's preview in front of you, go through the plan and find every step that would stop and wait for a person: an approval, a login, a site or tool the AI hasn't been allowed to use yet, a decision only you can make. Do those together in the afternoon, before the run starts, so the night runs with no one stepping in. A run that stops at 11 PM to ask a question sits idle until morning. If one gets missed, the night doesn't stop: that item moves to the end of the run and keeps going as far as it can, and the morning review shows what it was waiting on. Then add it to the list of things the afternoon check looks for, so the same miss doesn't happen twice.

**Example (optional, for the Notes section or under the step):** Greg's setup runs this every day. A short preview email arrives at 3:47 PM listing tonight's runs and a "do together at 4 PM" list - the approvals, logins and new sites the night will need. He and the AI clear that list at 4 PM, and the run starts with nothing left to ask.

## (b) Lines for the "Use this pattern" prompt

Add as a new phase between "Phase 4b - Build the morning review" and "Phase 5 - Check for scheduling":

```
## Phase 4c - Prepare for the Night Shift
Before the run starts, go through tonight's plan with the user and list every step that would need a person - an approval, a login, a new website or tool, a decision - and do those together now, so the night runs with no one stepping in. Anything still missed moves to the end of the run and shows up in the morning summary as "waiting on you," and gets added to the next afternoon's check.
```

Add to "Behavior rules":

```
- Clear every step that needs a person before the run starts, never in the middle of the night
```

## (c) Lines for the PMO SKILL.md

Add the same "Phase 4c - Prepare for the Night Shift" block and the same behavior rule as in (b), in the same places. Then add this line to the end of the "For PMO and EPMO leads" section:

```
Before tonight's run, clear the people parts together: the PPM tool or SharePoint login, a sponsor's approval to use a report, the decision on which projects the health check covers.
```
