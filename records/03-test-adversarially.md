# Record: Pattern 03 - Test Adversarially

**Category:** Accuracy  
**Maturity level:** Foundation  
**Status:** Published  
**Page:** `patterns/03-test-adversarially.html`

## Purpose
Names the failure of trusting fluent AI output. Value: prompt the AI to attack its own output before use, and recognize that trusting an output and knowing it is valid are different - validation is what the human brings.

## Idea providers
- Greg Stellflue - author.
- **Justin J MacBale** - Pattern contributor. Contributed two insights: AI output can fail from missing context, data, or nuance (not just hallucination); and trust vs. validity. Credit is live on the page. **Consent:** Greg confirmed October 16, 2026 that the contributor approved being credited. Justin's relationship to Greg: not captured (per `sources/justin-macbale-test-adversarially.md`).

## Feedback providers
- Justin J MacBale (see above).

## Sources
- No external statistics. Sample prompts only.
- Justin's original text: **not recovered** (source file says lost to context compression).

## Red-team reviews
- **None.** Greg confirmed October 16, 2026 that no red team has been done. To do (BACKLOG.md item 7).

## Decisions and rejected framings
- Context-gap failure mode added October 12, 2026; trust-vs-validity distinction added October 13, 2026 (both from Justin).

## Status and open questions
- Recover Justin's original text if possible.
- Red team after the reorder.

## Connections
- **Related patterns:** 01, 05 (page); referenced by 06, 08, 12.
- **Companion skill:** Test Adversarially skill ("diagnosing which failure modes apply, proposing adversarial lenses"); "Use this pattern" modal on the page.
- **Backlog items:** 7.

## History
- October 10, 2026: initial launch.
- October 12, 2026: own page, illustration, context-gap failure mode, Justin credit.
- October 13, 2026: trust vs. validity.
- October 14, 2026: "Use this pattern" modal.
- October 15, 2026: Foundation tag; reorder drafted.

---
*Record drafted October 15, 2026 (overnight run) from git history, the `sources/` folder, BACKLOG.md, pattern pages, and Greg's project notes. Items marked **Not captured** were not found in any record - Greg to fill in or confirm.*
