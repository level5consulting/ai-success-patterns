# Night Shift Tracker rebuild - proposal (November 3, 2026)

Proposal only. Nothing has changed on the live tracker. Every current feature stays, and the Morning Review form stays separate. Built on The AI Operations Manager: one place that shows what the agents are doing, whether they did it, and what they need from you. Each change is its own question in the form.

## What's there today (all kept)
- Coming up: scheduled runs, soonest first, with your next step.
- Done: the last two nights, with where the work is and the decision needed.
- Standing rhythms.
- The headline count of runs tonight and coming up.
- Rows kept in ops/data/night-runs.json, updated by each run.

## What I found looking at it
- **It can't show a run that went wrong.** The page only knows Scheduled, Done and Rhythm. Monday's run stalled on an approval at 11:40 PM and the tracker could only say Done, with a note in a column the page doesn't display.
- **A missed run sits in "Coming up" forever.** "Session 2 finish" (November 1) was still listed as coming up tonight, two days after Session 2 went live. I marked it Done in the data.
- **"Where it is" is plain text.** You can't click through, which doesn't meet the Plans in Motion link standard.
- **The rhythms are out of date.** The list has 4 PM preview, nightly run and session rhythm, but not the morning learning email - and the times are approximate (the nightly run actually starts at 11:21 PM CT, the preview at 3:47 PM, the learning email at 7:21 AM).

## Proposed changes
1. **Last night, at the top.** One line: did it run, did it finish, where did it stop, how many form items it left you. Answers "do I need to worry about last night?" (the tracker's own question, in the spirit of Dashboards That Answer a Question).
2. **New statuses: Stopped and Missed.** Stopped is a run that didn't finish, shown with where it stopped. Missed is worked out by the page: a Scheduled row whose night has passed moves out of Coming up and gets flagged.
3. **Click through.** Add a link to each row, following the Plans in Motion standard, so "Where it is" opens the thing.
4. **Agent registry.** Turn Standing rhythms into a registry of each scheduled task: what it does, when it really runs, what it may do (for example, sends email or never sends email), last run and result. Kept current from the scheduled task list at each nightly run.
5. **Older runs stay findable.** Done still shows the last two nights by default, with a "show all" control for the rest of the history.
6. **Show the notes.** Add the existing notes field to Done on wide screens, so "stalled on approval" is visible.

## Not proposed
- Merging the form into the tracker - you asked to keep it separate.
- Removing anything above.

If approved, the Wednesday or Thursday run builds what you accept on the live tracker and tells you what changed.
