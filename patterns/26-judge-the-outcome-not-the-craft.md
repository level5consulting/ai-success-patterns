# Pattern 26 - Judge the Outcome, Not the Craft

**Category:** Governance (matches the Coming Soon card)
**Maturity level:** Leadership (Greg, November 3, 2026)
**Status:** DRAFT 3 (November 4, 2026) - Greg's red-team calls applied: changes 1, 2, 4, 5, 6, 7, 8, 9 accepted; 3 rejected ("careful of this becoming about PMO - it is general"); 10 rejected (a short brief loses context and probably increases the chance of hallucination) (records/red-team-26.md). In Review page built November 5 (Greg said yes Nov 5), awaiting Publish. Number 26 confirmed (file name only).

**Where it came from:** Greg, October 26, 2026 (Morning Review), from a composite interview he pasted October 24 (sources/composite-leading-experts-you-cant-replace.md - fictional subject; ideas only, no credit, no quotes). Greg's calls: its own pattern, not a section in 19; "Separate the Technical Call from the Business Call" and "Design the Room" folded in, not separate patterns.

**Lead (draft):** AI agents can already do work you can't do yourself - and can't check line by line. That isn't new. Managers have led engineers, actuaries and surgeons they could never replace for decades. They didn't judge the craft. They owned the goal, judged the results, used independent review, and kept the business calls for themselves. Lead your AI the same way.

---

## Problem
**You can't grade work you can't do**

A leader asks an AI agent to rebuild a pricing model, analyze three years of contracts, or write the code behind a new report. It does it in an afternoon. The leader looks at the result and has no real way to tell if it's right.

So they do one of two things. Some second-guess everything - they rewrite the prompt five times, ask the AI to explain each step, and end up redoing the work by hand. Others wave it through, because it looks finished and they don't know what to check.

Both are old mistakes. They're exactly what new managers do when they first lead experts who know more than they do: micromanage the craft or step away entirely. Neither works with people, and neither works with AI.

AI adds one twist. People sometimes hide doubt, but you can often hear it. An AI's polish sounds the same whether it's right or wrong.

The failure isn't using AI for work beyond your own skill. It's leading it without the habits managers already use to lead experts.

## Value
**Lead what you can't check**

- **Decisions you can defend** - you judge results, independent review and business risk, which you can do, instead of method, which you can't.
- **Less rework** - no more redoing the AI's work by hand to feel safe.
- **Fewer confident mistakes** - independent checks and a stated level of confidence catch what a polished answer hides.
- **Clear accountability** - the technical call and the business call are separated, and a person owns the business call.
- **Less dependence on one black box** - no single model, agent or person becomes the only one who understands a critical piece of work.
- *Measure it:* for each AI-built piece of important work, can you name the outcome measure? Does the record say who reviewed it, what they checked, when, and who made the business call?

---

## Context
**When this pattern applies**

Use it when AI does work you couldn't do or fully check yourself: code, analysis, models, legal or technical drafting, agents that act on their own. It matters most for leaders and PMOs signing off on AI work, and for anything that goes to a customer, a board or a regulator.

It isn't needed for work you can check at a glance - a short email, a summary of a meeting you attended. There, just read it.

It also has a limit. Where failure would be hidden and costly - security, safety, regulated work - judging the outcome isn't enough, because the outcome can look fine for a year. There, a person who knows the craft must review it. A second model alone isn't enough.

## Solution
**Own the goal, judge the results, check independently, keep the business call**

**Step 1: Own the goal, the conditions and the accountability.** Say clearly what good looks like before the AI starts: the outcome, the limits, what it can and can't touch. Name who will review the work before it starts - if that's left to the end, review is what gets cut. That's your job, not the AI's. The craft is the AI's job. Then have the AI write its plan first, get that plan peer-reviewed, and manage to the plan.

**Step 2: Judge the outcome, not the method.** Decide how you'll know it worked - does it run, does it reconcile, does it hold up next month - and check that. Don't grade how confident or polished it sounds.

