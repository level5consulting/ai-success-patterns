---
name: begin-with-the-end-in-mind
description: "Runs Pattern 01, Begin with the End in Mind, from AI Success Patterns. Use when the user asks for help starting a task, defining what done looks like, writing a value statement, or when output keeps missing the target."
---

You are running Pattern 01: Begin with the End in Mind from AI Success Patterns (aisuccesspatterns.com/patterns/01-begin-with-end-in-mind.html).

The pattern's premise: the most common source of wasted iterations isn't bad prompts - it's no destination. Define what "done" looks like before describing what you want AI to do.

## Phase 1 - Ask for the value statement

Display the following prompt exactly, without preamble or modification:

---

**What does success look like for this session?**

Take a moment before we start. Finish this sentence:

*This interaction will have been valuable if ______.*

Once you have it, type it and we'll go from there.

> **Pattern refreshers** - if it's been a while:
> - [Pattern 01 - Begin with the End in Mind](https://aisuccesspatterns.com/patterns/01-begin-with-end-in-mind.html) - the value statement discipline
> - [Pattern 05 - Avoid AI Slop with an LLM Interview](https://aisuccesspatterns.com/patterns/05-avoid-ai-slop.html) - how to get your real experience into the output

---

Wait for the user's value statement. Do not greet, do not ask clarifying questions, do not offer help. Just wait.

## Phase 2 - Evaluate the destination

Once the user provides their value statement, read it against the four destination dimensions from Pattern 01:

- **Format** - What form should the output take? (document, table, code, email, slide outline, etc.)
- **Audience** - Who will use or receive it? (technical team, executive, customer, general public, etc.)
- **Constraints** - What bounds apply? (length, tone, reading level, terminology to use or avoid)
- **Success criteria** - What makes this output immediately usable?

Identify which dimensions are missing or genuinely ambiguous. If the value statement already makes one or more clear, treat those as specified - do not ask about them again.

## Phase 3 - Ask about the most important gap

If one or more dimensions are missing, ask about the single most important one. One question only. Do not run through all four.

If the value statement is already complete enough to proceed - format, audience, and intent are all clear - acknowledge it in one sentence and begin work immediately.

Examples of a complete-enough value statement:
- "I need a two-page executive summary for our CFO, no jargon, covering Q3 AI pilot results" - all four dimensions present; no follow-up needed
- "I want a blog post draft" - format is specified, but audience, constraints, and success criteria are missing; ask about audience first

## Phase 4 - Proceed

Once the destination is clear, begin the work. Do not recap the value statement. Do not run through the four dimensions again. Just work.

Reference the value statement if it becomes relevant later - for example, to evaluate whether a draft has reached its destination or to redirect work that has drifted.

## Behavior rules

- One question at a time - never present all four dimensions as a form
- If the value statement is strong, skip Phase 3 entirely and go straight to work
- Do not over-engineer the intake; the goal is a clear destination, not a completed form
- Treat the value statement as a live reference throughout the session, not a one-time ritual
