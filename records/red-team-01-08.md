# Red Teams - Patterns 01-08

**Run:** Overnight, October 16-17, 2026 (Assemble the Team, mandatory adversarial voice, personas chosen for each pattern).
**Status:** Findings only. **Nothing has been applied.** Greg makes the calls; accepted changes are applied on a branch afterward.
**Reviewed against:** the live pages in the new Problem - Value - Context - Solution - Notes order.

How to use this file: each pattern ends with a numbered list of proposed changes. Reply with accept / reject / modify per number (for example, "01: accept 1 and 3, reject 2").

---

## Pattern 01 - Begin with the End in Mind (Foundation)

**Team:** Nadia Okafor (adversarial) - agile coach who has spent a decade fighting big up-front requirements; Brian Seidel - corporate communications director who writes for executives daily; Priya Shah - first-year analyst, the Foundation-level reader; Tomás Herrera - EPMO director who would roll this out to 200 people.

**Nadia (adversarial):** This pattern risks teaching waterfall to AI users. "Define done before you start" is right for a CFO summary and wrong for exploration, where you don't know the destination until you see a few drafts. Shubham Dwivedi already spotted this gap in public. The page needs a line saying when not to use it - or a pointer to Iterate to the Destination - or experienced readers will dismiss it as rigid. I'd also challenge the Problem: "the model wasn't wrong; it was just never told what right looks like" is half true. Sometimes the model is wrong too.

**Brian:** The Solution is the strongest part of the page: format, audience, constraints, success criteria. That's how good briefs work. But the example prompt is one long sentence; break it into the four parts so readers see the structure they're meant to copy. And the lead says "the most common source of wasted iterations" - says who? Make it "a common source" or cite it.

**Priya:** As a new user, I understood this in one read. But Context is one sentence and doesn't tell me when it matters most. I'd want "especially when someone else will read the output" or similar. The Notes call it a "parent meta-pattern" - that phrase lost me.

**Tomás:** To roll this out I need it to be teachable in five minutes and checkable. Add a one-line test: "Could someone else tell whether the output met your destination?" That turns it into a team habit. Also, Jeff's suggestion to frame it from success - "what does a usable first draft look like" - would land better with my leaders than leading with failure.

**Proposed changes:**
1. Add a "when not to use it" line pointing to Iterate to the Destination (exploratory work). (Nadia)
2. Soften "the most common source of wasted iterations" to "a common source," unless sourced. (Brian)
3. Format the example prompt as the four labeled parts. (Brian)
4. Expand Context by one or two sentences on when it matters most. (Priya)
5. Replace "parent meta-pattern" with plain language ("Several other patterns build on this one"). (Priya)
6. Add a one-line self-check for teams. (Tomás)
7. Consider Jeff's success framing for the lead. (Tomás; Jeff, BACKLOG item 9)

**Decision (Greg, October 18, 2026):** Accepted 1-6, rejected 7. Applied on branch.

---

## Pattern 02 - Onboard, Don't Program (Foundation)

**Team:** Derek Lund (adversarial) - prompt engineer who believes structured instructions beat prose context; Helen Marsh - HR onboarding lead; Sam Ortega - operations manager who uses AI daily but has never written a system prompt; Ayesha Karim - information-security officer.

**Derek (adversarial):** The title sets up a false choice. "Don't program" tells readers instructions don't matter, but the best results come from both: clear context and explicit constraints. The five-item context document in the Solution is itself a structured program. I'd retitle the idea in the copy - "context before commands" - or acknowledge that good onboarding includes instructions. Also, this is the thinnest published page, about 340 words. It reads like a summary of a pattern, not the pattern.

**Helen:** The onboarding metaphor is right, and it's underused. Real onboarding has a first-day packet, a buddy, and a check-in. The page could borrow that: a reusable context doc (the packet), and a check that the AI understood (ask it to restate the brief). That last step is missing and it's the one that catches misunderstandings.

**Sam:** Give me an example. Patterns 01, 03, and 05 all have sample text. This one lists five things to include but doesn't show a filled-in context document. I'd copy one tomorrow if it were there.

