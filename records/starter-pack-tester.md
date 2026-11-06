# Starter pack tester - context document and test prompt

Built November 6, 2026 with Onboard, Don't Program (Greg's answers, played back and confirmed). **Internal.**

## Context document
1. **Who:** Greg Stellflue. He installs each pack himself, as a website visitor would, then hands off to the tester.
2. **The work:** test the six PMO starter pack skills in Claude, ChatGPT and Gemini, after they're installed.
3. **Constraints:** made-up data only. The six skills in order, pmo-start-here first. No time limit.
4. **Preferences:** Greg pastes one prompt to start, then answers nothing. The tool plays the PMO lead itself. Results: one line per skill, PASS or FAIL with the reason.
5. **What good looks like (a pass):** the installed skill starts when asked, follows its phases, asks one question at a time, and produces the promised output, with no em dashes and no pattern numbers.

## The prompts - one per tool (paste into a new chat after installing the pack)

Records go to a safe place, never the live site: Claude and ChatGPT write to the **pack-tests** branch on GitHub (main is never touched); Gemini writes to a **PMO Pack Tests/Gemini** folder in Google Drive.

### Claude
```
You are testing the PMO / EPMO Lead Starter Pack from AI Success Patterns. Six skills are installed in Claude. Test them one at a time, in this order:

1. pmo-start-here
2. the-chat-is-not-your-memory
3. avoid-ai-slop-with-an-llm-interview
4. assemble-the-team
5. the-night-shift
6. ghost-in-the-workflow

You play two parts, and keep them apart:
- THE SKILL: run the installed skill exactly as its instructions say. Use the installed skill, not your own idea of it. If you can't find or load it, stop that test and mark it FAIL.
- THE PMO LEAD: answer the skill's questions as Dana Kerr, PMO lead at Northfield Components, a made-up 900-person industrial parts maker. Dana runs 14 projects; the one in focus is "ERP Phase 2", a made-up rollout that is three weeks behind with an October steering committee coming up. Everything about Dana, Northfield and the projects is made up. Answer in a sentence or two, the way a busy PMO lead would.

Do not stop or wait for me at any point. Play both parts through all six skills in one response, then give the six result lines. Label every turn: "SKILL:" or "DANA:". Run only the skill whose turn it is. If a skill suggests another skill, Dana says "not now" and the test moves on in order - never run a later skill early, and never skip one. Run each skill until it produces its promised output, then move to the next. Carry what earlier skills produced into later ones, as Dana would.

After all six, grade each skill honestly. Don't go easy on it because you played both parts. A skill PASSES only if all of these are true:
- It was the installed skill, it started when asked, and it ran in its turn - a skill run early or skipped is FAIL
- It followed its phases in order
- It asked one question at a time
- It produced the output it promises
- No em dashes (the long dash), and no pattern numbers, in anything the skill wrote - search your own output for the long dash before grading

Finish with exactly six lines, nothing after them:
1. pmo-start-here - PASS or FAIL - reason
2. the-chat-is-not-your-memory - PASS or FAIL - reason
3. avoid-ai-slop-with-an-llm-interview - PASS or FAIL - reason
4. assemble-the-team - PASS or FAIL - reason
5. the-night-shift - PASS or FAIL - reason
6. ghost-in-the-workflow - PASS or FAIL - reason

Two skills must write a real record, not just show it in the chat:
- the-chat-is-not-your-memory: write the ERP Phase 2 project record to GitHub repository level5consulting/ai-success-patterns, branch pack-tests, folder tests/claude/project-record.md
- ghost-in-the-workflow: write the AI asset record to GitHub repository level5consulting/ai-success-patterns, branch pack-tests, folder tests/claude/ai-asset-record.md
Use the GitHub connection. Write only to that branch and folder - never to main.
If you cannot write the file, say exactly what stopped you, and that skill is FAIL - reason: could not write the record. Never claim a file was written unless the write succeeded; give its link if you have one.

Start now with skill 1.
```

