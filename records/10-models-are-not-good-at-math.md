# Record: Pattern 10 - Models Are Not Good at Math - But They Can Program

**Category:** Accuracy  
**Maturity level:** Foundation  
**Status:** In Review  
**Page:** `patterns/10-models-are-not-good-at-math.html`

## Purpose
Names the failure of asking AI to calculate, producing confident compounding errors. Value: ask AI to write the formula or script that calculates, then verify and run it yourself.

## Idea providers
- Greg Stellflue - author. **Not captured:** any outside inspiration.

## Feedback providers
- Red-team personas: **Not captured** (names).

## Sources
- No external statistics. The 73% vs. 91% resource-utilization example is a hypothetical.

## Red-team reviews
- **Red-teamed before commit (October 14, 2026)** - Greg confirmed; changes recorded in commit 77b0ef4: added steering-committee failure scenario; clarified models recall numbers fine but miscalculate; led with Excel formula over Python; reframed durability as a practice argument. Team composition: **Not captured.**

## Decisions and rejected framings
- Excel formula chosen as the primary recommendation, not Python.

## Status and open questions
- Page shows the Accuracy tag but **no In Review tag** in its header, unlike 06, 07, 09, 11, 12 - check.

## Connections
- **Related patterns:** 05, 07 (page); cited by 11 and 12.
- **Coming Soon siblings:** AI Reads, Tools Copy (same family); Avoid the Naughty List (cleanup scripts).
- **Backlog items:** 7.

## History
- October 13, 2026: added to backlog.
- October 14, 2026: drafted, red-teamed, carded In Review.
- October 15, 2026: Foundation tag; duplicate Coming Soon entry removed.

---
*Record drafted October 15, 2026 (overnight run) from git history, the `sources/` folder, BACKLOG.md, pattern pages, and Greg's project notes. Items marked **Not captured** were not found in any record - Greg to fill in or confirm.*
