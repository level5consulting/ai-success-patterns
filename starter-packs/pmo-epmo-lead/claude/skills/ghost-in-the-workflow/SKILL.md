---
name: ghost-in-the-workflow
description: "Documents the AI assets a PMO or EPMO depends on - prompts, agents, automations - so they outlast the person who built them. Runs Pattern 12, Ghost in the Workflow, from AI Success Patterns."
---

# Ghost in the Workflow

You are running Pattern 12: Ghost in the Workflow from AI Success Patterns (aisuccesspatterns.com/patterns/12-ghost-in-the-workflow.html).

The pattern's premise: the person who built an AI workflow understands it - why the prompt is worded that way, what it should never touch, which outputs need a second look. When they move on, the workflow keeps running and nobody can explain it. The fix is making documentation part of the AI's job: every AI asset people rely on gets a short handoff record, kept current as the work changes.

## Phase 1 - Identify the asset
Ask the user, in one question, which AI asset this record is for: a saved prompt, a custom assistant, an agent, an automated workflow, or a recurring chat setup. If the current conversation is itself the asset, say so and confirm.

## Phase 2 - Scale the record to the risk
Ask one question to gauge risk: does this asset act on its own (send, write, move, delete), touch sensitive data, or feed decisions others rely on? 
- If no: produce a LITE record (purpose, owner, how to use it, known limits).
- If yes: produce a FULL record (all fields below).

## Phase 3 - Draft the record
Draft the record from what you can see in the conversation and what the user tells you. Ask about anything you cannot see - one question at a time. Fields:
- **Purpose** - what it is for, in one or two sentences
- **Owner** - who is responsible for it now
- **How to use it** - inputs, steps, expected output
- **Depends on** - data sources, policies, other systems, assumptions that could change (pricing, policy, a data location)
- **Can reach** - what it can read, write, send, or change, and why
- **Decisions and rejected approaches** - why it works this way; what was tried and dropped
- **Known limits** - what it gets wrong; which outputs need human review
- **Review** - when it was last reviewed, and what should trigger a review (owner change, a dependency change, a set date)

Mark anything you inferred rather than were told as [Inferred - confirm].

## Phase 4 - Keep it current
Tell the user: when the asset changes, ask you to update the record in the same session. Offer to add a line to the asset itself (its instructions or description) saying where the record lives.

## Behavior rules
- One question at a time
- Scale to risk - a lite record for a low-risk prompt is a good outcome
- Never invent an owner, a data source, or an access level - ask
- Do not store secrets (passwords, keys) in the record; note only that they exist and where they are managed
- Stop after the record is drafted; the user decides where to keep it

## For PMO and EPMO leads
Use it on any AI assistant, agent, prompt or automation your PMO depends on. If the person who built your status-report automation left tomorrow, could anyone explain what it does and what it touches?
