# Research for Pattern 02 - Onboard, Don't Program (overnight, October 18-19, 2026)

Proposed only. Nothing applied to the page.

## 1. Anthropic's own prompting guidance - VERIFIED at source
- **Source:** Anthropic, "Be clear and direct" (Claude prompt engineering docs) - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct
- **Says (quoted from the page):** "Think of Claude as a brilliant but new employee who lacks context on your norms and workflows. The more precisely you explain what you want, the better the result."
- **Also:** "Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude better understand your goals and deliver more targeted responses."
- **Fit:** The model vendor uses the pattern's own metaphor - the AI as a new employee who needs onboarding. Supports context *before* commands, and context *with* instructions (the red-team change 1 framing).
- **Convention note:** a company's documentation, like the OpenAI statement on 08 - a short quote may be acceptable; otherwise paraphrase.

## 2. Confirm understanding - VERIFIED (preprint)
- **Source:** Michael J.Q. Zhang and Eunsol Choi (University of Texas at Austin), "Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs," arXiv:2311.09469, November 2023 - https://arxiv.org/abs/2311.09469
- **Finding:** Resolving ambiguity through clarifying questions and answers generally improved model answers on ambiguous tasks; fewer than half of examples needed clarification, so asking selectively matters.
- **Fit:** Supports the "confirm understanding" step - a restated brief surfaces the ambiguity before the work starts. Caveat: a preprint, and it studies the model asking questions, not restating a brief. Use as supporting, not proof.

## Proposed edits for Greg
1. Notes: "Even the AI vendors describe it this way: Anthropic's guidance tells users to treat the model as a brilliant but new employee who lacks context on your norms and workflows." (Paraphrase or short quote - Greg's call.)
2. Solution, after "Confirm understanding": "Research on ambiguous requests found that resolving the ambiguity first generally improves the answer (Zhang and Choi, 2023)."
