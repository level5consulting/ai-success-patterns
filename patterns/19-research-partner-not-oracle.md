# Pattern 19 - Research Partner, Not All-Knowing Oracle

**Category:** Accuracy (Greg, October 19, 2026)
**Maturity level:** Practice (Greg, October 23, 2026)
**Status:** DRAFT 2 (overnight, October 26-27, 2026) - red-teamed October 25-26 (records/red-team-19.md); all 9 of Greg's accepted calls applied. Not built as HTML. Ready to propose for In Review.

**Greg's line (October 19, 2026):** "I would have never been able to research and quote sources like I can with you helping."

**Lead (draft):** AI puts real, source-backed research within reach of anyone - and makes it just as easy to cite sources that don't exist. Treat AI as a research partner whose every citation you check at the source, not an oracle whose answers you repeat.

---

## Problem
**The same tool that finds sources can invent them**

I would never have been able to research and quote sources the way I can now. AI has changed who can do research. A consultant, a project lead, or a small-business owner can find studies, pull figures, and trace an argument back to where it started in an afternoon - work that used to need a research team or a week in the library.

But the same fluency that finds real sources can produce convincing fake ones: a study that doesn't exist, a quote nobody said, a statistic with the decimal in the wrong place, and a real source that says something different from what the summary claims. It all reads exactly like the real thing.

The last one is the hardest to catch. The source exists, the link works, and a quick check passes - but the source doesn't say what you're about to repeat.

The cost is public and rising. In 2023, a lawyer filed a brief built on AI research without reading the cases; several of the cases didn't exist, and the court sanctioned the lawyers (Mata v. Avianca). In 2025, Deloitte Australia partially refunded a AU$440,000 government report after a university researcher found references to research papers that don't exist and a made-up quote from a federal court judgment (AP, October 7, 2025). Deloitte didn't say AI caused the errors, but the revised report disclosed that it had used Azure OpenAI.

The failure isn't using AI for research. It's treating its answers as the source instead of as a lead to the source.

## Value
**Research you'd defend, done in a fraction of the time**

- **Research that used to be out of reach** - finding, reading, and comparing sources across a topic, without a research team.
- **Every claim traceable to where it came from** - so you can answer "where did you get that?" in the room.
- **Errors caught before they leave your hands** - the fabricated reference, the wrong figure, the source that says something else - found by you, not by your audience.
- **Credibility that compounds** - people learn that your numbers check out.
- *Measure it:* two counts - sources you dropped because you couldn't confirm them, and errors someone else found after you published (the goal is zero).

---

## Context (first pass)
**When this pattern applies**

This pattern applies whenever AI helps you gather evidence that you or others will rely on: articles, presentations, proposals, business cases, policy and legal work, anything with a statistic or a quote.

It matters most when the claim will be repeated - published, presented, put in front of a client or a court - because that's when a fabricated source does the most damage. The highest stakes: anything with legal, financial or regulatory weight, and anything published under your organization's name.

It is not a reason to avoid AI for research. It's how to use it so the speed doesn't cost you your credibility.

## Solution (first pass)
**Let AI find the leads, then check every one at the source**

**Step 1: Use a tool that searches, and ask for sources, not just answers.** For research, use an AI tool that actually searches and shows its sources (Pattern 17). For every factual claim, ask where it comes from: author, title, date, and a link. A claim with no source is a guess - and a citation from a tool that can't search is a lead to look for, not a source.

**Step 2: Check each source at the original.** Open the actual study, article, filing, or report - not the AI's summary, and not a search snippet about it. Confirm it exists, it says what's claimed, and the numbers match. A source is checked only when you've found the exact passage on the original page - a working link isn't enough.

**Step 3: Mark what you verified, and drop what you couldn't.** Label each source verified or unverified. If you can't confirm it, leave it out or say plainly that it's unconfirmed. A smaller set of real sources beats a long list of maybes. The minimum rule under deadline: anything you'll publish or present gets checked; everything else can stay a lead.

**Step 4: Follow the evidence, even when it disagrees with you.** If the original says something different from what you hoped, change the claim - not the source.

**Step 5: Keep the receipts.** Save the sources you used - the link, the date you checked, the exact passage - with the work itself, not in someone's browser history, so anyone can retrace it later (Pattern 12, and The Chat Is Not Your Memory).

---

