# Models Are Not Good at Everything

**Renamed from:** Models Are Not Good at Math - But They Can Program (published, In Review).
**Web address:** stays `patterns/10-models-are-not-good-at-math.html` so links already shared keep working (Greg, November 5, 2026). This draft's file name is for the draft only; the page is an update to the existing page, not a new one.
**Category:** Accuracy
**Maturity level:** Practice (Greg, November 5, 2026 - AI Reads, Tools Copy folds in at Practice). The published page says Foundation - see Questions for Greg.
**Status:** DRAFT 1 (overnight, November 9-10, 2026). Red-teamed the same night, findings only (records/red-team-10-everything.md). Not built as HTML.

**Where it came from:** Greg, November 5, 2026 (decided): make the math pattern a combination pattern that lists the known weak spots, each with its fix. Folds in the AI Reads, Tools Copy draft (patterns/27-ai-reads-tools-copy.md), which comes off Coming Soon; its red team (Nina Sorensen, Marcus Hale, Joy Adeyemi, Pete Lindgren) became this pattern's red team. Chris Gallivan "Inspired by" credit, paraphrased - consent confirmed by Greg, November 5. Work AI Index material and the two proposed weak spots verified at 4 PM, November 9 (records/4pm-checks-2026-11-09.md on ops, sections 1 and 4).

**Lead (draft):** AI is very good at a lot of things. It is not good at everything, and it won't tell you which is which. It sounds just as sure doing arithmetic, copying a spreadsheet or reading a regulation as it does writing a summary. Know the weak spots, and for each one hand the precise part to something that can do it: code for the math, your tools for the copying, the official source and a qualified person for the rules.

---

## Problem
**Same confident voice, right or wrong**

An analyst uploads last quarter's numbers to an AI assistant, skims the summary, and sends it to the CFO. At Monday's quarterly business review, three of the figures don't match the spreadsheet they came from. (That story comes from the Work AI Institute's 2026 Work AI Index.) Nobody lied. The summary read well. The numbers just weren't the numbers.

He isn't unusual. In the same survey, 41% of workers say they sometimes deliver AI-generated work they couldn't explain if asked. Among heavy users - people who use AI for half their work time or more - it's more than half.

I call that botcrap: AI work nobody checked. Sending it on is botcrapping. And the check that stops it - the person who actually reads the work before it goes out - is the botwatch.

Here's why the botwatch matters. AI generates text. That's what it's built to do, and most of the time it does it very well. But some jobs only look like writing. Adding up a column isn't writing. Copying 400 rows into a new template isn't writing. Quoting a regulation isn't writing. On those jobs the AI still writes what a good answer would look like - and what a good answer looks like is usually close to the truth, which is exactly why nobody catches it.

