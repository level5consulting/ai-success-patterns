# Red team - Pattern 17, Right Tool, Right Job (overnight, October 21-22, 2026)

Findings only - nothing applied. Greg makes the calls in the morning (Morning Review form).
Inputs: patterns/17-right-tool-right-job.md, including Greg's October 21 answers and the Scott Baker decision-tree input (sources/scott-baker-automation-ai-decision-tree.md; credit pending Scott's consent).

**Team (approved by Greg, October 21, 2026):**
- **Gary Lindholm (adversarial)** - CIO who standardized on one AI platform for security and cost, and will defend it.
- **Ana Reyes** - data analyst who juggles three AI tools every day.
- **Marcus Chen** - procurement and vendor-management lead.
- **Sophie Brandt** - security and compliance officer.

---

## Round 1 - Problem and Value

**Gary (adversarial):** You open by calling my standard "a performance decision nobody made." I made it - on purpose. One platform means one contract, one security review, one place data goes, one training program. You're describing a power user's frustration and calling it an organizational failure. And the Leadership label makes it worse: you're telling CIOs they got it wrong. If you want me to listen, say plainly that standardizing is usually right, and the pattern is about the exceptions. Your Context says that; your Problem doesn't.

**Ana:** The Problem is my life. But "Fewer 'AI can't do this' conclusions" is the best line on the page and it's buried as a bullet. That's the actual cost - teams stop trying. Also, Greg's Level 5ive story is good, but "the work didn't change - the tool did" is the punchline; say what changed in the result, not just that it changed.

**Marcus:** "Lower cost where it doesn't need the best" is real, but you never say how anyone would know the cost. Most organizations can't see per-task cost. If you're going to claim savings, give me a measure I can actually pull - license and usage spend by tool, or cost per recurring task.

**Sophie:** Every extra tool is another place company data goes. The Value section never mentions that. A pattern that encourages more tools without a guardrail will get blocked by people like me - and it should be. Name the tradeoff: each exception needs an approved data path.

**Round 1 proposed changes:**
1. Rewrite the Problem's opening and last line so standardizing is presented as usually right, and the failure is having no named exceptions - not the standard itself. (Gary)
2. Move "fewer 'AI can't do this' conclusions" to the top of Value and say why it matters: teams stop using AI for work it could do well. (Ana)
3. Sharpen Greg's Level 5ive story with what changed in the result, not just that the tool changed (Greg to supply a line). (Ana)
4. Make the cost claim measurable: track spend by tool, or cost per recurring task, and drop "lower cost" if it can't be measured. (Marcus)
5. Add the data tradeoff to Value: every exception is another place company data goes, so each needs an approved data path. (Sophie)

---

## Round 2 - Context and Solution (including "Use this pattern" and the decision-tree input)

**Gary (adversarial):** Step 4, "set a default and name the exceptions," is the one I'd actually adopt - make it the spine. And put an owner on it: who approves an exception? If anyone can declare one, I have twelve tools by spring. Step 3, "run the same task through two tools," assumes people have two tools. In my shop they don't - and shouldn't. Say: test with the approved tools, or request a pilot.

**Ana:** The decision-tree questions belong at the front of Step 2: is it worth doing at all, does it follow fixed rules (then ordinary automation, not AI), does it need judgment, can you manage the risk, is the value worth the complexity. That turns "match the job" from a vibe into a checklist. And "ask the AI what it's good at" is clever but risky - models overstate what they can do. Keep it, but say Step 3 is the check, not the answer.

**Marcus:** Step 5, "revisit when the tools change," needs a trigger I can put in a contract cycle: at renewal, and when a major new model ships. Renewal is when you have leverage.

**Sophie:** "Use this pattern" tells the AI to recommend other tools. Fine - but add one behavior rule: if the work involves sensitive data, tell the user to check their organization's approved tools first. And Step 1 should include "what data goes in" alongside "what comes out" - Greg's own point from the data-readiness thread: how much data a task needs depends on the domain and the risk.

**Round 2 proposed changes:**
6. Make Step 4 (default plus named exceptions) the core of the Solution, and name who approves an exception. (Gary)
7. Reword Step 3 to test with approved tools, or request a time-boxed pilot - not "any two tools." (Gary)
8. Fold the decision-tree questions into the front of Step 2 as a short checklist, paraphrased (worth doing? fixed rules? needs judgment? risk manageable? value worth the complexity?). Credit only if Scott agrees. (Ana)
9. Keep "ask the AI what it's good at," but add that models can overstate their abilities - Step 3 is the check. (Ana)
10. Tie Step 5 to two triggers: contract renewal and a major new model release. (Marcus)
11. Add to Step 1: what data goes in, how sensitive it is, and how much data the job actually needs (domain and risk). (Sophie, with Greg's data-readiness point)
12. Add a "Use this pattern" behavior rule: for sensitive data, check the organization's approved tools before trying another. (Sophie)
