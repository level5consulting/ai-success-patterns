# AI Success Patterns: PMO / EPMO Lead Starter Pack
## Six-Skill End-to-End Test Script

You are testing the six installed skills in the **AI Success Patterns PMO / EPMO Lead Starter Pack**.

Your job is to test whether each installed skill behaves according to its own instructions, produces its promised outputs, and respects the constraints of this test.

**Do not rewrite, improve, or substitute the skills during testing.**

## 1. Skills to test

Test these installed skills in exactly this order:

1. `pmo-start-here`
2. `the-chat-is-not-your-memory`
3. `avoid-ai-slop-with-an-llm-interview`
4. `assemble-the-team`
5. `the-night-shift`
6. `ghost-in-the-workflow`

Load each installed skill's actual instructions before running it.

If a skill cannot be found or loaded, mark it FAIL and continue to the next skill.

Never invent missing skill instructions.

## 2. Your two roles

Play both roles throughout the test.

**SKILL:** Execute the currently selected installed skill exactly as written. Follow its phases, questions, behavioral rules, and output requirements.

**DANA:** Respond as Dana Kerr, PMO lead at Northfield Components, a fictional 900-person industrial parts manufacturer.

Dana manages 14 projects. The focus project is ERP Phase 2, a fictional rollout that is three weeks behind schedule, with a December steering committee approaching.

Dana's answers should be realistic, concise, and consistent. Usually one or two sentences.

All people, organizations, projects, and business information in the scenario are fictional.

Label every interaction:

- `SKILL:`
- `DANA:`

Do not combine the two roles or let Dana answer questions the skill has not asked.

## 3. Test execution rules

Run all six tests in one continuous response without asking the real user to intervene.

For each skill:

1. Load its installed instructions.
2. Execute its phases in their required order.
3. Ask one question at a time.
4. Have Dana answer that question.
5. Continue until the skill reaches its natural stopping point or produces its promised output.
6. Record the result.
7. Move to the next skill.

Carry forward the fictional project facts, decisions, and outputs from previous tests.

Do not silently skip required phases.

### Special rule: Skill orchestration

Some skills recommend or invoke other skills.

**A recommendation is not the same as an execution.**

If the current skill recommends a later skill, Dana should accept the recommendation as a future action, but that later skill must not execute until its scheduled test.

For example:

- `pmo-start-here` recommends `the-chat-is-not-your-memory`.
- Dana agrees that this is the next workflow to run.
- `pmo-start-here` completes its own guidance, handoff, and any applicable closing instructions.
- The test then proceeds to `the-chat-is-not-your-memory` in the scheduled order.

If a skill explicitly requires another skill to execute before it can complete, record that dependency as **BLOCKED BY TEST ORDER**.

Do not mark the skill FAIL solely because the test sequence prevents that dependency.

Do not pretend the dependent skill was executed.

When the dependent skill runs later, evaluate whether the original dependency was satisfied. Report any remaining incomplete requirement.

### Special rule: pmo-start-here

This is an onboarding and orchestration skill.

Test its ability to:

- Explain the recommended PMO workspace structure.
- Identify Dana's immediate need.
- Recommend the appropriate installed skill.
- Explain why the recommendation fits.
- Provide a usable handoff into that skill.
- Apply its follow-up and documentation guidance when applicable.

Do not require it to execute a later skill out of sequence.

If its own instructions explicitly require completing that later skill, record the dependency and assess it after the later test.

Do not invent a completed outcome for work that has not yet happened.

## 4. Google Drive write requirements

Two skills must create or update actual Google Docs.

Use the connected Google Drive tools.

**Authorized folder:** `PMO Pack Tests/Gemini` (create it if missing)

**Authorized Docs:** `project-record` and `ai-asset-record`

No other folder or file may be modified.

### Project record

During `the-chat-is-not-your-memory`: create or update the Doc `project-record`. It must contain the ERP Phase 2 context, sources, decisions, next actions, and handoff notes required by the installed skill.

### AI asset record

During `ghost-in-the-workflow`: create or update the Doc `ai-asset-record`. It must document the fictional Night Shift workflow using the fields and risk level required by the installed skill.

### Write verification

For both Docs:

1. Check whether the Doc already exists.
2. Create it if missing, or update it if present.
3. Confirm the write succeeded.
4. Read the Doc back when possible to verify the stored content.
5. Include the Doc link in the test output.

If the write fails, report the exact error or permission limitation.

**A record displayed in chat does not count as a successful Drive write.**

A skill that requires a Drive write for this test cannot PASS unless the write succeeds.

## 5. Rules for honest testing

Follow these rules strictly:

- Use the installed skill, never a reconstructed version.
- Follow phases in order.
- Ask only one question at a time.
- Do not skip mandatory questions.
- Do not invent tool results or successful actions.
- Do not silently correct a skill's behavior.
- Do not run another skill early.
- Do not use em dashes in skill-generated text.
- Do not use pattern numbers in skill-generated text.
- Preserve Dana's decisions across tests.
- Keep fictional scenario facts separate from verified tool actions.

If a skill violates a requirement, record the violation even if the final output looks good.

If a skill asks for information Dana has not provided, Dana may supply reasonable fictional information consistent with the scenario.

If the skill requires an external action, use the available tools where authorized. Otherwise, report the limitation rather than simulating success.

## 6. Grading

Evaluate each skill against its installed instructions and the test requirements.

Use three possible outcomes:

**PASS**

The installed skill loaded, executed in its assigned turn, followed its required phases and questioning rules, and produced its promised output. Any required external write succeeded.

**FAIL**

The skill was unavailable, violated a required behavior, skipped a mandatory phase, failed to produce a required output it could have produced, or failed a required Drive write.

**BLOCKED**

The skill could not complete a mandatory dependency because the test's fixed order or an unavailable external capability prevented it. The skill itself did not demonstrate an instruction violation.

Do not use BLOCKED to excuse a skill that ignored its own instructions.

Distinguish between:

- Skill design defects
- Skill execution defects
- Test-script constraints
- Tool or permission failures

For every FAIL or BLOCKED result, identify the exact reason.

Do not award PASS merely because an output looks reasonable.

## 7. Final report

After all six tests, provide:

**A. Test transcript**

Show the labeled SKILL and DANA interactions in sequence.

**B. Output verification**

Identify the promised outputs produced by each skill, including Doc links and confirmed write results.

**C. Test observations**

Identify actual skill defects separately from test-environment limitations.

**D. Final grading**

Finish with exactly six result lines, using this format:

1. pmo-start-here - PASS / FAIL / BLOCKED - reason
2. the-chat-is-not-your-memory - PASS / FAIL / BLOCKED - reason
3. avoid-ai-slop-with-an-llm-interview - PASS / FAIL / BLOCKED - reason
4. assemble-the-team - PASS / FAIL / BLOCKED - reason
5. the-night-shift - PASS / FAIL / BLOCKED - reason
6. ghost-in-the-workflow - PASS / FAIL / BLOCKED - reason

Replace each outcome placeholder with exactly one result.

Before grading, check the transcript for em dashes, pattern numbers in skill-generated text, skipped phases, multiple questions asked at once, and unverified claims of external actions.

Do not add commentary after the six final result lines.

**Begin immediately with the installed `pmo-start-here` skill.**