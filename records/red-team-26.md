# Red team - Judge the Outcome, Not the Craft (November 3, 2026)

Findings only - nothing applied. Greg decides each item in the Morning Review form. Reviewed: patterns/26-judge-the-outcome-not-the-craft.md (draft 2, Greg's example and peer-review note applied).

**Team (approved by Greg, November 3, 2026). All four are fictional reviewers:**
- **Karen Holt (adversarial)** - CTO who says leaders who can't read code shouldn't sign off on AI-built code at all.
- **Raj Menon** - EPMO lead approving AI-built status and risk reports.
- **Elena Fischer** - head of internal audit.
- **Sam Ortiz** - senior engineer tired of managers second-guessing his work.

---

## Round 1 - Problem, Value and Context

**Karen (adversarial):** "Judge the outcome" works when failure shows up. Code can pass every test you can think of and carry a security hole for a year. "Does it run" tells a non-engineer nothing about that. Say plainly where this pattern stops: when failure would be hidden and costly, a person who knows the craft has to review it. A second model doesn't cover that.

**Sam:** "A person who isn't sure will usually show it." Have you met engineers under deadline? Some do, some don't. You also need that line less than you think: the real point is that AI's doubt never shows in its tone. Say that without flattering people.

**Raj:** Your opener is a pricing model. My world is a status report going to the steering committee. Give me one PMO example - an AI-built risk report - so my people see themselves in it.

**Elena:** "Can you name who reviewed it?" is the right measure, but at audit that needs evidence. Say what the record holds: who reviewed it, what they checked, when, and who made the business call.

**Round 1 proposed changes:**
1. Context and Step 3: where failure would be hidden and costly (security, safety, regulated work), a person who knows the craft must review it. A second model alone isn't enough. (Karen, adversarial)
2. Problem: change "A person who isn't sure will usually show it. An AI won't tell you it's unsure" to "People sometimes hide doubt, but you can often hear it. An AI's polish sounds the same whether it's right or wrong." (Sam)
3. Problem: add a PMO example - an AI-built risk report going to the steering committee. (Raj)
4. Step 6 and Measure it: the record says who reviewed it, what they checked, when, and who made the business call. (Elena)

## Round 2 - Solution and Use this pattern

**Karen (adversarial):** Step 4 says to make the AI state its confidence. That number isn't evidence. Models can sound sure and be wrong, and the stated confidence can be off too. Use it to decide where to look, never as the reason to accept. And Step 5 says accept the technical answer "unless independent review disagrees" - which also passes work nobody reviewed.

**Sam:** "A 10 percent chance of being wrong" - where did that number come from? Nobody can give it to you for most work, and it teaches false precision. Also, Step 3's second model: if it reads the first model's conclusions, it tends to agree. Point it at the record, yes - but in a fresh chat, ideally a different model, and ask it what's wrong, not whether it's right.

**Raj:** Your own example says the managers reviewed the *plans*, then managed to completion. The draft only reviews at the end. Step 1 should have the AI write its plan, get that plan reviewed, then manage to it. That's the part of your story my PMs would recognize. Also, name the reviewer in Step 1 - if it's left to the end, review is what gets cut.

**Elena:** Prompt Phase 3 proposes checks but leaves the user to set them up. Have it write a short review brief the user can hand to the second model or the expert.

**Round 2 proposed changes:**
5. Step 4: stated confidence shows where to look, and is never the reason to accept. (Karen, adversarial)
6. Step 5: "Accept the technical answer once independent review has been done and doesn't disagree" - unreviewed work doesn't pass. (Karen, adversarial)
7. Step 5: replace "a 10 percent chance of being wrong" with a plain example with no invented figure: "I accept that this could be wrong in that one case. For this customer, that's too much risk." (Sam)
8. Step 3: run the second model in a fresh chat, a different model if you can, pointed at the record, and ask what's wrong with the work - not whether it's right. (Sam)
9. Steps 1 and 3: have the AI write its plan first, have the plan peer-reviewed, then manage to the plan - Greg's managers' move - and name the reviewer before the work starts. (Raj)
10. Use this pattern, Phase 3: write a short review brief the user can hand to the second model or the expert. (Elena)