The known weak spots:
- **Math.** Ask for a budget variance or a utilization rate and you get something that looks like a calculation but isn't. It's a prediction of what the answer might be, with the steps shown. The steps look fine. The number is wrong. A program manager pastes a 73% utilization figure into the steering deck; three weeks later the real number turns out to be 91%, and every staffing decision from that meeting was built on a number nobody calculated. (A hypothetical, but you've seen it.)
- **Copying exact data.** AI reads a messy spreadsheet well. Ask it to copy that spreadsheet into a new format and it rebuilds the data instead of carrying it across. A figure changes by a digit. Two rows swap. A row goes missing. A contract clause comes back reworded so it reads the same and means something different. It has the right headers and the right shape, so nobody checks it line by line.
- **Regulatory and compliance work.** Rules change, and the AI may be working from an older version, or another state's or country's version. And in this work the exact wording is the point. "Should" and "must" read alike in a summary. They don't read alike to an auditor.

Two more, proposed for Greg to accept or reject:
- **[PROPOSED] Made-up citations and quotes.** Courts keep getting filings that cite cases AI invented. Damien Charlotin's AI Hallucination Cases database tracks them, and a Stanford CIS analysis (October 2025) of 114 US cases involving attorneys found about 90% came from solo or small firms. The case name, the citation format and the quote all look right. The case doesn't exist.
- **[PROPOSED] Long documents - the middle gets missed.** Researchers (Liu et al., "Lost in the Middle," 2024) found that models do best when the key information is at the start or the end of a long input, and much worse when it's in the middle - even models built for long documents. Ask about a long contract, and a clause buried in the middle is easier to miss than one on the first page.

The failure isn't using AI for these jobs. It's letting the AI's text stand in for the part that has to be exact.

## Value
**Use AI for everything it's good at, and know where to stop**

- **Numbers you can stake a decision on** - a formula or script does the arithmetic, the same way every time, and anyone can read the logic and rerun it.
- **Copies that match the source** - a filter, query, export or script moves the data, and the row counts and totals either match or they don't.
- **Rules you can defend** - the wording comes from the official source and a qualified person signs off, so the answer holds up when someone asks where it came from.
- **You keep the fast part** - AI still reads the whole thing, explains it and tells you where to look, in minutes.
- **A team that knows the weak spots by name** - "did a tool copy that?" and "who signed off on the rule?" become normal questions, not accusations.
- **Value realized from pattern usage** - put in your own numbers: hours saved, rework avoided, errors caught before the meeting instead of after. For a sense of scale, writing and checking the formulas behind a report is part of a financial analyst's job, a role that pays a median of about $103,570 (BLS, May 2025). This pattern covers part of that work. The sign-off on regulated work stays with your qualified person.
- *Measure it:* for each piece of AI-assisted work that will be used as a number, a record or a rule, can you say what did the precise part (a formula, a tool, the official source) and who did the botwatch?

---

## Context
**When this pattern applies**

Use it any time AI output will be used as a number, as data, as an exact quote, or as a statement of what a rule requires - especially when it goes to a decision-maker, a customer, a court, an auditor or a regulator.

It applies even when the job looks simple. Simple arithmetic and short copies are where the errors are hardest to spot: the magnitude feels right, the shape looks right, and the error is small enough to survive a skim.

It doesn't apply when you want meaning rather than exact content: summaries, explanations, first drafts, finding patterns and anomalies, brainstorming. That's what AI does well. A short list you can check at a glance is fine too. Just check it.

The list of weak spots isn't fixed. Models get better at some things, and new weak spots show up as people use AI for new jobs. The habit underneath doesn't change: when the exact answer matters, the AI's text isn't the record.

## Solution
**Calculate with code, copy with tools, review independently**

This is a string, not a single. Three patterns work in sequence: this one (the AI writes the calculation instead of doing it), AI Reads, Tools Copy (the AI explains, your tools move the data), and Judge the Outcome, Not the Craft (someone independent checks the result before it ships). For citations and sources, add Research Partner, Not All-Knowing Oracle.

| Weak spot | What goes wrong | The fix |
|---|---|---|
| Math | A confident number nobody calculated | Have the AI write the formula or script; you run it |
| Copying exact data | Rows changed, swapped or missing | AI reads, your tools copy; prove the copy |
| Regulatory and compliance | Old rule, wrong place, loose wording | Check the official source; a qualified person signs off |
| [PROPOSED] Citations and quotes | Sources that don't exist or don't say that | Open every source and check the quote yourself |
| [PROPOSED] Long documents | The middle gets missed | One section at a time, or key material first |

**Step 1: Sort the job before you start.** Ask which part is reading and explaining, and which part has to be exact: a number, a copy, a quote, a rule. "What's unusual in this spreadsheet?" is reading. "What's the total variance?" is math. "Put these rows in the new template" is copying. "What does the regulation require?" is a rule. Give each part to the right worker.

**Step 2: Math - have the AI write the calculation, not do it.** Instead of pasting data and asking for an answer, ask for a formula or script that produces it, then run it yourself in Excel, Google Sheets, or whatever you have.

- Don't: "Here are my project costs by month. What is the total spend variance against budget?"
- Do: "Here are my project costs by month. Write an Excel formula that calculates total spend variance against budget. Explain the logic so I can check it before I use it."

The second gives you something you can run, inspect and hand to a colleague. Then ask the AI to look at the result for reasonableness - not to recalculate, just to flag anything out of range.

**Step 3: Copying - AI reads, your tools copy.** Let the AI summarize, compare and point you to what matters. Do the moving with a filter, query, report, export, or plain copy and paste. If you don't know how, have the AI tell you the steps or write the formula or script, then run that against the source. The AI writes the tool. It doesn't carry the data. Then prove the copy: compare row counts and totals with the source, and spot-check the first row, the last row and a few in the middle. When exact wording matters, pull it from the document yourself, or ask the AI where the passage is and go read it there.

**Step 4: Regulatory and compliance - the official source, and a person who signs.** Use AI to explain a rule, find which sections apply, and draft questions. Then check every requirement against the official source - the agency, the regulator, the standard itself - for the right place and the current date. Have a qualified person sign off before anything goes out: your compliance officer, attorney, accountant or other licensed professional. You can't judge the craft here, so judge the outcome and use the expert (Judge the Outcome, Not the Craft).

**Step 5: [PROPOSED] Citations and quotes - open every source.** Treat every citation as a lead, not a source. Open it, find the passage, and check that it says what you're about to repeat (Research Partner, Not All-Knowing Oracle). Asking the AI whether its own source is real is not a check.

**Step 6: [PROPOSED] Long documents - don't trust the middle.** Ask about one section at a time, or put the key material at the start of what you give the AI. For anything that matters, ask where in the document the answer is, and go read that page.

**Step 7: Do the botwatch, then ship.** Before the work goes out, someone reads it - ideally someone who didn't produce it. Check the parts that had to be exact against what did them: the formula, the tool, the source, the sign-off. If you couldn't explain it if asked, it isn't ready.

---

## Notes
- **Why the model sounds certain when it's wrong:** models are trained to produce fluent, confident text, so the confidence in an answer is not evidence that it's right. Some models have gotten better at simple arithmetic, and some now run code on their own. That helps. But a formula in a spreadsheet, a query that copied the data, or a link to the official rule is still better than a number or a paragraph in a chat window: it can be checked, rerun and handed to a colleague. That's a practice argument, not a capability argument, and it holds however good the models get.
- **Spreadsheets aren't perfect either:** a well-known audit found errors in 49 of 54 operational spreadsheets (Panko, University of Hawaii, reported by Computerworld, 2004). That's the point: a formula can be audited and fixed. A number in a chat window can't.
- **Why one pattern, not five:** the fixes are different, but the habit is the same - know what AI is weak at, and hand the exact part to something built for it. One name a team can say out loud: "Models aren't good at everything - who checked the numbers?"
- **The string:** Models Are Not Good at Everything -> AI Reads, Tools Copy -> Judge the Outcome, Not the Craft. Calculate with code, copy with tools, review independently.
- **Connections:** Judge the Outcome, Not the Craft (independent review; the expert for regulated work); Research Partner, Not All-Knowing Oracle (check citations at the source); Avoid the Naughty List (AI writes the fixes, people approve, the system changes the data); Right Tool, Right Job (the tool that can actually do the job); Assemble the Team (challenge the work before it matters - bring a compliance voice before the real sign-off); Own the Thinking (don't accept what you can't explain).
- **Greg's example:** [GREG: a time AI quietly changed something it was asked to copy or calculate? Candidate: this library's own rule to edit files with a script rather than retype them.]

