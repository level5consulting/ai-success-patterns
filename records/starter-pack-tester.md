# Starter pack tester - context document and test prompt

Built November 6, 2026 with Onboard, Don't Program (Greg's answers, played back and confirmed). **Internal.**

## Context document
1. **Who:** Greg Stellflue. He installs each pack himself, as a website visitor would, then hands off to the tester.
2. **The work:** test the six PMO starter pack skills in Claude, ChatGPT and Gemini, after they're installed.
3. **Constraints:** made-up data only. The six skills in order, pmo-start-here first. No time limit.
4. **Preferences:** Greg pastes one prompt to start, then answers nothing. The tool plays the PMO lead itself. Results: one line per skill, PASS or FAIL with the reason.
5. **What good looks like (a pass):** the installed skill starts when asked, follows its phases, asks one question at a time, and produces the promised output, with no em dashes and no pattern numbers.

## The prompt (paste into a new chat in each tool)

```
You are testing the PMO / EPMO Lead Starter Pack from AI Success Patterns. Six skills are installed in this tool. Test them one at a time, in this order:

1. pmo-start-here
2. the-chat-is-not-your-memory
3. avoid-ai-slop-with-an-llm-interview
4. assemble-the-team
5. the-night-shift
6. ghost-in-the-workflow

You play two parts, and keep them apart:
- THE SKILL: run the installed skill exactly as its instructions say. Use the installed skill, not your own idea of it. If you can't find or load it, stop that test and mark it FAIL.
- THE PMO LEAD: answer the skill's questions as Dana Kerr, PMO lead at Northfield Components, a made-up 900-person industrial parts maker. Dana runs 14 projects; the one in focus is "ERP Phase 2", a made-up rollout that is three weeks behind with an October steering committee coming up. Everything about Dana, Northfield and the projects is made up. Answer in a sentence or two, the way a busy PMO lead would.

Do not stop or wait for me at any point. Play both parts through all six skills in one response, then give the six result lines. Label every turn: "SKILL:" or "DANA:". Run each skill until it produces its promised output, then move to the next. Carry what earlier skills produced into later ones, as Dana would.

After all six, grade each skill honestly. Don't go easy on it because you played both parts. A skill PASSES only if all of these are true:
- It was the installed skill, and it started when asked
- It followed its phases in order
- It asked one question at a time
- It produced the output it promises
- No em dashes, and no pattern numbers, in anything the skill wrote

Finish with exactly six lines, nothing after them:
1. pmo-start-here - PASS or FAIL - reason
2. the-chat-is-not-your-memory - PASS or FAIL - reason
3. avoid-ai-slop-with-an-llm-interview - PASS or FAIL - reason
4. assemble-the-team - PASS or FAIL - reason
5. the-night-shift - PASS or FAIL - reason
6. ghost-in-the-workflow - PASS or FAIL - reason

Start now with skill 1.
```

## How to use it
Install the pack in the tool, start a new chat, paste the prompt. Send Greg's six lines back to the AI Success Patterns chat, with the tool name, for the record.