## Notes (planned)
- **This library is built this way:** every statistic on aisuccesspatterns.com was checked at its source; an October 15, 2026 source check found four errors on the live site and fixed them; unconfirmed claims were left out (examples in BACKLOG: CSA 15% on Pattern 12, the $86K sanction, the Pattern 04 claim); pasted sources are saved word for word in sources/.
- **Distinct from:** Pattern 03, Test Adversarially (attacks the AI's reasoning; this is about evidence); Pattern 10, Models Are Not Good at Math (the same idea for numbers); Pattern 06, AI as Amplifier (already uses Mata v. Avianca as "The Lawyer" example - decide whether to share or move it).
- **Connections:** Pattern 17, Right Tool, Right Job (use a tool that searches and cites for research); AI Reads, Tools Copy (Coming Soon).
- **Talk story:** a library where every statistic was checked at its source, built by one person in a week.

## Use this pattern (first pass)
*Paste this into any AI system's custom instructions or at the start of a conversation to run Pattern 19.*

```
# Research Partner, Not All-Knowing Oracle

You are running Pattern 19: Research Partner, Not All-Knowing Oracle from AI Success Patterns (aisuccesspatterns.com/patterns/19-research-partner-not-all-knowing-oracle.html).

The pattern's premise: AI makes real research possible for anyone - and makes it just as easy to cite sources that don't exist. Act as a research partner whose every citation the user checks at the original, not an oracle whose answers they repeat.

## Phase 1 - Understand the question
Ask the user, in one question, what they're researching and where the result will be used (an article, a presentation, a business case). Ask one follow-up only if the claim they need to support is unclear.

## Phase 2 - Find leads, with sources
For each claim you offer, give the source: author or organization, title, date, and a link if you have one. If you are not sure a source exists or says this, say so plainly and mark it [Unverified - check before use]. Never invent a source, a quote, or a figure. If you can't find support for a claim, say that.

## Phase 3 - Hand over the checklist
End with a short checklist the user works through: open each source at the original (not a summary or snippet), confirm it exists and says what's claimed, confirm the numbers match, mark each verified or unverified, and drop what can't be confirmed.

## Behavior rules
- One question at a time
- Every factual claim gets a source or an [Unverified] mark
- Never fabricate citations, quotes, or numbers - "I couldn't find support for that" is a good answer
- If the evidence contradicts what the user hoped, say so
- End every answer that cites sources with: "I can be wrong about sources. Check each one before you use it."
- Stop after the leads and the checklist; the user verifies and decides
```

---

## Sources
- **Mata v. Avianca (S.D.N.Y., 2023)** - verified via Bloomberg Law in sources/research-06-ai-as-amplifier.md (already used on Pattern 06).
- **Deloitte Australia refund** - AP (Rod McGuirk), October 7, 2025, verified October 25, 2026: AU$440,000 report; partial refund; "references to nonexistent academic research papers" and "a fabricated quote from a federal court judgment"; found by Sydney University researcher Chris Rudge; AP calls them "apparent" AI-generated errors; the revised report disclosed Azure OpenAI. https://www.news4jax.com/business/2025/10/07/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
- **Greg's own library:** the October 15, 2026 source check (four errors found on the live site).

## Questions for Greg - answered October 23, 2026
1. Example: already in Notes (the October 15 source check that found four errors on the live site) - use that.
2. Level: Practice.
3. Mata v. Avianca: use in both 06 and 19.
4. Name: "Research Partner, Not All-Knowing Oracle" (Greg).
5. Red team approved: Helen Marsh (adversarial), Carlos Ruiz, Priya Shah, Tom Gallagher - runs Sunday night.

## Original questions
1. **Your example.** A time AI gave you a source that turned out to be wrong or fake while building this library - what was it, and how did you catch it?
2. **Level.** Practice (proposed) or Foundation?
3. **Mata v. Avianca overlap.** It's already Pattern 06's "The Lawyer" example. Use it here too, move it here, or use only Deloitte here?
4. **Name check.** Keep "Research Partner, Not Oracle"?
5. **Red team.** Proposed team: **Helen Marsh (adversarial)** - fact-checker at a business magazine who has caught AI-fabricated quotes in submitted articles and thinks AI research is a liability; **Carlos Ruiz** - management consultant who builds client decks against deadlines and needs speed; **Priya Shah** - corporate librarian / research specialist; **Tom Gallagher** - general counsel who has to defend what the company publishes. Approve or swap?