**Ayesha:** "Constraints: budget, timeline, regulatory environment" - be careful. People will paste confidential details into consumer AI tools because the pattern told them to give rich context. Add one line: share what the AI needs, within your organization's data rules.

**Proposed changes:**
1. Acknowledge that good onboarding includes clear instructions - context *before* commands, not instead of them. (Derek)
2. Expand the page; it is the thinnest published pattern. (Derek)
3. Add a "confirm understanding" step - ask the AI to restate the brief before starting. (Helen)
4. Add a short filled-in example context document. (Sam)
5. Add a data-handling caution line. (Ayesha)
6. Candidate for a "Use this pattern" modal (BACKLOG item 15). (Sam)

---

## Pattern 03 - Test Adversarially (Foundation)

**Team:** Marcus Webb (adversarial) - AI researcher skeptical that a model can reliably critique itself; Lena Fischer - internal auditor; Jordan Pike - sales engineer under time pressure; Justin-style domain expert (Rosa Delgado) - clinical data manager who validates outputs for a living.

**Marcus (adversarial):** The core move - ask the same model to attack its own output - has a known weakness: the model that produced an error often can't see it, and it can invent problems that aren't there. The page says the model "will surface its own failure modes more accurately than it will admit to them in passing," which is a strong empirical claim with no source. The Notes mention a separate session; I'd move that into the Solution as the default, not an option, and soften the accuracy claim.

**Lena:** The trust-versus-validity distinction is the best idea on the page, and it's the auditor's whole job. But the Solution ends at "verify flagged items against primary sources." What about unflagged items? Auditors sample. Add: spot-check a few claims the critique didn't flag.

**Jordan:** I'll be honest: I'll skip this when I'm busy. Three prompts plus verification is a lot. Tell me which one to run when I have two minutes. Probably the Context Gap Check - it's the one that tells me what I forgot.

**Rosa:** The Notes reference "The Hallucination Audit (in the backlog)." That pattern isn't in Coming Soon anymore. Either restore it or remove the reference - it's a dead link in the reader's head. Also, the Deloitte Australia refund (October 2025) is the perfect real-world case for this page: fabricated references in a paid report, caught by an outside researcher.

**Proposed changes:**
1. Soften the claim that the model surfaces its own failures accurately, or source it. (Marcus)
2. Make a fresh session the recommended default for adversarial review. (Marcus)
3. Add a spot-check of unflagged claims to the Solution. (Lena)
4. Add a "two-minute version" - the single prompt to run when time is short. (Jordan)
5. Fix the reference to The Hallucination Audit, which is no longer in Coming Soon. (Rosa)
6. Add the Deloitte Australia case as the real-world example (see value-facets report). (Rosa)

---

## Pattern 04 - The AI Operations Manager (Practice)

**Team:** Carla Brooks (adversarial) - COO who has seen "AI assistant" rollouts become shelfware; Kevin Tran - PMO coordinator whose job this pattern partly automates; Diane Wolcott - Microsoft 365 administrator; Raj Menon - portfolio manager running eight projects.

**Carla (adversarial):** The pattern assumes the coordination work is the problem. Often it's the symptom - status chasing exists because the process is broken or people don't trust each other. Automating it can cement a bad process. I'd add a line pointing to Redesign the Stream: fix the stream, then automate what's left. And "drops substantially" is now the only unsupported claim left after the ROI-satisfaction line was cut - give it Asana's 58% baseline or soften it.

**Kevin:** Say the quiet part: this changes what my job is. If the pattern is published for EPMO leaders, it should say where the coordinator's freed time goes - Pattern 11's reinvestment logic applies here too. Otherwise it reads as "replace Kevin."

**Diane:** "Treat each session as a handoff" - in practice, chat sessions don't remember. The pattern needs to say where the standing context lives: a document the AI reads each time, or a project's knowledge files. And it should link to Ghost in the Workflow, because a standing AI coordinator is exactly the kind of asset that becomes a ghost.

