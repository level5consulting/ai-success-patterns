# Test Adversarially

**Category:** Accuracy  
**Status:** Published

---

## Name
Test Adversarially

## Context
Any situation where AI-generated output will be used to inform decisions, shared externally, or relied on by others. Applies to research summaries, code, recommendations, analysis, and any output where errors carry real consequence.

## Problem
AI models are optimized to be helpful and fluent. They produce confident, well-structured output whether or not the underlying claims are accurate. Users who evaluate output by how it reads — coherent, professional, detailed — miss factual errors, logical gaps, and fabricated specifics that hide inside polished prose. Trusting fluency as a proxy for accuracy is the most common and costly AI mistake in professional settings.

## Solution
After generating output you intend to use, prompt the model to attack it:

*"Now act as a skeptical expert reviewer. Identify every claim in what you just wrote that could be wrong, outdated, or unsupported. List specific weaknesses, not general caveats."*

Or:

*"What would a critic say about this analysis? What's missing? What assumptions am I making that might not hold?"*

Then verify the flagged items against primary sources. The model will surface its own failure modes more accurately than it will admit to them in passing.

## Value Consequence
Errors caught before they leave your hands instead of after. Decisions grounded in verified claims instead of fluent-sounding assertions. A professional track record of accurate AI-assisted work that builds trust over time — with your audience and with yourself.

---

## Notes
This pattern pairs naturally with *The Hallucination Audit* (backlog). The difference: adversarial testing is active (you prompt for critique); a hallucination audit is structural (you build verification into the workflow design).

Some practitioners run adversarial testing in a separate AI session to eliminate anchoring — the second model hasn't "committed" to the first model's output.

## Related Patterns
- [Begin with the End in Mind](01-begin-with-end-in-mind.md)
- Red-Teaming Your Own Prompts (backlog)
- The Hallucination Audit (backlog)
