# Pattern 21 - Redesign the Stream, Not the Role

**Category:** Governance (matches the Coming Soon card)
**Maturity level:** Leadership (Greg, October 16, 2026)
**Status:** DRAFT 2 (overnight, October 28-29, 2026) - Greg's answers applied October 27; red-teamed October 27-28 (records/red-team-21.md); all 9 accepted calls applied. Not built as HTML.

**Where it came from:** Sandra Loughlin, PhD, LinkedIn post, October 2026 (sources/sandra-loughlin-value-stream-redesign.md) - Greg agrees "wholeheartedly." Sandra is OK with credit on the site (Greg, October 19, 2026, for Pattern 06); confirm it covers this page. Paraphrase only.

**Lead (draft):** Most AI work redesign starts with roles: what can AI do for the analyst, the coordinator, the estimator? Business value doesn't live in roles. It lives in value streams - the work that crosses roles from request to result. Map the stream first, put AI where it moves the whole flow, and redesign the roles last.

---

## Problem
**Faster people, same slow process**

We used AI to answer RFP questions, and it was great - that part got much faster. But it did nothing for the reviewers, and the answers still waited on them. Until we automated that part of the stream too, it barely moved our overall turnaround time.

Ask an organization how it plans to use AI and you'll usually hear a list of roles. AI will help the analysts write reports, the coordinators schedule, the estimators price. Each team gets a tool, each person gets faster, and leadership waits for the results to show up in the business.

They often don't. Business value comes out of value streams - the end-to-end flow from a customer's request to its result, crossing roles, teams and often locations. Make one step in that flow faster and, unless that step was the constraint, the work just waits longer at the next one. The analyst writes the report in an hour instead of a day, and it sits in an approval queue for a week like it always did.

Role-first redesign also misses what holds the stream together: the handoffs, the re-keying, the person everyone calls because they know how it really works. None of that belongs to one role, so no one's AI tool touches it.

None of this is new. Lean teams have mapped value streams for decades. What's new is the temptation AI creates to skip the map and hand everyone a tool.

The failure isn't using AI inside roles. It's starting there - and expecting faster roles to add up to a faster business.

## Value
**AI that moves the result, not just the task**

- **Gains that reach the business** - cycle time, throughput and quality improve for the whole stream, not just one step.
- **AI goes where the constraint is** - effort lands on the step that's actually holding the work up, then the next one.
- **The invisible work gets seen** - handoffs, workarounds and tacit knowledge show up on the map, so they get fixed or protected instead of broken.
- **Something to show in the first 30 days** - one stream mapped, one constraint named, and an end-to-end baseline to measure against. That's a result a leader can report before any role changes.
- **The people who do the work help redesign it** - they map the stream with you; they're part of the redesign, not its subject.
- **Roles that fit the new work** - roles are redesigned around what people still need to do, with the skills that work needs, instead of guessed at up front.
- *Measure it:* end-to-end cycle time and throughput for the stream, before and after; how much of a single step's time saving shows up in the end-to-end result.

---

## Context (first pass)
**When this pattern applies**

Use it when an organization is planning AI-driven work redesign, an operating-model change, or role changes tied to AI - and when AI tools are already deployed but the business results haven't followed.

It fits work that crosses roles and teams: order to cash, quote to contract, intake to delivery, hire to productive, incident to resolution. The more handoffs, the more it matters.

It is slower to start than handing out tools by role, so it isn't the first thing to do with a single team trying AI for the first time. Start it with one stream and a small team, not the whole company.

## Solution (first pass)
**Map the stream, put AI in the flow, then redesign the roles**

**Step 1: Pick one value stream and map it end to end.** From the request to the result. For each step: who does it, how long it takes, how long work waits before it, and what gets handed off or re-entered. Mark the human glue - the workarounds and the people who make it work - and the steps that need real judgment. Map it with the people who do the work. A rough estimate from them is enough to start; you don't need a data project.

**Step 2: Find the constraint.** Where does work wait longest? On the floor, it's where work piles up or people wait. That's where AI effort pays first. Speeding up a step that isn't the constraint mostly builds a bigger queue at the next one.

**Step 3: Redesign the flow with AI in it.** Use AI to automate what can be automated and to support the judgment steps - starting at the constraint. A round is done when the end-to-end measure moves - then find the next constraint and do it again. A moved bottleneck is progress; it tells you where to go next.

**Step 4: Iterate until the flow is good enough for now.** Run the new flow with a small team for a few cycles and measure the whole stream, not one step.

**Step 5: Then redesign the roles.** Look at the human work that's left. Group it into roles that make sense, name the skills each needs, and match people to them - training where the gap is. The people in the stream see the new flow before their role changes, and skill gaps get training, not just a new org chart. Roles come last because you can't design them until you know the work.

---