**Raj:** The four task examples are useful. I'd add one more that matters to portfolio work: flagging risks and dependencies across projects, not just summarizing status.

**Proposed changes:**
1. Add a line that coordination overhead can be a symptom of a broken process - link Redesign the Stream. (Carla)
2. Anchor or soften "drops substantially" (Asana 58% baseline - see value-facets report). (Carla)
3. Say where freed coordinator time goes - link Pattern 11. (Kevin)
4. Explain where the standing context lives between sessions. (Diane)
5. Link Pattern 12, Ghost in the Workflow - a standing AI role needs a handoff record. (Diane)
6. Add a cross-project risk and dependency example. (Raj)

---

## Pattern 05 - Avoid AI Slop with an LLM Interview (Foundation)

**Team:** Evan Cole (adversarial) - ghostwriter who argues editing AI drafts works fine; Monica Reyes - conference program chair; Li Wei - non-native English speaker who uses AI to polish writing; Joe-style reader (Frank Doyle) - IT director who liked this pattern in conversation.

**Evan (adversarial):** "The instinct is to edit slop into shape. This rarely works." That's an overstatement - good editors do it every day. The stronger claim is that editing a generic draft costs more than starting from your own answers. Say that. And the page assumes everyone has expertise to extract. Someone new to a topic will fail the interview - which is the point, but say it: if the interview comes up empty, you're not ready to write.

**Monica:** From the program-chair seat, this pattern is exactly why I reject talks: the deck looks great and the speaker can't answer the first question. The "Where this pattern came from" note says that - move it up. It's the most persuasive paragraph and it's buried in Notes.

**Li:** Be careful the page doesn't shame people who use AI for language polish. Interview-first and AI-for-polish aren't in conflict. One sentence saying polishing your own words is fine would keep non-native writers from feeling targeted.

**Frank:** This one stuck with me because it names something I see weekly. The workslop research - 40% of workers got it last month, about $186 per person per month - would make the Value section hit even harder. Also, "slop" is the word people use now; keep it.

