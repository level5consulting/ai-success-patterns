---
name: test-adversarially
description: "Runs Pattern 03, Test Adversarially, from AI Success Patterns. Use when the user asks for help testing AI output, stress-testing a draft, finding weak spots, or asking what could go wrong."
---

## What this skill does

When invoked, examine the output to be tested - either the most recent AI-generated output in this session, or whatever the user pastes in - and run an adversarial review using the appropriate lenses.

## Step 1 - Identify the output

If the user has pasted output to test, use that. If not, use the most recent substantial AI-generated output in this session. If it is unclear what to test, ask: "What output should I test?"

## Step 2 - Diagnose which lenses apply

Evaluate the output against three failure modes and select the lenses that apply:

**Adversarial Review** - applies when the output contains factual claims, statistics, citations, named sources, dates, or specific assertions that could be wrong, outdated, or fabricated. Almost always applies.

**Context Gap Check** - applies when the output involves organizational specifics, internal data, proprietary processes, or nuance that the model could not have known from the conversation alone. Ask: did the model have to assume things it shouldn't have?

**Critic's Lens** - applies when the output makes recommendations, presents analysis, or argues a position. Ask: what would a skeptical expert say about the reasoning, not just the facts?

## Step 3 - Present the selection and confirm

Present the selected lenses as a short list. For each, give one plain-language sentence explaining why it applies to this specific output. Then ask:

> "Run these? (or tell me which to add, drop, or change)"

Do not run the critique until the user confirms.

## Step 4 - Run the critique

For each confirmed lens, run the following:

**Adversarial Review:** Identify every claim in the output that could be wrong, outdated, or unsupported. List specific weaknesses - not general caveats. Flag fabricated specifics, overconfident assertions, and anything that would require independent verification before use.

**Context Gap Check:** Identify what context, data, or organizational nuance you would have needed to give a more accurate or complete answer. State explicitly what you had to assume because it was not provided.

**Critic's Lens:** What would a skeptical expert say about this analysis? What assumptions does it make that might not hold? What's missing from the reasoning?

## Step 5 - Close with a validation prompt

After the critique, add:

> "Testing surfaces what may be wrong. Validation is what you bring that the model never had - domain expertise, source verification, or data you can check directly. What can you verify independently?"

## Tone

Direct and specific. No hedging, no general caveats. If something looks wrong, say so plainly. The point of this pattern is to surface problems before they leave the user's hands.
