# Pattern 17 - Right Tool, Right Job

**Category:** Accuracy (from the Coming Soon card - confirm)
**Maturity level:** Leadership (Greg, October 21, 2026)
**Red team:** overnight October 21-22; all 12 changes accepted by Greg October 22 (3 and 9 with his edits) and applied.
**Status:** FIRST DRAFT, questions answered October 21 (overnight, October 20-21, 2026) - Problem, Value, first-pass Context and Solution, Notes plan, first-pass "Use this pattern." Not red-teamed (overnight red team after Greg approves a team). Not built as HTML.

**Coming Soon card (current, live):** 'What's the best AI?' is the wrong question. The right question is: best for what? Organizations that standardize on one model across all use cases are optimizing for procurement convenience, not performance. Model selection should follow the task.

**Lead (draft):** "What's the best AI?" is the wrong question. Best for what? Different models are good at different jobs - and so are tools that aren't AI at all. Match the tool to the task, and check the match when the task matters.

---

## Problem
**One model for every job - and no named exceptions**

Most organizations pick an AI tool the way they pick an email system: one vendor, one contract, everyone on it. That's usually the right call. One platform means one security review, one place company data goes, one training program, and one bill.

The failure isn't the standard. It's having no named exceptions. Models aren't interchangeable. Some are stronger at long documents, some at code, some at careful reasoning, some at speed and cost. Some can search the web or run code; some can't. A model that's excellent at drafting can be poor at arithmetic (Pattern 10). A tool that's great for a quick answer can be the wrong one for research you'll cite - and sometimes the right tool isn't AI at all.

When the default handles everything, the weak spots don't show up as "wrong tool." They show up as "AI isn't good at this" - and the team stops using AI for work it could do well with the right tool.

I found this out starting Level 5ive. I first tried two popular AI chat tools to build my marketing materials, and both were wrong for the job: they didn't have the depth of business knowledge I needed. When I switched, I got answers and value much faster. Neither of the first two would have gotten me where I am in three months.

## Value
**Better results from the AI you already pay for**

- **Fewer "AI can't do this" conclusions** that are really "this AI can't do this." That's the real cost of the wrong tool: teams stop using AI for work it could do well.
- **Better output on the work that matters** - the right tool for long documents, code, analysis, or research, instead of one model's average.
- **Spend you can see** - track spend by tool, or cost per recurring task, so cheaper tools go to routine work and the strongest to the hard jobs.
- **A deliberate standard, not an accidental one** - one default for most work, with named exceptions, chosen on purpose.
- **Every exception has an approved data path.** Each extra tool is another place company data goes, so no exception goes live without one.
- *Measure it:* for a few recurring tasks, compare results and time across approved tools; track spend by tool; track how often people say "AI couldn't do it" before and after.

---

## Context (first pass)
**When this pattern applies**

This pattern applies when an organization is choosing or standardizing AI tools, when a team concludes "AI is bad at this," or when a task matters enough that output quality is worth a second look.

It applies most to recurring tasks with real stakes: analysis that feeds decisions, code that ships, research that gets cited, content that represents the organization.

It is not an argument against standardizing. One default for most work is sensible for security, cost, and support. The pattern is about naming the exceptions on purpose.

## Solution (first pass)
**One default, named exceptions - matched to the job and checked on your own work**

**Step 1: Name the job, not the tool.** Before choosing, describe the task: what goes in (a 200-page contract, a spreadsheet, a code base), how sensitive that data is, and how much data the job actually needs - which depends on the domain and the risk. Then what comes out (a summary, a number, working code), and what being wrong would cost.

**Step 2: Match the job to the right kind of tool.** Start with five quick questions:
1. Is the work worth doing at all? If not, simplify it or drop it (AI Friction).
2. Does it follow fixed rules with predictable inputs? Then ordinary automation - a formula, a workflow, a report - is usually the right tool, not AI.
3. Does it need reasoning or judgment? That's where AI earns its place.
4. Can you measure and manage the risk - test it, oversee it, trace what it did?
5. Is the value worth the complexity? If not, start smaller.

Then match the job to a tool's strengths: long documents, code, calculation (write code, don't calculate - Pattern 10), research with sources (a tool that searches and cites), quick drafts. A fast way to start: ask the AI what it's good at and what it isn't - and ask it what other tools do well. A model that knows it can't make images will often point you to good ones. Don't just take a model's word for itself; Step 3 is the check.

**Step 3: Test on your own work - with approved tools.** Run the same real task through the approved tools you have, or request a time-boxed pilot for one that isn't approved yet. Compare the output, not the demo. Do this for the few tasks that matter most, not everything.