**Inspired by**
**Chris Gallivan** - His point that AI is a great reader and a risky copier - it can explain a complex spreadsheet brilliantly, then rebuild the data instead of copying it when asked to move it - shaped the copying section of this pattern.

## Use this pattern
*Paste this into any AI system's custom instructions or at the start of a conversation to run Models Are Not Good at Everything.*

```
# Models Are Not Good at Everything

You are running Models Are Not Good at Everything, an AI Success Pattern (aisuccesspatterns.com).

The pattern's premise: AI sounds equally sure whether it is right or wrong, and some jobs are known weak spots - math, copying exact data, regulatory and compliance work, citations and quotes, and the middle of long documents. Do the reading and explaining. Hand the exact part to something that can do it: code for math, tools for copying, the official source and a qualified person for rules. The string: calculate with code, copy with tools, review independently.

## Phase 1 - Sort the job
Ask the user in one question what they want done and what the result will be used for. Sort each part into reading and explaining, or exact work: a calculation, a copy of data, an exact quote or citation, a statement of what a rule requires, or an answer from deep inside a long document. Tell the user which parts are exact work and why.

## Phase 2 - Do the reading
Do the reading and explaining parts. Say which figures, quotes or claims the user should check against the source before repeating them.

## Phase 3 - Hand off the exact parts
- Math: do not give a calculated number as the answer. Write the formula or script, explain the logic, and tell the user how to run it. If you can run code, run it and show the code and inputs.
- Copying: do not retype data or exact text as an exact copy. Give the steps, formula, query or script, then tell the user how to prove the copy: row counts, totals, and a spot check of the first row, the last row and a few in the middle.
- Rules: explain the rule, then name the official source to check it against and say that a qualified person must sign off. Say if the rule may have changed or may differ by place.
- Citations and quotes: give each source as a lead to open and check, never as confirmed.
- Long documents: work one section at a time, and say where in the document each answer comes from so the user can read it there.

## Phase 4 - The botwatch
Before the user ships the work, list what must be checked and by whom: each formula, copy, quote, citation and rule, and who will review it independently. Say plainly: if the user couldn't explain it if asked, it isn't ready.

## Behavior rules
- One question at a time
- Never present a number you predicted as a number you calculated
- Never present retyped data or text as an exact copy
- Never present a citation or a rule as confirmed until the user has checked the source
- Short lists the user can check at a glance are fine; tell them to check
```

