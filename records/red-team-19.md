# Red team - Pattern 19, Research Partner, Not All-Knowing Oracle (overnight, October 25-26, 2026)

Findings only - nothing applied. Greg makes the calls Monday morning (Morning Review form). Reviewed: patterns/19-research-partner-not-oracle.md (with Greg's October 23 answers: Practice; Mata in both 06 and 19; the October 15 source check as the example).

**Team (approved by Greg, October 23, 2026):**
- **Helen Marsh (adversarial)** - fact-checker at a business magazine who has caught AI-fabricated quotes in submitted articles and thinks AI research is a liability.
- **Carlos Ruiz** - management consultant who builds client decks against deadlines and needs speed.
- **Priya Shah** - corporate librarian and research specialist.
- **Tom Gallagher** - general counsel who has to defend what the company publishes.

**Source check tonight:** the Deloitte Australia story was verified at AP (Rod McGuirk, October 7, 2025): AU$440,000 report, partial refund, "references to nonexistent academic research papers" and "a fabricated quote from a federal court judgment," found by Sydney University researcher Chris Rudge. AP calls the errors "apparent" AI-generated errors; Deloitte did not confirm AI caused them, but the revised report disclosed it used Azure OpenAI. Mata v. Avianca stays verified via sources/research-06-ai-as-amplifier.md.

---

## Round 1 - Problem and Value

**Helen (adversarial):** You write that Deloitte refunded a report "after a researcher found fabricated references" and put it under AI failures. AP says "apparent" AI errors, and Deloitte never said AI caused them. If I'm checking this page, that sentence fails my check - on a page about checking sources. Say what's confirmed: fabricated references and a made-up court quote, and a revised report that disclosed Azure OpenAI.

**Tom:** The real risk isn't only the fake case. It's the real source that says something different from the summary. That's the one that gets past a quick "does it exist?" check, and it's the one I see most. You mention it in a list in paragraph two. Give it its own line.

**Carlos:** The Problem reads like "AI is dangerous for research." I'm the guy who has to hit Friday. Lead with what I get: research I couldn't do before, in an afternoon. Your own line - "I would never have been able to research and quote sources the way I can now" - should open the page, not sit in the middle of paragraph one.

**Priya:** "Every claim traceable" is the value I'd sell to a CFO. But the measure - "share of citations verified at the original" - is hard to count. Make it something a person can actually track: how many sources you dropped because you couldn't confirm them, and how many errors someone else found after you published (the goal is zero).

**Round 1 proposed changes:**
1. Reword the Deloitte example to what AP confirms: fabricated references and a made-up court quote; Deloitte didn't confirm AI caused them, but the revised report disclosed Azure OpenAI. (Helen)
2. Give "a real source that says something different from the summary" its own sentence as the hardest failure to catch. (Tom)
3. Open the Problem with Greg's line and the upside, then the risk. (Carlos)
4. Change the measure to two counts: sources dropped as unconfirmed, and errors found by others after publishing. (Priya)

## Round 2 - Context, Solution, and Use this pattern

**Helen (adversarial):** Step 2 says "open the actual study." Fine - but AI tools now link to real pages that don't contain the quote. The link working proves nothing. Tell people to find the exact passage on the page, or it isn't checked.

**Priya:** Step 1 asks the AI for author, title, date and link. A model without search will happily produce all four for a paper that doesn't exist. Say plainly: use a tool that actually searches and shows its sources (Pattern 17), and treat a citation from a tool that can't search as a lead to look for, not a source.

**Carlos:** Five steps is right, but I'll skip Step 3 under deadline. Give me the minimum: if a claim will be published or presented, it gets checked; everything else can stay a lead. That's a rule I'd actually follow.

**Tom:** Context should name where this matters most - anything with legal, financial or regulatory weight, and anything published under the company's name. And Step 5's "keep the receipts" should say where: with the work, not in someone's browser history.

**Helen (adversarial), on Use this pattern:** Phase 2 tells the AI "never invent a source." It will anyway, sometimes - that's the whole problem. Don't let the prompt sound like a guarantee. Add a line the AI says every time: "I can be wrong about sources. Check each one before you use it."

**Round 2 proposed changes:**
5. Step 2: a source is checked only when you've found the exact passage on the original page - a working link isn't enough. (Helen)
6. Step 1: use a tool that searches and shows its sources (Pattern 17); a citation from a tool that can't search is a lead, not a source. (Priya)
7. Add a minimum rule: anything you'll publish or present gets checked; the rest can stay a lead. (Carlos)
8. Context: name the highest-stakes cases - legal, financial, regulatory, and anything published under the company's name. Step 5: keep the receipts with the work. (Tom)
9. Use this pattern: the AI ends each answer with "I can be wrong about sources. Check each one before you use it." (Helen)
