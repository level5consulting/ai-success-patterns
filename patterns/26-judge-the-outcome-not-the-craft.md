# Pattern 26 - Judge the Outcome, Not the Craft

**Category:** Governance (matches the Coming Soon card)
**Maturity level:** Leadership (proposed)
**Status:** DRAFT 1 (November 3, 2026). Not red-teamed. Not built as HTML. Number 26 is proposed - next free number.

**Where it came from:** Greg, October 26, 2026 (Morning Review), from a composite interview he pasted October 24 (sources/composite-leading-experts-you-cant-replace.md - fictional subject; ideas only, no credit, no quotes). Greg's calls: its own pattern, not a section in 19; "Separate the Technical Call from the Business Call" and "Design the Room" folded in, not separate patterns.

**Lead (draft):** AI agents can already do work you can't do yourself - and can't check line by line. That isn't new. Managers have led engineers, actuaries and surgeons they could never replace for decades. They didn't judge the craft. They owned the goal, judged the results, used independent review, and kept the business calls for themselves. Lead your AI the same way.

---

## Problem
**You can't grade work you can't do**

A leader asks an AI agent to rebuild a pricing model, analyze three years of contracts, or write the code behind a new report. It does it in an afternoon. The leader looks at the result and has no real way to tell if it's right.

So they do one of two things. Some second-guess everything - they rewrite the prompt five times, ask the AI to explain each step, and end up redoing the work by hand. Others wave it through, because it looks finished and they don't know what to check.

Both are old mistakes. They're exactly what new managers do when they first lead experts who know more than they do: micromanage the craft or step away entirely. Neither works with people, and neither works with AI.

AI adds one twist. A person who isn't sure will usually show it. An AI won't tell you it's unsure unless you've built a way for that to come out.

The failure isn't using AI for work beyond your own skill. It's leading it without the habits managers already use to lead experts.

## Value
**Lead what you can't check**

- **Decisions you can defend** - you judge results, independent review and business risk, which you can do, instead of method, which you can't.
- **Less rework** - no more redoing the AI's work by hand to feel safe.
- **Fewer confident mistakes** - independent checks and a stated level of confidence catch what a polished answer hides.
- **Clear accountability** - the technical call and the business call are separated, and a person owns the business call.
- **Less dependence on one black box** - no single model, agent or person becomes the only one who understands a critical piece of work.
- *Measure it:* for each AI-built piece of important work, can you name the outcome measure, who reviewed it independently, and who made the business call?

---

## Context (first pass)
**When this pattern applies**

Use it when AI does work you couldn't do or fully check yourself: code, analysis, models, legal or technical drafting, agents that act on their own. It matters most for leaders and PMOs signing off on AI work, and for anything that goes to a customer, a board or a regulator.

It isn't needed for work you can check at a glance - a short email, a summary of a meeting you attended. There, just read it.

## Solution (first pass)
**Own the goal, judge the results, check independently, keep the business call**

**Step 1: Own the goal, the conditions and the accountability.** Say clearly what good looks like before the AI starts: the outcome, the limits, what it can and can't touch. That's your job, not the AI's. The craft is the AI's job.

**Step 2: Judge the outcome, not the method.** Decide how you'll know it worked - does it run, does it reconcile, does it hold up next month - and check that. Don't grade how confident or polished it sounds.

**Step 3: Use independent and downstream review.** Have someone who knows the craft check it, or a second model, or a test. Ask the people who use the result: if they keep rejecting it, that tells you something even if you can't read the work.

**Step 4: Ask the questions experts respect.** "What would have to be true for this to work?" "What are you least sure about?" "If this is wrong, how would we find out, and how fast?" Make the AI say its level of confidence - it won't offer it on its own.

**Step 5: Separate the technical call from the business call.** Accept the technical answer unless independent review disagrees. The business call - how much risk, what it costs, when it ships - is yours, and you make it openly: "I accept that this has a 10 percent chance of being wrong. For this customer, that's too high."

**Step 6: Don't depend on one source you don't understand.** Document what the AI built and how it was checked (Pattern 12, Ghost in the Workflow). For critical work, make sure a second model, tool or person could take it over.

---

## Notes (planned)
- **Old skill, new worker:** this is how managers have always led experts they couldn't replace - engineers, actuaries, surgeons, cybersecurity specialists. The habits transfer almost unchanged.
- **The one difference:** a person shows doubt; an AI hides it unless the process asks for it. Step 4 is where that gets built in.
- **Connections:** Pattern 19, Research Partner, Not Oracle (check the sources); Pattern 03, Test Adversarially (independent review); Pattern 10, Models Are Not Good at Math (check the numbers with code); Pattern 12, Ghost in the Workflow (no single black box); Pattern 06, AI as Amplifier (your judgment is what gets amplified); Pattern 17, Right Tool, Right Job (a second model as a check).
- **Greg's example:** needed - a time Greg led people who could do things he couldn't (JCI cybersecurity portfolio is a candidate).

## Use this pattern (first pass)
*Paste this into any AI system's custom instructions or at the start of a conversation to run Pattern 26.*

```
# Judge the Outcome, Not the Craft

You are running Pattern 26: Judge the Outcome, Not the Craft from AI Success Patterns (aisuccesspatterns.com).

The pattern's premise: AI can do work the user can't do or check line by line. Lead it the way managers lead experts they can't replace: own the goal, judge outcomes rather than method, use independent review, and keep the business call with a person.

## Phase 1 - Set the goal
Before doing the work, ask the user in one question what the outcome should be and how they will know it worked. Help them write the outcome, the limits, and one or two measures they can check without understanding the method.

## Phase 2 - Do the work and show your confidence
Do the work. Then state plainly what you are least sure about, what would have to be true for it to work, and how the user would find out if it is wrong - and how fast.

## Phase 3 - Set up the checks
Propose how the result can be checked without judging the method: a test, a reconciliation, a second model, an expert reviewer, or feedback from the people who will use it. Say which one matters most.

## Phase 4 - Split the calls
List the technical calls (where the user should accept the answer unless review disagrees) and the business calls (risk, cost, timing) that belong to the user. Do not make the business calls.

## Behavior rules
- One question at a time
- Never present work without stating your confidence and its weak points
- Judge results, not how convincing the work sounds
- The business call always belongs to the user
```

---

## Questions for Greg
1. **Number and level.** Pattern 26, Governance, Leadership - OK?
2. **Your example.** A time you led people who could do things you couldn't (JCI cybersecurity portfolio?), and what you judged instead of the craft.
3. **Red team (proposed).** **Karen Holt (adversarial)** - CTO who says leaders who can't read code shouldn't sign off on AI-built code at all; **Raj Menon** - EPMO lead approving AI-built status and risk reports; **Elena Fischer** - head of internal audit; **Sam Ortiz** - senior engineer who's tired of managers second-guessing his work. Approve or swap?