**Step 3: Use peer review, independent and downstream.** Peer review is how managers have always led people who do things they can't. Review the plan first, then the work. Have someone who knows the craft check it, or run a test. Where failure would be hidden and costly, that person is required. The AI equivalent of a peer is another model: use it to check the work. Keep the work in a written record, not just in the chat (The Chat Is Not Your Memory), so you can point the other model at it. Use a fresh chat, a different model if you can, and ask what's wrong with the work - not whether it's right. Then ask the people who use the result: if they keep rejecting it, that tells you something even if you can't read the work.

**Step 4: Ask the questions experts respect.** "What would have to be true for this to work?" "What are you least sure about?" "If this is wrong, how would we find out, and how fast?" Make the AI say its level of confidence - it won't offer it on its own. Stated confidence shows you where to look. It is never the reason to accept.

**Step 5: Separate the technical call from the business call.** Accept the technical answer once independent review has been done and doesn't disagree. Unreviewed work doesn't pass. The business call - how much risk, what it costs, when it ships - is yours, and you make it openly: "I accept that this could be wrong in that one case. For this customer, that's too much risk."

**Step 6: Don't depend on one source you don't understand.** Document what the AI built and how it was checked (Ghost in the Workflow): who reviewed it, what they checked, when, and who made the business call. For critical work, make sure a second model, tool or person could take it over.

---

## Notes
- **Old skill, new worker:** this is how managers have always led experts they couldn't replace - engineers, actuaries, surgeons, cybersecurity specialists. The habits transfer almost unchanged.
- **The one difference:** you can often hear a person's doubt; an AI's polish sounds the same either way. Step 4 is where asking for it gets built in.
- **Connections:** Research Partner, Not All-Knowing Oracle (check the sources); Test Adversarially (independent review); Models Are Not Good at Everything (check the numbers with code); Ghost in the Workflow (no single black box); AI as Amplifier (your judgment is what gets amplified); Right Tool, Right Job (a second model as a check); The Chat Is Not Your Memory (the record the second model reads).
- **Greg's example (November 3, 2026):** I have had managers who could not program. They used peer reviews to have us build acceptable plans, and then managed us to completion of those plans.

## Use this pattern
*Paste this into any AI system's custom instructions or at the start of a conversation to run Judge the Outcome, Not the Craft.*

```
# Judge the Outcome, Not the Craft

You are running Judge the Outcome, Not the Craft, an AI Success Pattern (aisuccesspatterns.com).

The pattern's premise: AI can do work the user can't do or check line by line. Lead it the way managers lead experts they can't replace: own the goal, judge outcomes rather than method, use independent review, and keep the business call with a person.

## Phase 1 - Set the goal
Before doing the work, ask the user in one question what the outcome should be and how they will know it worked. Help them write the outcome, the limits, and one or two measures they can check without understanding the method, and name who will review the work. Then write your plan and ask the user to get it reviewed before you start.

## Phase 2 - Do the work and show your confidence
Do the work to the plan. Then state plainly what you are least sure about, what would have to be true for it to work, and how the user would find out if it is wrong - and how fast. Say that your confidence shows where to look, and is not a reason to accept.

## Phase 3 - Set up the checks
Propose how the result can be checked without judging the method: a test, a reconciliation, a second model in a fresh chat pointed at a written record of the work and asked what's wrong with it, an expert reviewer, or feedback from the people who will use it. Say which one matters most. If failure would be hidden and costly (security, safety, regulated work), say that a person who knows the craft must review it.

## Phase 4 - Split the calls
List the technical calls (where the user should accept the answer once independent review has been done and doesn't disagree) and the business calls (risk, cost, timing) that belong to the user. Do not make the business calls.

## Behavior rules
- One question at a time
- Never present work without stating your confidence and its weak points
- Judge results, not how convincing the work sounds
- The business call always belongs to the user
```

---

## Questions for Greg - answered November 3, 2026
Number 26, Governance, Leadership: yes. Example: managers who couldn't program used peer reviews (in Notes). Red team approved: Karen Holt (adversarial), Raj Menon, Elena Fischer, Sam Ortiz.
