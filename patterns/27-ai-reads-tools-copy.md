# Pattern 27 - AI Reads, Tools Copy

**Category:** Accuracy (matches the Coming Soon card)
**Maturity level:** Foundation (proposed)
**Status:** DRAFT 1 (November 4, 2026). Not red-teamed. Not built as HTML. Number 27 is for the file name only.

**Where it came from:** Chris Gallivan's LinkedIn post, October 14, 2026 (sources/chris-gallivan-ai-reads-tools-copy.md). Ideas only, in our words; no quote, and no credit until he agrees (Greg, October 14: reaching out to Chris; "it is more than just spreadsheets"). Consent is not on record.

**Lead (draft):** AI can read a messy spreadsheet and tell you what's going on in it. Ask the same AI to copy that spreadsheet into a new format, and you may get numbers that are slightly off, rows in a new order and entries that are gone. It looks right. Ask AI to explain. Let your tools do the copying.

---

## Problem
**It looks right. It isn't.**

Reading and copying feel like the same skill. In a person, they nearly are: someone who can read a table can copy it. So after AI explains a spreadsheet well, it's natural to say "great, now move these columns into the new template."

But AI doesn't copy the way a tool copies. It writes out what it expects to come next. Most of the time that matches the source, which is what makes it dangerous. A figure changes by a digit. Two rows swap. Row 412 goes missing. A clause in a contract comes back reworded so it reads the same and means something different. A name in the meeting notes gets corrected to a name that was never said.

Nothing flags it. The output has the right shape, the right headers and the right tone, so nobody checks it line by line. Often it's too long for anyone to check that way, which is why they asked AI in the first place.

It isn't only spreadsheets. It's code pasted back with one line quietly changed, contract language, quotes from an interview, records moved from one system to another: anything where the exact text is the point.

The failure isn't using AI on your data. It's trusting it to carry the data across.

## Value
**Understanding from AI, exact copies from tools**

- **Numbers that match the source** - the copy comes from a filter, query, report or script, which does the same thing every time.
- **You keep the fast part** - AI still reads the whole thing and tells you what matters, in minutes.
- **Copies you can prove** - row counts and totals either match or they don't. That's a check anyone can run.
- **Quotes and clauses stay exact** - what people said and what a contract says stay word for word.
- *Measure it:* for each AI-assisted copy, transfer or extract, did a tool do the moving, and do the row count and the totals match the source?

---

## Context
**When this pattern applies**

Use it whenever the exact content matters and the output will be used as data or as the record: moving data between formats, pulling rows from a report, quoting a contract or a source, editing a long file.

It doesn't apply when you want meaning rather than exact content. Summaries, explanations, finding patterns and anomalies, and first drafts are what AI does well. A short list you can check at a glance is fine too. Just check it.

## Solution
**Ask AI to explain. Let tools copy.**

**Step 1: Split the job in two.** Before you start, ask which part is reading and which is copying. "What's unusual in this spreadsheet?" is reading. "Put these rows in the new template" is copying. Give them to different workers.

**Step 2: Use AI to read and explain.** Let it summarize, compare, find anomalies and tell you where to look. Treat what it says as a pointer, and check any figure you plan to repeat against the source (Research Partner, Not All-Knowing Oracle).

**Step 3: Use a tool to copy.** Use a filter, query, report, export, or copy and paste. If you don't know how, have AI tell you the steps or write the formula, query or script, then run that against the source (Models Are Not Good at Math - But They Can Program). The AI writes the tool. It doesn't carry the data.

**Step 4: Prove the copy.** Compare row counts and totals with the source, and spot-check the first row, the last row and a few in the middle. Have the script do this if there is one. If they don't match, stop and find out why.

**Step 5: For words, quote from the source.** When exact wording matters, pull it from the document yourself, or ask AI where the passage is and go read it there. When AI edits a long file, have it change only the named part, then compare the before and after with a tool that shows every difference.

---

## Notes
- **The same family as:** Models Are Not Good at Math (use AI for what it's good at and tools for precision); Avoid the Naughty List (AI writes the fixes, people approve, the system changes the data).
- **Also connected:** Test Adversarially (test before trusting); Right Tool, Right Job; Research Partner, Not All-Knowing Oracle (check against the source).
- **Greg's example:** [GREG: a time AI quietly changed something it was asked to copy? This library's own rule to edit files with a script rather than retype them is a candidate: "never re-type a file's content."]

## Use this pattern
*Paste this into any AI system's custom instructions or at the start of a conversation to run AI Reads, Tools Copy.*

```
# AI Reads, Tools Copy

You are running AI Reads, Tools Copy, an AI Success Pattern (aisuccesspatterns.com).

The pattern's premise: AI reads and explains well, but when asked to reproduce content it may write what it expects instead of what is there. Use AI to explain. Use tools to copy, and prove the copy.

## Phase 1 - Split the job
Ask the user in one question what they want done with the content. Sort each part into reading (summarize, explain, compare, find anomalies) or copying (move, extract, reformat, quote exactly).

## Phase 2 - Do the reading
Do the reading parts. Say which figures or quotes the user should check against the source before repeating them.

## Phase 3 - Hand the copying to a tool
Do not retype data or exact text as your answer. If you can run code on the source file, do the copy with code. If not, give the user the steps, formula, query or script to run themselves, using the tools they have.

## Phase 4 - Prove it
Tell the user how to check the copy: row counts, totals, and a spot check of the first row, the last row and a few in the middle. If you ran the copy, run these checks and show the results.

## Behavior rules
- One question at a time
- Never present retyped data as an exact copy; if asked to, say the risk and offer the tool route
- Short lists the user can check at a glance are fine; tell them to check
- Exact wording comes from the source, not from your memory of it
```

---

## Questions for Greg
Level Foundation? Your example? Chris Gallivan: did he answer about credit? Red team proposed: Nina Sorensen (adversarial, data engineer: "this is a model limit that will go away, and people won't write queries"), Marcus Hale (finance manager moving data each month), Joy Adeyemi (paralegal quoting contracts), Pete Lindgren (small-business owner who only has Excel).