---

## Sources
- The current page, patterns/10-models-are-not-good-at-math.html (math section, the 73% / 91% hypothetical, Panko 2004, "why the model sounds certain").
- patterns/27-ai-reads-tools-copy.md and records/27-ai-reads-tools-copy.md (copying section). Origin: sources/chris-gallivan-ai-reads-tools-copy.md. Failure examples are illustrative, not measured.
- Work AI Institute, 2026 Work AI Index - https://www.glean.com/work-ai-institute/reports/work-ai-index - verified 4 PM, November 9: the 41% line, "more than half of heavy users" (54%, heavy = AI for 50% or more of work time, from a table), the analyst story (paraphrased). Survey: 6,000 full-time digital workers, US, UK and Australia, December 2025 - January 2026.
- [PROPOSED] Stanford CIS, "Who's submitting AI-tainted filings in court?" (October 2025), analysis of Damien Charlotin's AI Hallucination Cases database - https://cyberlaw.stanford.edu/blog/2025/10/whos-submitting-ai-tainted-filings-in-court/ - verified 4 PM, November 9.
- [PROPOSED] Liu et al., "Lost in the Middle: How Language Models Use Long Contexts," TACL 2024 (arXiv 2307.03172) - https://arxiv.org/abs/2307.03172 - verified 4 PM, November 9.
- BLS, financial analysts, median $103,570 (May 2025) - records/hires-you-dont-need.md.
- Regulatory section: no new source needed (4 PM, November 9).

## Questions for Greg
1. Level: Practice (as you set for the copying part) or keep Foundation, which the published page shows?
2. Accept or reject each proposed weak spot: made-up citations and quotes; long documents.
3. Your example (Notes)?
4. Jen Vodenlich's "I just have to check prices" fits the botwatch step. Her consent covers the Results page; ask her before using it here?
5. Red team's numbered decisions: records/red-team-10-everything.md.
