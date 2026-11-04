# Proposal - Rebuild the Night Shift Tracker with Pattern 04 (overnight, October 27-28, 2026)

Proposal only - nothing changed. Greg, October 27, 2026: "Our nightshift tracker is the start of the AI operations manager. It might be a good exercise to rebuild it using this pattern."

Current tracker: https://claude.ai/artifact/MjuCxQgA7Uwa6uvueWtUPY - a list of runs (night, time, workstream, item, status, output, needs decision, notes), fed by uploading night-runs.json. It shows the last two nights of Done.

## What's missing today
- **No list of agents.** Runs are one-off rows. There's no record of which standing jobs exist (nightly run, 4 PM preview, certification reminder, webinar rhythm, publish days, skills pack), who owns them, or when they run.
- **Adding a job is manual.** A new kind of run only shows up when someone writes a row.
- **Results live in three places.** The tracker, the Morning Review form, and the overnight summary on GitHub. Each run reports to some of them.
- **Updates are a file upload.** Every change means re-uploading night-runs.json.

## The rebuild

### 1. Agent registry (new, top of the page)
One row per standing agent:

| Field | Example |
|---|---|
| Agent | Nightly run |
| What it does | Red teams, drafts, Use this pattern, cert prep |
| Schedule | Sun-Thu, 11:30 PM CT |
| Inputs | Week plan, Morning Review answers, BACKLOG |
| Reports to | This dashboard + Morning Review form |
| Owner | Greg (decisions); Claude (runs) |
| Status | Active / Paused |

Starting agents: Nightly run; 4 PM preview email; Morning certification reminder; Webinar draft (Wed); Webinar red team (Thu); Webinar finish (Sun); Publish day; Skills pack (one-off).

### 2. Run log (today's list, same fields for every agent)
Agent, when it ran, status (scheduled / done / failed / needs a decision), what it produced (link), decision needed (link to the form item). Every agent writes the same row - that's the rule that lets new agents plug in.

### 3. Today panel
Tonight's scheduled runs, open decisions in the Morning Review form (count and links), and anything that failed.

### 4. Adding an agent
Write one registry row (Step 1's fields). From then on it reports to the run log like every other agent. No new page, no new tracker.

## How it would be built
- Keep the existing artifact and link (it's pinned).
- Move the data from an uploaded file to the artifact's own database: two collections, `agents` and `runs`, so each run writes its own row instead of re-uploading a file.
- Each scheduled task's instructions get one added line: "write your run row to the Night Shift Tracker."
- The 4 PM email reads the same data, so the email and the page always match.

## Why it's a good worked example
It's Pattern 04 running for real: a standing coordination role, one dashboard, a registry that new agents join. It also shows Pattern 25 (the record lives outside the chat) and Pattern 15 (overnight work reports in the morning). It could become the Notes example on Pattern 04's page.

## Questions for Greg
1. Rebuild the tracker this way?
2. Keep the Morning Review form separate (decisions) and the tracker for runs - or merge them into one page?
3. Build it Thursday night, or put it in next week's plan?