**Step 4: Set one default and name the exceptions.** This is the heart of the pattern. Keep one standard tool for most work. Write down the few tasks where another tool is better, who can use it, and its approved data path - and name who approves a new exception, so the list stays short on purpose.

**Step 5: Revisit at renewal and when the tools change.** Re-run Step 3 on your key tasks at contract renewal, when a major new model is released, and when people start saying "AI can't do this" again.

---

## Notes (planned)
- **Connections:** Pattern 10, Models Are Not Good at Math (the clearest wrong-tool case); AI Friction (Coming Soon - whether AI is the right tool at all; kept separate per Greg, October 15, 2026, unless "no tool" is folded in here); AI Reads, Tools Copy (Coming Soon - AI explains, tools extract); Research Partner, Not Oracle (Coming Soon - the right tool for cited research); Pattern 12 (record which tool an asset depends on).
- **Governance angle:** procurement and security drive one-tool standards for good reasons; the pattern should respect that and offer the "default plus named exceptions" middle path.

## Use this pattern (first pass)
*Paste this into any AI system's custom instructions or at the start of a conversation to run Pattern 17.*

```
# Right Tool, Right Job

You are running Pattern 17: Right Tool, Right Job from AI Success Patterns (aisuccesspatterns.com/patterns/17-right-tool-right-job.html).

The pattern's premise: "What's the best AI?" is the wrong question - best for what? Match the tool to the task, and check the match when the task matters.

## Phase 1 - Name the job
Ask the user, in one question, what task they're trying to do. Then confirm three things in one short summary: what goes in, what comes out, and what being wrong would cost. Ask one follow-up only if one of those is unclear.

## Phase 2 - Match the tool
The best way to know what a tool is good at is to ask it - so answer that honestly. Say plainly whether you are a good tool for this job and why. Name your own limits for it (for example: calculation, current information, exact copying of large data, citing sources). If another kind of tool would do it better - a spreadsheet formula, code, a search tool, a database query, a different kind of AI tool - say so and why. Do not name specific products unless the user asks.

## Phase 3 - Suggest a quick test
If the task matters, suggest one simple way to check the match on the user's own work: run the same small example through two tools and compare the result, not the explanation.

## Behavior rules
- If the work involves sensitive data, tell the user to check their organization's approved tools before trying another
- Don't just describe yourself - also say what other kinds of tools do well for this job
- One question at a time
- Be honest about your own limits - recommending another tool is a good outcome
- "Not AI" is a valid answer
- Stop after the recommendation; the user decides
```

---

## Sources
- None yet. Possible support to look for (verify at source before use): published model comparisons or benchmarks by task type; enterprise surveys on multi-model use. Avoid naming products or rankings that go stale quickly.

## Questions for Greg - answered October 21, 2026
1. Leadership. 2. Keep "not AI" here, reference AI Friction. 3. Greg's example: starting Level 5ive, two popular chat tools were wrong for building marketing materials (kept product-neutral on the page). 4. No product names; point out that the best way to know is to ask the AI what it is good at. 5. Team approved.

## Original questions
1. **Category and level.** Accuracy (card) - Practice for choosing per task, or Leadership because standardization is an organizational call?
2. **"No tool" option.** Fold "not AI at all" in here (Step 2 currently includes it), or keep that strictly for AI Friction?
3. **Your example.** A time you saw a team write off AI because the tool was wrong for the job - at Planview with Anvi, JCI, or a customer?
4. **Product names.** Stay product-neutral (current draft), or name examples like "a search-and-cite tool" vs. specific products?
5. **Red team.** Proposed team for tomorrow night: **Gary Lindholm (adversarial)** - CIO who standardized on one AI platform for security and cost and will defend it; **Ana Reyes** - data analyst who juggles three AI tools daily; **Marcus Chen** - procurement and vendor-management lead; **Sophie Brandt** - security and compliance officer. Approve or swap?

---

## Input for the October 21-22 red team (Greg, October 21, 2026)
Greg: Scott Baker's "Automation & AI Decision Tree" "will fit in choose the right AI" (sources/scott-baker-automation-ai-decision-tree.md, image in sources/images/). Have the red team consider folding its decision order into the Solution, paraphrased: worth doing at all? (if not, simplify or drop - AI Friction); deterministic? (traditional automation - the "not AI" option in Step 2); needs reasoning or interpretation?; can the risk be measured and managed? (oversight, audit trail - Patterns 15 and 12); does the value justify the complexity? (start smaller). Then choose the simplest approach that works reliably: AI that assists people, or an agent that acts within limits. Also Greg's comment on Nysa Zaran Evagelinos's post: how much data a task needs depends on the domain and the risk (sources/nysa-zaran-evagelinos-data-readiness.md). Credit Scott Baker only with his consent.
