# Begin with the End in Mind

**Category:** Conversational  
**Status:** Published

---

## Name
Begin with the End in Mind

## Context
Any AI-assisted task that produces a deliverable: a document, analysis, code, plan, recommendation, or decision. Applies at the start of a conversation, prompt sequence, or agentic workflow.

## Problem
Most AI interactions start with a task description but no definition of done. The model produces output — often impressive output — that doesn't fit the actual destination: wrong format, wrong audience, wrong level of detail. The user iterates. Tokens accumulate. Quality drifts. Time is lost. The model wasn't wrong; it was just never told what "right" looks like.

## Solution
Before describing what you want the AI to do, describe what you want to receive. Specify:
- **Format**: Document, table, bullet list, code, slide outline, email
- **Audience**: Technical team, executive sponsor, customer, general public
- **Constraints**: Length, tone, reading level, terminology to use or avoid
- **Success criteria**: What would make this output immediately usable

Then give the task. The model aligns its generation to the destination, not just the request.

Example opening: *"I need a two-page executive summary, written for a CFO with no technical background, using plain language, no acronyms, and concluding with three specific cost implications. Then: summarize our Q3 AI pilot results..."*

## Value Consequence
Output arrives at a usable state in fewer iterations. Format mismatches, audience misreads, and length issues — the most common revision causes — disappear before they occur. Downstream steps (review, approval, publishing) move faster because the first draft is already shaped for its destination.

---

## Notes
This pattern is the parent meta-pattern for several child patterns, including *Avoid AI Slop with an LLM Interview* (Pattern 5). Any technique that helps specify the desired output before prompting is an instance of this pattern.

## Related Patterns
- [Avoid AI Slop with an LLM Interview](05-avoid-ai-slop-llm-interview.md) (child pattern)
- [Onboard, Don't Program](02-onboard-dont-program.md)