### ChatGPT
```
You are testing the PMO / EPMO Lead Starter Pack from AI Success Patterns. Six skills are installed in ChatGPT. Test them one at a time, in this order:

1. pmo-start-here
2. the-chat-is-not-your-memory
3. avoid-ai-slop-with-an-llm-interview
4. assemble-the-team
5. the-night-shift
6. ghost-in-the-workflow

You play two parts, and keep them apart:
- THE SKILL: run the installed skill exactly as its instructions say. Use the installed skill, not your own idea of it. If you can't find or load it, stop that test and mark it FAIL.
- THE PMO LEAD: answer the skill's questions as Dana Kerr, PMO lead at Northfield Components, a made-up 900-person industrial parts maker. Dana runs 14 projects; the one in focus is "ERP Phase 2", a made-up rollout that is three weeks behind with an October steering committee coming up. Everything about Dana, Northfield and the projects is made up. Answer in a sentence or two, the way a busy PMO lead would.

Do not stop or wait for me at any point. Play both parts through all six skills in one response, then give the six result lines. Label every turn: "SKILL:" or "DANA:". Run only the skill whose turn it is. If a skill suggests another skill, Dana says "not now" and the test moves on in order - never run a later skill early, and never skip one. Run each skill until it produces its promised output, then move to the next. Carry what earlier skills produced into later ones, as Dana would.

After all six, grade each skill honestly. Don't go easy on it because you played both parts. A skill PASSES only if all of these are true:
- It was the installed skill, it started when asked, and it ran in its turn - a skill run early or skipped is FAIL
- It followed its phases in order
- It asked one question at a time
- It produced the output it promises
- No em dashes (the long dash), and no pattern numbers, in anything the skill wrote - search your own output for the long dash before grading

Finish with exactly six lines, nothing after them:
1. pmo-start-here - PASS or FAIL - reason
2. the-chat-is-not-your-memory - PASS or FAIL - reason
3. avoid-ai-slop-with-an-llm-interview - PASS or FAIL - reason
4. assemble-the-team - PASS or FAIL - reason
5. the-night-shift - PASS or FAIL - reason
6. ghost-in-the-workflow - PASS or FAIL - reason

Two skills must write a real record, not just show it in the chat:
- the-chat-is-not-your-memory: write the ERP Phase 2 project record to GitHub repository level5consulting/ai-success-patterns, branch pack-tests, folder tests/chatgpt/project-record.md
- ghost-in-the-workflow: write the AI asset record to GitHub repository level5consulting/ai-success-patterns, branch pack-tests, folder tests/chatgpt/ai-asset-record.md
Use the GitHub connection. Write only to that branch and folder - never to main.
If you cannot write the file, say exactly what stopped you, and that skill is FAIL - reason: could not write the record. Never claim a file was written unless the write succeeded; give its link if you have one.

Start now with skill 1.
```

### Gemini
```
You are testing the PMO / EPMO Lead Starter Pack from AI Success Patterns. Six skills are installed in Gemini. Test them one at a time, in this order:

1. pmo-start-here
2. the-chat-is-not-your-memory
3. avoid-ai-slop-with-an-llm-interview
4. assemble-the-team
5. the-night-shift
6. ghost-in-the-workflow

You play two parts, and keep them apart:
- THE SKILL: run the installed skill exactly as its instructions say. Use the installed skill, not your own idea of it. If you can't find or load it, stop that test and mark it FAIL.
- THE PMO LEAD: answer the skill's questions as Dana Kerr, PMO lead at Northfield Components, a made-up 900-person industrial parts maker. Dana runs 14 projects; the one in focus is "ERP Phase 2", a made-up rollout that is three weeks behind with an October steering committee coming up. Everything about Dana, Northfield and the projects is made up. Answer in a sentence or two, the way a busy PMO lead would.

Do not stop or wait for me at any point. Play both parts through all six skills in one response, then give the six result lines. Label every turn: "SKILL:" or "DANA:". Run only the skill whose turn it is. If a skill suggests another skill, Dana says "not now" and the test moves on in order - never run a later skill early, and never skip one. Run each skill until it produces its promised output, then move to the next. Carry what earlier skills produced into later ones, as Dana would.

After all six, grade each skill honestly. Don't go easy on it because you played both parts. A skill PASSES only if all of these are true:
- It was the installed skill, it started when asked, and it ran in its turn - a skill run early or skipped is FAIL
- It followed its phases in order
- It asked one question at a time
- It produced the output it promises
- No em dashes (the long dash), and no pattern numbers, in anything the skill wrote - search your own output for the long dash before grading

Finish with exactly six lines, nothing after them:
1. pmo-start-here - PASS or FAIL - reason
2. the-chat-is-not-your-memory - PASS or FAIL - reason
3. avoid-ai-slop-with-an-llm-interview - PASS or FAIL - reason
4. assemble-the-team - PASS or FAIL - reason
5. the-night-shift - PASS or FAIL - reason
6. ghost-in-the-workflow - PASS or FAIL - reason

Two skills must write a real record, not just show it in the chat:
- the-chat-is-not-your-memory: write the ERP Phase 2 project record to Google Drive folder "PMO Pack Tests/Gemini", as a Google Doc named project-record
- ghost-in-the-workflow: write the AI asset record to Google Drive folder "PMO Pack Tests/Gemini", as a Google Doc named ai-asset-record
Create them as Google Docs in that Drive folder (make the folder if it doesn't exist). The Doc names are project-record and ai-asset-record.
If you cannot write the file, say exactly what stopped you, and that skill is FAIL - reason: could not write the record. Never claim a file was written unless the write succeeded; give its link if you have one.

Start now with skill 1.
```

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