## Notes (planned)
- **Tiger teams:** start with one or two small teams on one stream - faster, a safe place to test new incentives and roles, and it avoids pushing change on everyone at once. (From Sandra's post - covered by the Inspired by credit.)
- **Pattern 04 link (Greg, October 27, 2026):** Pattern 04's Context already points here ("Fix the stream first, then automate what's left"); the link goes live when 21 publishes.
- **Data is the hidden barrier:** mapping the stream usually shows that the data feeding it is the biggest obstacle - and the biggest unlock. Link to Pattern 18, Avoid the Naughty List.
- **Squares with Greg's bottleneck rant:** the rant says moving the bottleneck is what improvement looks like. This pattern agrees - and adds that you have to know where the bottleneck is, which is why you map the stream first.
- **Greg's example (October 27, 2026):** the RFP story - now the opening of the Problem.
- **Connections:** Pattern 13, Automate the Invisible (the invisible work on the map); Pattern 11, The Productivity-to-Headcount Trap (faster roles read as fewer people); Pattern 14, Embed the Expert (the tacit knowledge the map finds); Pattern 18, Avoid the Naughty List (data); Pattern 16, The Staged Journey.
- **Bigger use (Greg, October 16, 2026):** this pattern is step 1 of the planned "For organizations" page - the Level 5ive engagement model.

## Use this pattern (first pass)
*Paste this into any AI system's custom instructions or at the start of a conversation to run Pattern 21.*

```
# Redesign the Stream, Not the Role

You are running Pattern 21: Redesign the Stream, Not the Role from AI Success Patterns (aisuccesspatterns.com/patterns/21-redesign-the-stream-not-the-role.html).

The pattern's premise: business value lives in value streams - end-to-end work that crosses roles - not in individual roles. Map the stream first, put AI where it moves the whole flow, and redesign roles last.

## Phase 1 - Pick the stream
Ask the user, in one question, which end-to-end process to look at, from request to result. If they name a role or a tool instead, ask which process that role or tool sits in.

## Phase 2 - Map it
Walk the stream step by step. For each step ask, one question at a time if needed: who does it, how long the work takes, how long it waits before this step, and what gets handed off or re-entered. If the user has process documents, tickets or reports, offer to draft the map from them for the user to correct. Show the map as a short table. Accept rough answers ("about a day") and mark them [Estimate - confirm] - don't stall. Mark steps that depend on one person's know-how and steps that need real judgment.

## Phase 3 - Find the constraint
Point to the step where work waits longest and say why it's the likely constraint. Mark any time you estimated rather than were told as [Estimate - confirm]. Explain in one line why speeding up other steps first would mostly build a queue.

## Phase 4 - Redesign the flow
For the constraint, propose how AI could automate or support the work, and what the person still decides. Then say where the constraint would likely move next. Suggest a small team to run the new flow for a few cycles and the end-to-end measure to watch.

## Phase 5 - Roles last
Only after the flow is redesigned, list the human work that's left and suggest how it might group into roles, with the skills each needs. Remind the user that roles come last and should be revisited after the flow has run.

## Behavior rules
- One question at a time
- Start from the stream, never from a role
- Don't invent times or volumes - ask, or mark estimates
- Measure the whole stream, not one step
- Stop after the redesign and the role sketch; the user decides
```

---

## Inspired by
Sandra Loughlin, PhD - her argument that AI work redesign should start from the value stream, not the role, and that roles are redesigned last (credit approved by Greg, October 27, 2026; Sandra OK with credit on the site, October 19, 2026). Paraphrase only.

## Sources
- Sandra Loughlin, PhD, LinkedIn post (sources/sandra-loughlin-value-stream-redesign.md) - idea source; paraphrase only.

## Questions for Greg - answered October 27, 2026
1. Sandra: add the Inspired by credit - done.
2. Pattern 04 link: OK to go live when 21 publishes.
3. Example: the RFP answers - in Notes.
4. Maribeth: leave out - removed.
5. Red team approved - ran overnight October 27-28.

## Original questions
1. **Credit Sandra.** Her post is the idea source, and she's OK with credit on the site (October 19). Add an "Inspired by" credit here too?
2. **Pattern 04 link.** Pattern 04's Context already says "Fix the stream first, then automate what's left (see Redesign the Stream, coming soon)." When 21 publishes, that link goes live - OK?
3. **Your example.** An EPMO or JCI story where speeding one team did nothing because the work waited elsewhere, or where mapping the flow showed the real constraint.
4. **Maribeth.** Mention her "humans as middleware" point (with her consent), or leave it out?
5. **Red team.** Proposed team: **Diane Walsh (adversarial)** - CHRO under pressure to show AI savings by role this quarter, who thinks stream mapping is a consultant's way to bill more hours; **Ray Kowalczyk** - operations VP who owns order to cash; **Priti Nair** - process excellence lead (Lean Six Sigma black belt); **James Ortiz** - frontline estimator whose role would change. Approve or swap?