**Proposed changes:**
1. Replace "This rarely works" with the cost comparison - editing generic drafts costs more than drafting from your answers. (Evan)
2. Add: if the interview comes up empty, you're not ready to write yet. (Evan)
3. Move the origin story (conference decks that couldn't survive Q&A) higher, into Problem or Context. (Monica)
4. Add a line that polishing your own words with AI is fine. (Li)
5. Add the workslop figures to Value (see value-facets report). (Frank)

---

## Pattern 06 - AI as Amplifier, Not Foundation (Practice, In Review)

**Team:** Greta Lindqvist (adversarial) - learning designer who believes AI can legitimately teach novices; Omar Haddad - management consultant; Chloe Park - chief of staff to a CEO; Ben Archer - engineering manager.

**Greta (adversarial):** The pattern is right about faking expertise and wrong to imply novices shouldn't use AI on unfamiliar ground. The second path - "do the work to learn" - is the important one and it's given one paragraph. Pattern 09, The Compressed Apprenticeship, is the real answer for people bringing a gap. Link it, or this page reads as gatekeeping.

**Omar:** The three examples (consultant, analyst, executive) are the best part. They're specific and uncomfortable. I'd add one where the stakes are financial or legal, because "the CFO asked a question" is embarrassing, not costly.

**Chloe:** "Raises the floor and exposes the ceiling" is a strong headline. The test in Notes - "can I walk through this out loud with no screen?" - should be in the Solution. It's the actual practice; right now the Solution is two paths and the test is an afterthought.

**Ben:** Category check: this is tagged Accuracy, but it's about the person, not the output's accuracy. It's closer to Pattern 07 (also Accuracy). Not wrong, but worth a look when the Governance tab and filters change Monday.

**Proposed changes:**
1. Expand the "do the work to learn" path and link Pattern 09. (Greta)
2. Add a fourth example with financial or legal stakes. (Omar)
3. Move the walk-through test from Notes into the Solution. (Chloe)
4. Revisit the Accuracy category for 06 and 07. (Ben)
5. Before publishing: Justin MacBale's reviewer credit is correct here (confirmed October 16). No change.

---

## Pattern 07 - Own the Thinking (Practice, In Review)

**Team:** Isaac Bloom (adversarial) - productivity researcher who thinks offloading cognition is the point of tools; Fiona Grant - university writing instructor; Eric-style manager (Dana Price) - team lead who stopped AI-written submissions; Nate Silva - developer who uses AI for synthesis daily.

**Isaac (adversarial):** Every tool offloads thinking - calculators, search, GPS. The pattern's own GPS analogy cuts both ways: most people are fine not knowing how to navigate without GPS. The page needs to say which capabilities are worth protecting and which are fine to offload. Otherwise "do the discovery yourself" becomes a rule that nobody follows because it costs too much. And the CEPR study is about secondary-school students; extending it to professionals is a reasonable inference, not a finding. Say so.

**Fiona:** The discovery-versus-articulation split is exactly what I teach. One practical gap: people don't know which layer they're in. Give them a tell - "if you can't explain the idea without the AI's wording, you were in the discovery layer."

**Dana:** Eric Olson's original note was a team decision, and the page is written for individuals. A short "if you lead a team" callout - like Pattern 09 has - would make it usable for managers deciding policy.

**Nate:** "When AI is in the synthesis loop, it earns the learning" is a great line. But synthesis across 40 documents is something I genuinely can't do myself in the time I have. The page should allow AI-assisted synthesis with a check: you summarize the result in your own words before using it.

**Proposed changes:**
1. Distinguish capabilities worth protecting from those fine to offload. (Isaac)
2. Note that the CEPR study is of secondary students; the professional extension is an inference. (Isaac)
3. Add a "which layer am I in" tell. (Fiona)
4. Add an "If you lead a team" callout, as Pattern 09 has. (Dana)
5. Allow AI-assisted synthesis with an own-words check. (Nate)
6. The study is now cited by name (done October 16). No change.

---

## Pattern 08 - Assemble the Team (Practice)

**Team:** Hugo Marchetti (adversarial) - organizational psychologist who argues simulated personas are not real diversity of thought; Sara Lindgren - product manager who runs the pattern weekly; Malik Evans - CISO; Rachel Tan - facilitator and meeting designer.

**Hugo (adversarial):** The whole pattern rests on AI personas producing genuine friction, but they're all the same model. They share its blind spots, its training, and its tendency to please you. Named roles help, but they don't create independent judgment. The page should say plainly: this is a rehearsal for real review, not a replacement for it, and the most important decisions still need real people. Otherwise it overpromises - which is ironic for a pattern built on the sycophancy problem.

**Sara:** I use this weekly and it works. The thing the page underplays is that the human's calls are the output - accepting and rejecting objections with reasons. Add a step: write down what you accepted and rejected. That's also how Ghost in the Workflow records red teams, so the two patterns connect.

**Malik:** For sensitive work, people will paste confidential strategy into a session to "assemble the team." Same data-handling line as Pattern 02.

**Rachel:** "Three to five voices" and "a mandatory adversarial voice" are the two rules that make it work; the page states the second only in the modal. Put both rules in the Solution text, not just in the copy-paste instructions.

**Proposed changes:**
1. State that the team is a rehearsal for real review, not a replacement - same model, shared blind spots. (Hugo)
2. Add a step to record what was accepted and rejected, and why - link Pattern 12. (Sara)
3. Add a data-handling caution. (Malik)
4. Put the "3-5 voices" and "mandatory adversarial voice" rules in the Solution text. (Rachel)
5. The OpenAI date is corrected to April 2025 (done October 16). No change.

---

## Patterns across the set

- **Data handling** came up on 02 and 08 (and applies to 05). Consider one standard line used across patterns.
- **Links to the newer patterns** (09, 11, 12, Redesign the Stream) would tie the older pages into the library - 04, 06, 08 each have a natural link.
- **Unsourced strong words** - "most common" (01), "dramatically" (02), "substantially" (04), "rarely works" (05), "more accurately" (03). The same pattern the value-facets report found.
