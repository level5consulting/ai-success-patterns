# Pattern 12 - Ghost in the Workflow

**Category:** Governance
**Status:** DRAFT - all sections written; full-pattern red team done and changes applied October 15, 2026. Not yet built as HTML.

**Subtitle:** The person who built your AI workflow understood it. They knew why the prompt was worded that way, what the agent was never supposed to touch, and which outputs needed a second look. Then they moved on, and the workflow kept running without them.

---

## Problem
**The builder did everything right - and it all lived in their head**

Picture the builder who does it well. Before building anything, they wrote down what success looked like (Pattern 01, Begin with the End in Mind). They gave the AI rich context about the business, the audience, and the constraints instead of a list of commands (Pattern 02, Onboard Don't Program). They tried to break it before trusting it, and tuned it around the failures they found (Pattern 03, Test Adversarially). Where numbers mattered, they had the model write code to calculate rather than calculate itself (Pattern 10, Models Are Not Good at Math). The agent works because of all that discipline.

Now ask where that discipline lives. The value statement is in a chat thread. The onboarding context is spread across forty prompt revisions. The red-team findings - the edge cases, the inputs that broke it, the step where a human must check the output - exist only in the builder's memory. So does the answer to a question nobody thought to ask: what systems and data the agent can reach, and why it needs that access.

Organizations have lost knowledge this way before, in undocumented spreadsheets, macros, and homegrown databases. What's different now is visibility. A spreadsheet's logic sits in its cells, where a successor can at least read it. An AI workflow's logic sits in its tuning history: the revisions, the rejected outputs, the conversations that shaped it. None of that is visible in the finished agent.

When the builder leaves, all of it leaves with them, and what stays behind is a ghost. The successor sees the output but not the reasoning. They can't tell a deliberate design choice from an accident, or a necessary permission from a leftover one. The obvious options are bad: keep running something they don't understand, or shut it down and lose the value it was producing.

The worst outcome is the one nobody chooses. The agent keeps running while the world changes underneath it. A data source is restructured, a policy changes, a field is renamed. Nothing errors out. The output stays plausible and quietly becomes wrong, and no one remaining knows which assumptions to check.

There's an irony here. AI is often sold as the way to capture institutional knowledge before it walks out the door. Poorly documented AI does the opposite: it creates a new category of institutional knowledge, buries it inside prompts and agent configurations, and loses it the same way organizations have always lost knowledge.

## Value
**AI assets that outlast the people who built them**

- **Cut the hidden cost of turnover.** Gallup estimates replacing an employee costs one-half to two times their annual salary, and part of that cost is the time it takes a replacement to become productive. For a $120,000 role, the total is $60,000 to $240,000. When the departing person's AI work documents itself, the successor inherits working knowledge instead of reverse-engineering it, which shortens that ramp. (Source: https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses-trillion.aspx - 2019; $120K is illustrative.)
- **Catch silent drift before it costs you.** Documented assumptions let a successor see which data, policies, and dependencies an agent relies on, and check them when they change.
- **Inherit an asset, not a liability.** The successor can change, improve, or retire the workflow with confidence, instead of choosing between blind trust and starting over.
- **Keep access defensible.** Every AI asset has a named owner who can explain what it reaches and why, so permissions can be reviewed rather than left in place.
- **Stay free to change models.** When an AI workflow documents its purpose, inputs, prompts and owner outside any one tool, you can move it to a different model without rebuilding it from memory.

## Context
**When this pattern applies**

This pattern applies from the moment anyone other than the builder depends on an AI asset. That includes agents running on a schedule or triggered by events, prompts a team reuses, chat workflows built into how a process gets done, and any AI that touches business systems or data. The test is simple: if the builder disappeared tomorrow, would someone need to understand this?

It applies most urgently in three situations:

- **Agents that act on their own.** An agent that writes to systems, sends messages, or moves data does more damage when misunderstood than a prompt someone runs by hand.
- **Workflows that grew up informally.** A personal experiment becomes something the team relies on, and it never gets a second look on the way.
- **Organizations in motion.** Reorganizations, turnover, and role changes are when ghosts are made. The builder rarely leaves through a planned handoff.

It does not apply to throwaway work. A one-off chat to draft an email doesn't need a record. The line is reuse and reliance, not effort.

And it applies before the builder leaves, not after. Documentation written during the work captures the reasoning while it's fresh and visible. Documentation reconstructed after the fact captures only what the successor can guess.

## Solution
**Make documentation part of the AI's job**

The fix is the thing that makes this problem different from every undocumented spreadsheet before it: the AI can document its own work. Instead of asking the builder to write it all down afterward, make documentation part of the AI's job description from the start. The AI produces the work, and it produces the record that explains the work.

**Step 1: Write documentation into the job description**

When you onboard the AI (Pattern 02), add a standing constraint: every output that others will rely on comes with a record a stranger could follow. For example:

> As you build and refine this workflow with me, maintain a running record for whoever inherits it. Capture what it does and why, the decisions we made and the alternatives we rejected, the assumptions it depends on, the systems and data it can access and why, the failures we found in testing, and the points where a human must check the output. Update the record whenever we change something. Write it for someone who wasn't in this conversation.

The builder doesn't write the documentation, but a human must review it. Treat the record as a draft, the same way you treat the AI's work. AI describes what it believes it did, which isn't always what it actually does.

**Step 2: Scale the record to the risk**

Not every AI asset needs the same record. Match the depth to how much damage a misunderstanding could do.

A **lite record** is enough for reusable prompts and chat workflows that a person runs by hand. It covers four things: what it's for, the key assumptions it depends on, where a human must check the output, and who owns it.

A **full record** is required for agents that act on their own, write to systems, or touch sensitive data. It answers every question a successor will have:

- **Purpose and success.** What it's for and what good output looks like (Pattern 01).
- **Context and design choices.** What the AI was told, and why it was built this way rather than another way.
- **Assumptions and dependencies.** Which data sources, policies, fields, and upstream processes it relies on. This is the list to check when something changes.
- **Access and permissions.** What systems and data it can reach, and why each one is needed. A human verifies this against the actual system configuration - the AI knows what it was told it can reach, not necessarily what it can.
- **Known failures and human checkpoints.** What broke during testing (Pattern 03), and where a person must verify before the output is used.
- **Owner and successor.** Who is accountable now, and who would take over. The named successor is the one who watches for triggers - especially the owner changing role, since the owner is the one leaving.
- **Retirement.** The conditions under which it should be retired, what access to revoke, and what depends on it downstream.

**Step 3: Keep the record with the work, not in the chat**

A record inside a chat history is still a ghost. Store it alongside the agent, prompt, or workflow it describes, wherever the team already keeps shared work, and version it with every change. If someone can find the agent, they can find its record.

If you build in a chat tool, make it a habit: at the end of each working session, have the AI output the updated record as a file, and save it next to the workflow.

Protect the record like the system it describes. A full record maps what an agent can reach and why, which makes it useful to an attacker. Give it the same access controls as the agent itself.

**Step 4: Test the record with someone who didn't build it**

Hand the record to a colleague who wasn't involved and ask them three questions. What does this do? What would you check if the main data source changed? Is it safe to change, and how would you know? If they can't answer, the record isn't done. This is Pattern 03 applied to the documentation itself.

**Step 5: Review the record when the world changes**

Set triggers, not just dates: the owner changes role, a data source or system is restructured, a policy the workflow depends on changes, or the output starts to look off. Each trigger means opening the record, checking its assumptions, and updating it. That's how silent drift gets caught. Sometimes the answer is that the workflow is no longer needed - and the record's retirement section says what to revoke and what will break when it goes.

## Notes

**The scale is about to change.** Gartner forecasts that by 2028 the average global Fortune 500 enterprise will have more than 150,000 AI agents in use. Every one of them has a builder who will eventually move on. Gartner's own guidance on agent sprawl calls for a central inventory and lifecycle rules. An inventory tells you an agent exists; the record tells you what it's for. This pattern supplies the part an inventory can't. (Verified: https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartner-identifies-six-steps-to-manage-artificial-intelligence-agent-sprawl)

**Most of the conversation is about access.** Security writers call these "orphaned agents" and focus on credentials that outlive their owners. That risk is real, and it's why access is part of every record. But the deeper problem is understanding. You can't right-size an agent's permissions, or safely retire it, if nobody knows what it's for.

**Related patterns.** This pattern preserves the work of Patterns 01, 02, 03 and 10. It is the mirror image of Embed the Expert (coming soon): Ghost in the Workflow is what happens when knowledge gets trapped in AI by accident; Embed the Expert captures it on purpose.

## Research notes (not for publication)

- Mirror relationship with Pattern 14, Embed the Expert: 12 is the failure mode, 14 is the deliberate practice.
- Link to AI tool sprawl: orphaned agents are sprawl's long tail. Possible figures, to verify against originals before use: Gartner forecast of 150,000+ AI agents per Fortune 500 company by 2028 (Gartner press release, April 28, 2026, cited secondhand in No Jitter, https://www.nojitter.com/ai-automation/why-you-need-a-retirement-plan-for-orphaned-ai-agents); Cloud Security Alliance finding that only 15% of organizations have near-full agent ownership (cited secondhand by 1Kosmos, https://www.1kosmos.com/resources/blog/ghost-agent-problem-employees-leave-ai-agents-keep-running).
- Industry framing: security vendors call these "orphaned agents" or the "ghost agent problem" and treat it as an access problem. This pattern covers the understanding problem underneath it. No named real-world incidents found as of October 15, 2026 - published examples are hypothetical.
- No "Inspired by" source - Greg confirmed none.

## Open decisions

- **Existing ghosts (Marcus, red team 2) - TBA.** How to handle AI assets that are already orphaned (e.g., AI reverse-engineers a draft record from the prompt, config, surviving chat history, and sample outputs). Greg: TBA - he wants to apply this pattern retroactively to everything already created, and make it a standard practice going forward. See BACKLOG.md.
- Five Solution steps kept (Claude's recommendation); sample constraint kept - pending Greg's explicit confirmation.

## Previous open decisions

- Keep five Solution steps, or merge Steps 4 and 5 into "test and maintain"?
- Is the sample constraint in Step 1 the right length and tone for the site?

## Red team log

- **October 15, 2026 - Problem and Value** (Assemble the Team: Dana Whitfield, CIO/adversarial; Marcus Oyelaran, EPMO director; Priya Raman, CISO; Tom Kessler, citizen developer). Applied: made AI-specific difference explicit - tuning history is invisible, and AI can document itself (Dana); quantified turnover cost in Value (Dana); added silent drift and successor confidence (Marcus); added access and permissions to Problem, Value, and the record (Priya). Not applied: Dana's critique that the "builder did everything right" framing flatters the reader - Greg kept it. Tom's concern about documentation burden is addressed by AI-generated documentation.
- **October 15, 2026 - Full pattern** (same team). Applied: softened the Gallup ramp-up claim (Dana); human review of the AI-written record made explicit, and access verified by a human against actual configuration (Dana, Priya); retirement added to the record and to Step 5 (Priya); lite vs full record scaled to risk (Tom). Deferred (TBA): handling existing ghosts (Marcus) - see BACKLOG.md. Follow-up decisions (Greg): the named successor watches the triggers (Marcus); access controls on the record itself (Priya); chat-tool tip - AI outputs the record as a file at the end of each session (Tom). All applied.
