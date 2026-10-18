# Pattern 14 - Embed the Expert

**Category:** Conversational (Greg, October 18, 2026 - changed from Agentic; update the Coming Soon card)
**Maturity level:** Practice
**Status:** FIRST DRAFT (overnight, October 16-17, 2026) - Problem and Value, plus a first pass at Context and Solution. Not red-teamed (live red team with Greg). Not built as HTML.

**Coming Soon card (current, live):** Your best practitioners' judgment stays personal. It gets shared informally when they're available, inconsistently when they're not, and it walks out the door when they leave. The fix: package that judgment as a reusable skill anyone can run.

**Lead (draft):** Your best practitioner reviews a charter in ten minutes and finds the three problems everyone else missed. That judgment helps one project at a time, when they're free. Package it as a skill - a set of instructions an AI runs the way they would - and it helps every project, every time.

---

## Problem
**Expert judgment scales one conversation at a time**

Every organization has a few people whose judgment others seek out. The senior PM who can read a project plan and say exactly where it will slip. The architect who spots the integration that will fail. The finance partner who knows which business case assumption won't survive the steering committee. Their judgment is the most valuable thing in the building, and it reaches only the people who can get time on their calendar.

At Planview, our CTO, Louise Allen, wrote articles that showed how she thought - and they were amazing. They reached more people than her calendar ever could. But an article explains a way of thinking; it can't apply it to your project on a Tuesday afternoon. [STORY - DETAILS NEEDED FROM GREG: what the articles covered, and how people used them. CONSENT NEEDED: Louise's OK to be named before publishing; otherwise anonymize as "a CTO I worked with."]

So it gets shared the way it always has: informally, when they're available. A hallway question. A review squeezed between meetings. A junior colleague who happens to sit nearby. Everyone else gets nothing, or gets a weaker version from whoever was free. The quality of a project's review depends on who was available that week.

When the expert leaves, retires, or moves to another role, it goes with them. That's not a distant risk. More than 4.1 million Americans turn 65 every year through 2027. Not all of them will retire, but a large share of the senior practitioners organizations depend on are nearing retirement, and their judgment is on the clock.

The philosopher Michael Polanyi observed that we know more than we can tell. Expert judgment is mostly that kind of knowledge: the expert does it without being able to fully explain it, so it rarely gets written down.

AI changes what's possible. An expert's way of reviewing a charter, pressure-testing a business case, or diagnosing a troubled project can now be written down as a **skill**: a reusable set of instructions an AI follows to apply that expert's approach on demand. Most organizations haven't done it. They use AI to produce more output, and leave their best judgment exactly where it was: in a few people's heads.

## Value
**The best judgment in the building, available on every project**

- **Every project gets the expert's first pass.** Reviews that only happened when the expert was free now happen every time, consistently.
- **The expert's time goes further.** Routine reviews run through the skill; the expert spends their time on the hard cases the skill flags.
- **Judgment survives turnover.** When the expert moves on, their approach stays in a form others can run, inspect, and improve.
- **New practitioners learn the expert's reasoning.** A skill that explains why it flags something teaches as it reviews (see Pattern 09).

---

## Context (first pass)
**When this pattern applies**

This pattern applies when one person's judgment is a bottleneck: work waits for their review, quality varies by who was available, or their departure would leave a visible gap. It fits best when the judgment follows a describable approach - questions they always ask, red flags they always check, a sequence they always follow - even if they've never written it down.

It does not replace the expert. A skill captures how an expert usually thinks, not everything they know. Novel situations, political judgment, and decisions with real consequence still need the person. The skill handles the first pass; the expert handles what the first pass surfaces.

It is the deliberate mirror of Pattern 12, Ghost in the Workflow. Ghost in the Workflow is what happens when knowledge gets trapped in AI by accident. Embed the Expert captures it on purpose, documented from the start.

## Solution (first pass)
**Interview the expert, write the skill, test it against the expert**

**Step 1: Pick one judgment, not a whole job.** "How Maria reviews a project charter" is a skill. "Everything Maria knows about project management" is not. Choose a review or decision that happens often and that people already wait for.

**Step 2: Interview the expert.** Use Pattern 05's interview approach: have AI ask the expert hard, specific questions about how they do this one thing - what they look at first, what makes them worried, what they've seen go wrong, what they ignore. Capture their answers in their own words.

**Step 3: Write the skill.** Turn the answers into instructions an AI can follow: the questions to ask, the checks to run, the red flags to name, and when to say "this needs a human." Model it on Pattern 08, Assemble the Team, which is itself a pattern packaged as a skill. Keep it tool-neutral: a skill is saved instructions, and works in any AI tool that lets you save and reuse them.

**Step 4: Test it against the expert.** Run the skill on past work the expert already reviewed. Compare its findings to theirs. Where it misses something, ask the expert why they caught it, and add that to the skill. Repeat until the expert would sign their name to the skill's first pass.

**Step 5: Get the expert's buy-in, and credit them.** The skill packages someone's judgment, so settle three things with them up front: they agree to it, they're named as the source, and it's clear who owns and maintains the skill once it's in use. An expert who helped build the skill will keep improving it. One who found out later won't.

**Step 6: Give it a handoff record.** Apply Pattern 12: record whose judgment it captures, what it's for, what it was tested against, its known gaps, and who owns it now. A skill without a record becomes the next ghost.

---

## Notes (planned)
- Pattern 08 (Assemble the Team) and its "Use this pattern" instructions are the working example of a pattern packaged as a skill.
- Each "Use this pattern" modal on the site (BACKLOG item 15) is a small Embed the Expert.
- Mirror of Pattern 12; companion to Pattern 09 (09 is people learning faster with AI; 14 is turning one person's judgment into something others can run).

## Sources
- "More than 4.1 million Americans turn 65 each year through 2027" - Alliance for Lifetime Income, Peak 65 release, January 10, 2024 - https://www.protectedincome.org/wp-content/uploads/2024/01/Peak-65-Release-final-011024.pdf (verified at the source). Note: turning 65 is not the same as retiring - use as a signal of the senior workforce aging out, not a retirement count.
- Michael Polanyi, *The Tacit Dimension* (1966) - "we know more than we can tell." Used in the Problem, paraphrased; credit on the page (Greg, October 18, 2026).

## Definitions
- **Skill:** a packaged, reusable set of instructions an AI follows to apply a specific approach on demand - the questions, checks, and judgment calls an expert would make for one kind of work. Not "skill" in the general human sense.

## Questions for Greg

**Answered October 18, 2026:**
1. Example: Louise Allen, Planview CTO - her articles were amazing. Story placeholder added to Problem; details and Louise's consent to be named still needed.
2. Category: Conversational, Practice.
3. Peak 65: keep, framed as nearing retirement.
4. Polanyi: keep, credited.
5. Expert consent: yes - added as Solution Step 5.
6. Tool-neutral: yes.

**Still open:**
- What Louise's articles covered and how people used them.
- Has Louise agreed to be named?
