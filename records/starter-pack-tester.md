# Starter pack tester - context document and test prompt

Built November 6, 2026 with Onboard, Don't Program (Greg's answers, played back and confirmed). **Internal.**

## Context document
1. **Who:** Greg Stellflue. He installs each pack himself, as a website visitor would, then hands off to the tester.
2. **The work:** test the six PMO starter pack skills in Claude, ChatGPT and Gemini, after they're installed.
3. **Constraints:** made-up data only. The six skills in order, pmo-start-here first. No time limit.
4. **Preferences:** Greg pastes one prompt to start, then answers nothing. The tool plays the PMO lead itself. Results: one line per skill, PASS or FAIL with the reason.
5. **What good looks like (a pass):** the installed skill starts when asked, follows its phases, asks one question at a time, and produces the promised output, with no em dashes and no pattern numbers.

## The test scripts (Greg's version, Nov 6 - replaces the earlier prompts)
One per tool, in records/starter-pack-tests/: test-script-claude.md, test-script-chatgpt.md (GitHub, level5consulting/patterns-test, tests/<tool>/) and test-script-gemini.md (Google Drive, PMO Pack Tests/Gemini). Same test; only the write target differs. Greg rewrote it because the first prompt conflicted with itself: "Dana says not now" fought pmo-start-here's job of recommending the next skill. His version separates recommending from running and adds BLOCKED BY TEST ORDER.

## How to use it
Install the pack in the tool, start a new chat, paste the prompt. Send Greg's six lines back to the AI Success Patterns chat, with the tool name, for the record.

## Results log

### Gemini - November 6, 2026 (first run, before the fixes above)
Gemini's own grades: six PASS. Reviewed against the transcript:
1. pmo-start-here - FAIL - it ran the Avoid AI Slop interview itself instead of handing off, so skill 3 ran out of turn.
2. the-chat-is-not-your-memory - PASS - read the record, logged the decision, ended with an agenda.
3. avoid-ai-slop-with-an-llm-interview - FAIL - ran early inside skill 1, then "skipped" in its turn; two em dashes in its output.
4. assemble-the-team - PASS, with notes - four distinct voices and one-by-one decisions; the adversarial voice challenged details, not the premise; the final list was labeled DANA.
5. the-night-shift - PASS - split, limits, brief, and said honestly it can't schedule.
6. ghost-in-the-workflow - PASS - one question at a time, full record scaled to risk.
Lesson: the tool grading itself went easy - it missed its own em dashes and the skipped skill. Greg reviews the transcript, not just the six lines.
Fixes: em-dash rule added to all 18 skills (branch no-copilot-pack); tester prompt now forbids running skills out of turn and makes the grader search for long dashes. Re-run Gemini with the new zip and prompt.

### Gemini - November 6, 2026 (second run, fixed skills and prompt)
PASS on all six, per Greg. Greg: "this will save me an hour of testing for each of these packs."

### Claude - November 6, 2026
Claude's own grades: six PASS. Reviewed: the skills ran well, in order, no em dashes. But the record-writing requirement was ignored - nothing was written to the pack-tests branch (checked) and the transcript never mentions trying. Per the script, the-chat-is-not-your-memory and ghost-in-the-workflow are FAIL - could not write the record. It also added notes after the six lines.
Findings worth fixing: assemble-the-team's example names "Dana, CFO" (clashes with the test persona); pmo-start-here says "five skills" while six install (five patterns plus itself). Scenario: "October steering committee" is already past - update the tester to "December".

### Claude - November 6, 2026 (re-run, patterns-test repo)
PASS on all six, per Greg. Both records written and confirmed: tests/claude/project-record.md and tests/claude/ai-asset-record.md in level5consulting/patterns-test (commit 10:30 AM). Correction: Claude CAN write to GitHub when the repository is connected - the earlier "read-only" assumption was wrong.
