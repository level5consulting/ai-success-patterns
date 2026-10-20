# AI Success Patterns - Backlog

Lower-priority site work, kept here so nothing is lost between sessions. Each item carries its full context so it can be picked up cold.

**Rule:** when an item is added, record what it is, why it matters, who raised it, any decisions or constraints already discussed, and open questions. Not just a title.

---

## 1. UI redesign

- **What:** A redesign of the aisuccesspatterns.com site.
- **Raised by:** Jeff Toppall (contributor).
- **Why:** Jeff recommended it in his feedback to Greg. His specific concerns with the current design were not recorded - capture them next time Jeff is consulted.
- **Constraints / known decisions:**
  - Greg prefers light color schemes.
  - Keep the established category tag colors, including `.tag-gov` (purple, `#6B3A8C` light / `#B07AD4` dark) for Governance.
  - Greg prefers a fresh redesign over incremental patching when direction shifts significantly.
  - `main` is live - redesign must be built on a branch and approved by Greg before merging.
- **Open questions:** What specifically did Jeff want changed (navigation, typography, layout, pattern page structure)?
- **Status:** Not started.

## 2. Red team published patterns 01-07 with Assemble the Team (superseded by item 7)

- **What:** Run each of patterns 01-07 through the Assemble the Team red-team process, as was done for 09-11.
- **Raised by:** Greg.
- **Why:** Patterns 09-11 went through the full workflow (Build - Red team - Iterate - Commit) and improved as a result. 01-07 were published before that step existed, so they haven't had the same scrutiny.
- **Constraints / known decisions:**
  - Apply current conventions while revising: section order Problem - Value - Context - Solution - Notes; regular dashes, no em dashes; "Inspired by" prose attribution, no direct quotes.
  - Pattern 08 (Assemble the Team) is the pattern itself and is not in scope.
  - Changes go on a branch; Greg approves before merge.
- **Related:** Patterns 01-05 still have leftover `.md` drafts next to their `.html` pages (06-11 are HTML only). Decide whether to delete or keep them during this pass.
- **Status:** Not started.

## 3. Add more quoted sources

- **What:** Add more sourced material to patterns, systematically across the site.
- **Raised by:** Jeff Toppall (contributor).
- **Why:** Jeff recommended more quoted sources to strengthen the patterns' credibility.
- **Constraints / known decisions:**
  - **Tension to resolve:** current convention is "Inspired by" prose attribution with **no direct quotes** (e.g., the Kent Beck quote was removed from Pattern 09). Decide whether "quoted sources" means adding direct quotes, adding more cited/attributed sources in prose, or a references section.
  - Origin material is preserved in `sources/` (Kent Beck, Eric Olson, Justin MacBale, Shubham Dwivedi, Chris Gallivan).
- **Status:** Not started - needs a decision on the quoting approach first.

## 4. Contributor outreach - Shubham Dwivedi and Chris Gallivan

- **What:** Reach out to Shubham Dwivedi and Chris Gallivan as contributors.
- **Raised by:** Greg.
- **Why:** Both already have source material in the repo:
  - Shubham Dwivedi: `sources/shubham-dwivedi-iterate-to-destination.md` - validates the Iterate to the Destination pattern.
  - Chris Gallivan: `sources/chris-gallivan-ai-reads-tools-copy.md`.
- **Open questions:** What is the ask (credit/permission, review, co-authoring a pattern)? Which patterns does each tie to?
- **Status:** Not started.

## 5. Add a Governance filter tab to the index

- **What:** Add a "Governance" button to the category filter row on `index.html` (alongside All, Conversational, Agentic, Accuracy), with an `active-gov` style using `--tag-gov` / `--tag-gov-fg` and a matching branch in `filterPatterns()`.
- **Raised by:** Claude, October 15, 2026; Greg approved fixing it.
- **Why:** Governance is now a category (Pattern 11 in review, Pattern 12 next), but the filter row has no tab for it.
- **Why it's waiting:** The filter tabs only apply to the **published** patterns grid. None of 01-08 are Governance, so a tab added now would show an empty list. Add it in the same commit that publishes the first Governance pattern (likely Pattern 11).
- **Status:** Deferred until first Governance pattern publishes.

## 6. Apply Ghost in the Workflow retroactively, and make it standard practice (scope answered by item 7)

- **What:** Go back through everything already created and give it a Ghost in the Workflow record, then make the record a standard step for all new work.
- **Raised by:** Greg, October 15, 2026, in response to Marcus Oyelaran's red-team point on Pattern 12 (the pattern prevents new ghosts but does nothing for ghosts that already exist).
- **Greg's words:** "TBA since I will want to go back and do this for all the patterns created go backwards and this pattern becomes a thing we do going forward."
- **Open question - scope (confirm with Greg):** "All the patterns created" could mean (a) the AI assets behind the site, such as the Assemble the Team, LLM Interview, Test Adversarially, and Session Start skills, (b) the pattern pages themselves, or (c) both.
- **Going forward:** Likely adds a step to the pattern workflow (Build - Red team - Iterate - Commit - Add card). Where the record step sits is undecided.
- **Related content gap:** Pattern 12 currently has no guidance for existing ghosts. Marcus's suggestion: AI reverse-engineers a draft record from the prompt, agent config, surviving chat history, and sample outputs, and flags what it can't determine. Could become a section of Pattern 12 or a follow-on pattern once Greg decides.
- **Status:** TBA - Greg will return to it.

## 7. Pattern walkthrough - new sequence, red team, and Ghost in the Workflow record for every pattern

- **What:** Walk through every pattern (01-12), one at a time: (1) reorder sections to Problem - Value - Context - Solution - Notes, editing transitions so it reads naturally; (2) red team with Assemble the Team where not already done, and apply Greg's calls; (3) write a record; (4) commit on a branch, publish on Greg's approval.
- **Raised by:** Greg, October 15, 2026. Supersedes item 2 (red team 01-07) and answers item 6 (apply Ghost in the Workflow retroactively).
- **Audit, October 15, 2026:**
  - Old order (Context - Problem - Solution - Value Consequence - Notes): 01, 02, 03, 04, 05, 06, 07, 08.
  - Out of order (Value - Problem - Context - Solution - Notes): 09.
  - Correct order: 10, 11, 12.
  - Maturity levels: published on all 12 (item 8).
  - Red-teamed: 09, 10 (Greg confirmed; details never captured), 11, 12. Not red-teamed: 01-08.
  - Records: none yet (12's draft .md has a red-team log).
- **Order:** Claude proposed published patterns first (01-05, 08), then 06, 07, 09, 10. Not yet confirmed by Greg.
- **Record contents (agreed October 15, 2026):** One record per pattern, internal (not shown on site), e.g. `records/NN-name.md`:
  - Purpose - the problem it names and the value it delivers
  - Idea providers - who, and credit/permission status
  - Feedback providers - who, and what they contributed
  - Sources - for every quote and figure, flagged verified/unverified
  - Red-team reviews - date, team, what was applied, what was rejected and why
  - Decisions and rejected framings - with the reason
  - Status and open questions
  - Connections - related patterns, dependent backlog items, companion skill if any
  - Maturity level - see item 8 (once a model is chosen)
- **Greg's test for the record:** Is it a good list to hand to someone if Greg leaves the project?
- **Overnight run, October 15, 2026 (branch `overnight-2026-10-15`, awaiting Greg's review):** records written for all 12 (`records/`); patterns 01-09 reordered (01 and 02 Value converted to bullet format; 07 study citation added; 10 In Review tag added); README, CONTRIBUTING, and home page modal updated to the new structure; source verification done (`records/source-verification.md`).
- **Still to do per pattern:** Greg's read, then red team (01-08 have none recorded).
- **Status:** Drafts done; review and red teams pending.

## 8. Maturity ranking for each pattern

- **What:** Give every pattern a maturity ranking showing who it's for - e.g. beginners, practitioners, or experts.
- **Raised by:** Jeff Toppall (recalled by Greg, October 15, 2026).
- **Constraint:** Greg is not sure he wants a 1-5 maturity model. Open to a different model.
- **Model chosen (Greg, October 15, 2026):** Foundation / Practice / Leadership. Rejected: 1-5 maturity model; beginner/practitioner/expert labels (they rank the reader - senior leaders avoid "beginner"). Also considered: Individual/Team/Organization scope, Shu-Ha-Ri.
- **Definitions:**
  - **Foundation** - habits anyone using AI needs, at any seniority; they apply in a single working session.
  - **Practice** - making AI a repeatable part of how work gets done; builds on the Foundation habits.
  - **Leadership** - decisions about people, investment, and governance that shape how a whole organization uses AI.
- **Rankings (confirmed by Greg, October 15, 2026):**
  - Foundation: 01 Begin with the End in Mind, 02 Onboard Don't Program, 03 Test Adversarially, 05 Avoid AI Slop with an LLM Interview, 10 Models Are Not Good at Math
  - Practice: 04 The AI Operations Manager, 06 AI as Amplifier, 07 Own the Thinking, 08 Assemble the Team
  - Leadership: 09 The Compressed Apprenticeship, 11 The Productivity-to-Headcount Trap, 12 Ghost in the Workflow
  - Judgment calls Greg settled: 06 Practice (not Foundation), 07 Practice, 09 Leadership, 12 Leadership.
- **Rule:** One level per pattern (no "Foundation - Practice" ranges), for simplicity.
- **Observation:** All published patterns are Foundation or Practice; every Leadership pattern is still In Review. For a site aimed at EPMO and AI leaders, publishing 11 or 12 gives leaders something at their level.
- **Open questions:** Show on the site now (small tag) or wait for the UI redesign? Rank Coming Soon cards too? Level goes into each pattern's record during the item 7 walkthrough.
- **Published October 15, 2026:** Level tag (gray outline, three-bar icon) on library cards, In Review cards, and every pattern page header; level key with one-line definitions above the library grid. Not shown on Coming Soon cards (levels may change before those patterns are written).
- **Not done:** Level filter buttons - not chosen; revisit once a Leadership pattern is published (same timing as the Governance filter tab, item 5).
- **Rule going forward:** every new pattern gets a level when it is carded.
- **Status:** Done.

## 9. Jeff Toppall phone-call feedback (October 14, 2026) - deep dive still needed

- **Source:** Rough notes from a phone call between Greg and Jeff Toppall, October 14, 2026. Recovered from Greg's project notes on October 15 - they had not made it into this backlog.
- **Next step:** A full deep-dive conversation with Jeff is still needed; these are phone notes only.
- **Points raised by Jeff (each needs a decision):**
  - **Value statement up front on the homepage** - at hero level, so visitors know immediately what the site gives them.
  - **Cite MIT and McKinsey reports on value realization** - real-world citations and quotes throughout. Related: item 3 (quoted sources) and its tension with the no-direct-quotes convention.
  - **Frame Pattern 01 from success,** not just problem and solution.
  - **Better look and feel overall.** Related: item 1 (UI redesign).
  - **Reconsider pattern numbering as the organizing principle** - should the library be organized by impact instead?
  - **Maturity model across patterns** - DONE as item 8 (Foundation / Practice / Leadership).
  - **Third parties in AI value realization** - vendors, partners, and other outside parties play a role; the patterns should represent that.
  - **Remove em dashes site-wide** - DONE (site and README).
- **Status:** Open. Deep dive with Jeff not yet scheduled.

## 10. Test the new section order on one pattern before restructuring all (David Krause)

- **What:** Before reordering every pattern into Problem - Value - Context - Solution - Notes (item 7), test the new order on one pattern page, gather feedback, then decide.
- **Raised by:** Red team on October 14, 2026, using David Krause's framing: test the hypothesis on one page, watch what happens, then decide.
- **Why it matters now:** Item 7 currently plans to reorder all of 01-09. Patterns 10, 11, and 12 already use the new order and could serve as the test. Decide whether the test has happened (and what the feedback was) before starting item 7.
- **Resolved (Greg, October 15, 2026):** Patterns 10-12 served as the test. Greg loves the new format and wants all patterns converted.
- **Status:** Closed.

## 11. Kent Beck contributor credit on the three humanistic AI patterns

- **What:** Kent Beck receives contributor credit on all three humanistic AI patterns when they move to In Review: The Compressed Apprenticeship (09), Think Together, Not Alone, and Give Back the Good Work.
- **Decided by:** Greg (recorded October 14, 2026).
- **Credit style:** Same contributor block style as Justin J MacBale on Pattern 03.
- **Current state:** Pattern 09 credits Kent Beck through an "Inspired by" block (his direct quote was removed - commit ea0bf8b). Think Together, Not Alone and Give Back the Good Work are still in Coming Soon.
- **Open question:** Confirm whether Pattern 09's current "Inspired by" block meets this, or should match the MacBale contributor style.
- **Source material:** `sources/kent-beck-compressed-apprenticeship.md`.
- **Status:** Apply as each pattern moves to In Review.

## 12. Strategic retrospective - connecting the site to speaking and consulting (October 15, 2026)

- **Greg's end goal:** Make the practice better, and use this work to get on the conference circuit and win consulting engagements.
- **Greg's read of the retrospective:** Moving in the right direction, with a long way to go.
- **Gaps Claude identified:**
  - The site serves practitioners; the buyer is a leader. All published patterns are Foundation or Practice; every Leadership pattern is still In Review.
  - No bridge from the public-domain library to what Level 5ive sells (GO Framework, Fractional Chief AI Evangelist).
  - Evidence is thin - few patterns have a real client story; Greg's Planview, JCI, and Daptiv experience is barely on the site.
  - Nothing is pointed at a stage - no talk abstract, no target conference list or submission deadlines; the speaker one-pager's topics are about SPM investment, not the patterns.
  - Time is going to site hygiene rather than demand generation.
- **Suggestions Claude made (not yet decided by Greg):**
  - Publish the Leadership patterns (11, 12) before the full walkthrough; timebox the walkthrough.
  - Add a "For organizations" section mapping patterns to the GO Framework and the Fractional Chief AI Evangelist offer.
  - Write one signature talk now (e.g. governance talk for EPMO leaders from 11 and 12, opening with the self-inflicted ghost story from October 15).
  - Target three or four PMO and SPM conferences with upcoming submission deadlines.
  - Pair each Leadership pattern with a real, anonymized Planview or JCI story.
  - Track signal: inbound DMs, speaking invites, consulting conversations that mention the site.
- **Signal log** (priority 9 - who is responding to the patterns):
  - October 15, 2026 - **Joe Bitter** was very interested and took lots of notes on specific patterns (shared by Greg). Patterns he liked most: **05 Avoid AI Slop, 08 Assemble the Team, 12 Ghost in the Workflow** (Greg, October 16, 2026).
  - October 16, 2026 - **Sandra Loughlin, PhD** (EPAM) commented on Greg's LinkedIn post about the patterns: "dude, this is AWESOME." Also the source of Redesign the Stream, Not the Role. Greg replied to her October 16, 2026 (contributor conversation opened).
  - October 16, 2026 - Greg: people are really getting behind the patterns idea. Signal favors a patterns-led talk over a governance-led one.
- **Conference strategy (Greg, October 16, 2026):** Start "off Broadway" - IT conferences and IT days, presenting for free as practice. Regions: southeast Wisconsin, La Crosse, Minneapolis-St. Paul, Louisville (expanded October 16, 2026). Include AmFam DreamBank in Madison. Venue research in project doc `talks/speaking-venues.md` (overnight run, October 16). Larger PMO/SPM/AI-governance stages later, once evidence and stories are ready. Talk abstract v3 is in the project doc `talks/ore-is-not-gold-abstract.md`.
- **Talk story to keep:** On October 15, 2026, the handoff note misstated what was published, Pattern 10's red team left no trace, and backlog items from October 14 were nearly lost - Ghost in the Workflow happening to its author.
- **Priority order (accepted by Greg, October 16, 2026)** - also shown on the dashboard's Backlog tab:
  - **Tier 1 - directly produces talks and engagements:** (0, added Oct 18 - top priority) build The Night Shift pattern; (1) publish Leadership patterns 11-13; (2) signature talk abstract, "ore is not gold" thesis, credit Kent Beck; (3) target conference list; (4) "For organizations" page; (5) homepage value statement (Option A, credit Kent Beck).
  - **Tier 2 - makes them land:** (6) real stories for Leadership patterns; (7) value-facets run; (8) contributor outreach; (9) track signal.
  - **Tier 3 - site quality, timeboxed:** build queue; red teams 01-08; "Use this pattern"; Jeff deep dive; Kent Beck credit on humanistic patterns; UI redesign; quoted sources; existing ghosts.
- **Publishing cadence (Greg, October 16, 2026):** No more than 2 patterns published per week. Week of October 12, 2026: 2 already published (12 and 13 to In Review), so item 1 (publish Leadership patterns) waits for next week. **Decided (Greg, October 16, 2026): Pattern 12, Ghost in the Workflow, publishes Monday, October 19, 2026** - on the strength of Joe Bitter's response. It is the first Governance pattern published, so the Governance filter tab (item 5) goes live in the same commit.
- **Status:** Priorities set. Working Tier 1 - starting with item 2 (signature talk) because item 1 is held by the publishing cadence.

## 13. Value has many facets - review and quantify every pattern's Value section (David Viney)

- **What:** Review the Value section of every pattern against the idea that value has many different facets, not one. Then quantify each facet where possible.
- **Raised by:** David Viney commented on **waste savings** as a form of value. Greg extended the idea (October 16, 2026): waste savings is one facet, and value has many more. The multi-facet framing is Greg's; David's contribution is the waste-savings starting point.
- **Source text:** **Not yet captured.** David's original comment (waste savings) - Greg to paste if he wants it saved in `sources/`. Platform, date, and which post it was on: not yet captured.
- **Greg's intent:** "Something to look at in our value statements." Greg suggested an overnight run to quantify them.
- **Why it matters (Claude's notes, not yet discussed):**
  - Most Value sections today are qualitative ("drops substantially," "shrinks dramatically"). Only Pattern 12 has a dollar figure (Gallup turnover cost).
  - Ties to the GO Framework's AI Value thinking - the board's two love languages (profitability and strategy) and the lampshade problem of hidden costs.
  - Ties to Jeff Toppall's ask to cite MIT and McKinsey reports on value realization (item 9) and to the source-verification report.
- **Possible overnight run (to confirm with Greg):** For each pattern, (1) tag each Value bullet by facet, (2) find a credible published figure or a defensible way to measure it, (3) flag bullets that can't be quantified honestly. Output as a report and proposed edits on a branch - no live changes.
- **Facets (confirmed by Greg, October 16, 2026):**
  1. Waste savings (David Viney) - rework, duplicated effort, iterations eliminated
  2. Time and speed - faster cycle times and decisions
  3. Cost avoidance - mistakes, rehiring, reversals that never happen
  4. Quality and accuracy - fewer errors reaching decisions
  5. Risk reduction - exposure, compliance, security
  6. Capability - people getting better, not just faster
  7. Trust and credibility - with stakeholders, boards, customers
  8. Strategic value - growth and capacity redirected to what matters
- **Expected finding (Claude's hypothesis):** most current Value bullets fall under 2 and 4; few touch 3, 5, or 8 - the facets boards care about most.
- **Open questions:** Quantify with external figures, measurement guidance ("how you would measure this"), or both? All 12 patterns, or published ones first?
- **Status:** Report ready for Greg's review - `records/value-facets-report.md` (overnight, October 16-17, 2026). Proposed edits not applied.

## 14. Standard practice for every new pattern (Greg, October 16, 2026)

- **Live red teams:** Every new pattern gets a live red team with Greg in the session (Assemble the Team, mandatory adversarial voice). Overnight red teams are only for catching up on patterns that were overlooked (01-08).
- **Ghost in the Workflow applied:** Every new pattern gets a record in `records/` from its first draft, updated at each red team, decision, and status change. Pattern 13 is the first.
- **Workflow becomes:** Build - Record - Live red team - Iterate - Update record - Commit - Add card to In Review.
- **Pattern dashboard:** "AI Success Patterns Tracker" (claude.ai artifact https://claude.ai/artifact/US9gRCg21pVwqb9co6MumM, created October 16, 2026). Shows every pattern's status, category, level, red team, record, queue position, and next step from an attached `patterns.json`. **Update it whenever a pattern changes status, gets red-teamed, or the build queue changes** - upload a new `patterns.json` and point the dataset at it.
- **Nightly run also preps the next pattern in the queue** for Greg's live red team the next morning (draft, record, sources, questions - no red team).

## 15. Add "Use this pattern" instructions to more patterns

- **What:** Give more pattern pages the "Use this pattern" modal - copy-and-paste instructions that run the pattern in any AI tool.
- **Raised by:** Greg, October 16, 2026, while reviewing the pattern dashboard.
- **Why:** Only 4 of 13 written patterns have it (01, 03, 05, 08). Readers can put those to work right away; the rest are read-only.
- **First candidate:** Pattern 12, Ghost in the Workflow - its Step 1 standing documentation constraint is already a ready-made prompt.
- **Other candidates (Claude's notes, not yet discussed):** 09 The Compressed Apprenticeship (its narrated-output prompt template), 10 Models Are Not Good at Math (its formula prompt), 13 Automate the Invisible (an AI-assisted value-stream mapping prompt).
- **Connection:** Pattern 14, Embed the Expert, is about turning expertise into a skill - each "Use this pattern" modal is an example of that.
- **Dashboard:** "Use this pattern" column added October 16, 2026.
- **Status:** Open - Pattern 12 first.

## 16. Credit Christopher Alexander on the website

- **What:** Add homage to Christopher Alexander - the architect whose pattern languages (A Pattern Language, 1977) inspired Design Patterns (1994) - to the site, alongside the Gang of Four reference.
- **Raised by:** Owen Fitch (red-team persona on the talk abstract), October 16, 2026. Greg: "I indeed owe homage to him. We should probably add that to the website as well."
- **Where:** The About section on `index.html` (the "In 1994, Gamma, Helm, Johnson, and Vlissides published Design Patterns..." paragraph) is the natural place. Also the README's "Gang of Four" line.
- **Related:** Kent Beck was an early figure in bringing patterns into software - check the history before stating it; if accurate, it connects the ore-and-gold thesis to the patterns frame.
- **Status:** Open.

---

# Pattern pipeline notes

Thinking captured for upcoming patterns, so the reasoning survives until each one is built.

## New idea - Avoid the Naughty List (unnumbered, Accuracy)

- **What:** A pattern about using AI for data cleanup: AI-driven data audits, and AI-written cleanup scripts.
- **Raised by:** Greg, October 15, 2026, mid-draft of Pattern 12. In his words: "AI data cleanup is a real thing and the use of AI Data Audits and cleanup scripts can be a thing."
- **Why:** Data cleanup is a real, common need, and AI can do both the audit (finding the problems) and produce the scripts that fix them.
- **Connections Claude noted (not yet discussed with Greg):**
  - Pattern 10, Models Are Not Good at Math - But They Can Program: same principle. Have AI write a cleanup script that can be reviewed and rerun, rather than having it edit data directly.
  - Pattern 12, Ghost in the Workflow: cleanup scripts are AI assets too and need a record of what they changed and why.
  - Pattern 03, Test Adversarially: test a cleanup script before it touches production data.
  - "Signal vs. Noise" and "The Intelligence Layer" in Coming Soon both depend on trusted data, so this may be a prerequisite pattern for them.
- **Greg's framing (October 15, 2026):** AI doesn't *automatically* clean data - but AI can absolutely *help* you clean it. AI data audits and cleanups are a valuable tool for work that used to be done by hand: "naughty list" reporting and emails chasing teams to fix their records. Origin: Greg's comment on a LinkedIn post claiming "AI doesn't clean data." His comment: "I think the first sentence should say, AI doesn't automatically clean data. I say this because AI can absolutely help you clean up your data. AI data audits and cleanups are a valuable tool that used to have be done by hand with naughty list reporting and emails to teams."
- **Rejected framing - do not reuse:** "The data is why your AI is failing" (dirty data gets blamed on the AI tool). Greg hates it - the point is using AI to make your data better, not data quality as a precondition for AI.
- **Possible shape (to confirm with Greg):** Problem - the manual naughty-list cycle (reports, emails, chasing owners, slow and resented), or the opposite misconception that AI cleans data on its own. Solution - AI audits the data and produces reviewable cleanup scripts and targeted fix requests; humans approve and own the changes.
- **Open questions:** Category (Accuracy, Agentic, or Governance)? Name? Does the Problem lead with the manual naughty-list cycle, the "AI cleans it automatically" misconception, or both? Any client or Planview/JCI stories to ground it? Where does it sit in the build queue?
- **Working title:** Avoid the Naughty List (confirmed by Greg, October 15, 2026). Category: Accuracy.
- **Site status:** Added to Coming Soon on `index.html` October 15, 2026.
- **Status:** In the build queue, sixth - after the original five (12 Ghost in the Workflow, 13 Automate the Invisible, 14 Embed the Expert, 15 The Staged Journey, 16 Right Tool, Right Job). Greg, October 15, 2026: it does not replace any of them.

## New idea - Iterate to the Destination (unnumbered)

- **What:** A pattern for when the value statement can't be defined up front and evolves with the work - a counterpoint or companion to Pattern 01, Begin with the End in Mind.
- **Raised by:** Shubham Dwivedi (Staff TPM, SAFe RTE) independently surfaced this gap in a LinkedIn comment on Greg's Pattern 02 post, October 14, 2026.
- **Source material:** `sources/shubham-dwivedi-iterate-to-destination.md`.
- **Contributor:** Potential contributor - Greg to engage. Related: backlog item 4 (contributor outreach).
- **Status:** Added to Coming Soon on the site October 15, 2026 (category: Conversational). Not in the build queue.

## New idea - AI Reads, Tools Copy (unnumbered)

- **What:** AI summarizes well, but when asked to reproduce data exactly it reconstructs from memory instead of copying. Applies beyond spreadsheets to code, contracts, meeting notes, and any large corpus. Use AI to explain; use normal tools (filters, queries, reports) to extract. Working line: "Ask AI to explain. Don't ask it to copy."
- **Source:** Chris Gallivan post, October 14, 2026. Source material: `sources/chris-gallivan-ai-reads-tools-copy.md`.
- **Contributor:** Greg to reach out to Chris Gallivan about contributor credit. Related: backlog item 4.
- **Related patterns:** Pattern 10 (Models Are Not Good at Math - same family: use AI for what it's good at, tools for precision); Avoid the Naughty List.
- **Status:** Added to Coming Soon on the site October 15, 2026 (category: Accuracy). Not in the build queue.

## New idea - AI Friction (unnumbered)

- **What:** Teams use AI for work that doesn't need it. A 20-second internal reply becomes a 10-minute prompting loop; three solid bullet points become five verbose, jargon-heavy pages. It looks polished, but the impact is zero - or negative, because the point of the work (e.g. genuine reflection and coaching in a performance review) gets lost.
- **Source:** Tom Buyckx LinkedIn post, about October 13, 2026. Full text saved in `sources/tom-buyckx-ai-friction.md`. Shared by Greg October 15, 2026.
- **Key ideas from the post (paraphrased):**
  - Metaphor: don't use a bicycle if you only need to cross the street.
  - Leaders' job is not only driving AI adoption but preventing AI friction.
  - Efficiency means using AI where leverage actually exists (deep research, account prep, scenario modeling), not as an automated layer of corporate noise.
  - Example: performance reviews inflated by an LLM, losing the reflection and coaching that were the point.
- **Contributor:** Tom Buyckx (3rd+ connection). Credit approach not yet discussed - Greg to decide whether to reach out.
- **Overlaps to resolve (Claude's notes):**
  - Pattern 05, Avoid AI Slop - the inflated-review example is a slop symptom; this idea is about *whether* to use AI at all, not how to keep output genuine.
  - Pattern 01, Begin with the End in Mind - a value statement would expose the zero-impact cases.
  - Right Tool, Right Job (Coming Soon) - that one is about which model; this is about whether AI is the right tool at all. Could be one pattern or two.
  - Speed Is Not a Value Statement (Coming Soon) - related theme of activity mistaken for value.
- **Possible framing (to confirm with Greg):** Leadership level - leaders set the norm for where AI earns its place, and where it just adds friction.
- **Name (Greg, October 15, 2026):** AI Friction. Alternative considered: "Don't Ride a Bicycle Across the Street."
- **Relationship to Right Tool, Right Job (Greg, October 15, 2026):** Different patterns - unless Right Tool, Right Job is expanded so that "no tool" (not using AI at all) is one of the options. Not yet decided whether to expand it.
- **Decided (Greg, October 15, 2026):** Keep AI Friction separate from Right Tool, Right Job (selection problem vs. habit problem; Accuracy vs. Leadership). Category: Governance.
- **Site status:** Added to Coming Soon October 15, 2026.
- **Open questions:** Build queue position? Reach out to Tom Buyckx about credit?
- **Status:** On the site (Coming Soon). Not in the build queue.

## New idea - Redesign the value stream, not the role (Sandra Loughlin) - pattern or something bigger

- **What:** Using AI to redesign work inside current roles rarely creates business value, because value comes from value streams that cut across roles, divisions, and geographies. Speeding up one step just moves the backlog to the next step unless that step is the real bottleneck. Redesign should start at the value stream: map the whole process (friction points, human glue, tacit knowledge, judgment-critical tasks, what people love and hate), apply AI to augment and automate, iterate until "good enough for now," then see what human tasks remain, and only then refactor them into new roles and skills.
- **Source:** Sandra Loughlin, PhD (Chief Learning Scientist, EPAM) LinkedIn post, about October 15, 2026. Full text in `sources/sandra-loughlin-value-stream-redesign.md`. Shared by Greg October 16, 2026.
- **Greg's view:** Agrees with it wholeheartedly. Not sure whether it's a pattern or something bigger.
- **Other points from the post:** SDLC and PDLC are the blueprint because those workflows are already mapped and measured; do the redesign in 1-2 Tiger Teams (faster, lets you test operational/incentive/talent tactics, avoids pushing change too fast); data and knowledge are the biggest barriers and the biggest unlock; capture skills data on people in the workstream so they can be matched to new roles.
- **Contributor:** Sandra Loughlin (3rd+). Credit approach not yet discussed.
- **Connections (Claude's notes, not yet discussed):**
  - Pattern 11, The Productivity-to-Headcount Trap - its Solution (redesign first, then decide on headcount) is the same sequence. Her post is strong external support for 11.
  - Automate the Invisible (13) - "human glue" and handoffs are the invisible work; overlaps heavily.
  - Ghost in the Workflow (12) and Embed the Expert (14) - tacit knowledge.
  - Avoid the Naughty List - her data point (data is the biggest barrier).
  - The Staged Journey and The Intelligence Layer (Coming Soon).
  - GO Framework, Organization pillar; Greg's EPMO and value-stream background.
- **Decided (Greg, October 16, 2026):** Both.
  - **Pattern:** "Redesign the Stream, Not the Role" - Leadership level. Coming Soon card drafted, awaiting Greg's OK.
  - **Bigger:** the patterns form one method - (1) map the value stream, (2) find the invisible work and tacit knowledge, (3) fix the data, (4) apply AI, (5) iterate, (6) redesign roles last. This becomes a **"For organizations" page** on the site: the Level 5ive engagement model, each step linking to its patterns (Redesign the Stream; Automate the Invisible; Ghost in the Workflow and Embed the Expert; Avoid the Naughty List; Productivity-to-Headcount Trap). Closes the retrospective's "bridge to the offer" gap (item 12). Also a candidate signature talk.
- **Open questions:** Tiger Teams as part of the engagement model? Credit Sandra on the page and the pattern? Page timing vs. publishing Leadership patterns.
- **Status:** Pattern card live in Coming Soon (October 16, 2026). "For organizations" page not started.

## New idea - Ore is not gold (Kent Beck) - possibly the library's central thesis

- **What:** Measuring AI productivity by output volume (lines of code per second) is like measuring the ore coming out of a mine. What matters is how much gold results. A 10x increase in ore from automation may or may not increase gold production.
- **Source:** Kent Beck, LinkedIn. Text and link (https://lnkd.in/p/gWiaWi-R) in `sources/kent-beck-ore-and-gold.md`. Shared by Greg October 16, 2026.
- **Greg's view:** "Might be the most important insight of this entire process. It applies to more than just coding."
- **Credit rule:** Kent approved being credited. No direct quotes on the site - "Inspired by" prose attribution, per Greg's convention (Pattern 09 precedent).
- **Why it's central (Claude's notes, not yet decided):** It names the failure many patterns already describe:
  - Pattern 11 - hours saved (ore) treated as headcount value (gold).
  - Redesign the Stream - speeding one step (ore) doesn't raise throughput (gold).
  - Pattern 01 - the value statement defines what the gold is.
  - AI Friction - more polished output (ore), zero impact (no gold).
  - Pattern 06 - more output from a gap is more ore with no gold.
  - Value facets (item 13) - the facets are the kinds of gold.
- **Possible uses (to decide):** a pattern of its own (e.g. "Measure the Gold, Not the Ore" - Leadership); the organizing thesis for the site's homepage value statement (Jeff's ask, item 9); the spine of the signature talk (retrospective item 12).
- **Decided (Greg, October 16, 2026):** Use it as (1) the thesis of the signature talk and (2) the homepage value statement. Not a standalone pattern for now.
- **Credit (Greg, October 16, 2026):** Kent Beck must be credited wherever it's used - on the homepage and in the talk. "Inspired by" prose attribution, no direct quote.
- **Status:** Homepage value statement - live October 16, 2026 (Option A, Kent Beck credited). Talk thesis - feeds retrospective item 12 (signature talk).

## New idea - AI sameness: better answers, less original thinking (Fabio Moioli) - unnumbered

- **What:** AI makes individual work better but collective work more alike. Ten people with the same AI tool get ten better ideas that look surprisingly similar. The risk isn't replacing creativity; it's not noticing how much the same suggestions and assumptions shape everyone's thinking. Don't confuse better answers with better thinking.
- **Source:** Fabio Moioli (Spencer Stuart) LinkedIn post, October 16-17, 2026. Full text in `sources/fabio-moioli-ai-sameness.md`. Shared by Greg October 17, 2026 ("good things here").
- **Evidence (verified):** Doshi & Hauser, *Science Advances* 10(28), 2024 - AI raised story novelty about 8%, mostly for less-creative writers, did not help the most creative, and made stories 10.7% more similar to each other.
- **Connections (Claude's notes, not yet discussed):**
  - Pattern 08, Assemble the Team - the strongest link; the fix for sameness is deliberately different perspectives. The study is strong external evidence for 08's Problem.
  - Pattern 05, Avoid AI Slop - generic, indistinct output; the study shows it happens even when output is rated better.
  - Pattern 06, AI as Amplifier - the study's finding that the least creative gained most and the most creative gained nothing is AI as amplifier in data.
  - Pattern 07, Own the Thinking - "better answers vs. better thinking."
  - Organizational angle: if every team uses the same model the same way, the organization's strategy converges on its competitors'. Strategic value facet; Leadership level.
- **Possible uses:** (1) evidence for Patterns 08 and 06; (2) a new pattern on organizational sameness ("Ten People, One Idea" or similar - Leadership); (3) a talk point alongside ore vs. gold.
- **Contributor:** Fabio Moioli (2nd connection). Credit approach not yet discussed.
- **On the site (October 19, 2026):** Coming Soon card added as "Ten People, One Idea" (working title), category Conversational (Claude's pick - Greg to confirm). Build queue position 5, after Research Partner, Not Oracle (Greg, October 19, 2026).
- **Status:** Idea captured. Use to be decided.

## New pattern - The Night Shift (working title) - TOP PRIORITY

- **What:** Delegating substantive AI work to run unattended overnight (or while you're away), with the human making the judgment calls in the morning. The new way Greg and Claude started working the week of October 12, 2026.
- **Raised by:** Greg, October 18, 2026 ("We are missing a pattern and it is a new way we are working"). Name suggested by Claude; Greg confirmed the idea.
- **Priority:** **Top of the priority list and first in the build queue** (Greg, October 18, 2026).
- **Failure mode:** Most people only use AI while sitting with it, so AI moves at the speed of their calendar. Those who do delegate unattended work often let AI act with no checkpoint, changing things nobody approved.
- **The practice, as learned this week:**
  1. Split the work by judgment - research, verification, drafting, records, and red-team *findings* go overnight; decisions, naming, red-team *calls*, and publishing stay with the human.
  2. Write each overnight task as a standalone brief - scope, outputs, and where they go - so it can be done cold.
  3. Nothing goes live overnight - everything lands on a branch or in a doc, behind approval.
  4. Findings, not changes - red teams propose numbered changes to accept or reject; they don't apply them.
  5. A morning review ritual - a short summary of what's ready, then decide piece by piece.
  6. Keep the record - handoff records, dashboard, and backlog updated so overnight work never becomes a ghost (Pattern 12).
- **Real examples to use (October 15-17, 2026):** Overnight run 1 - handoff records for all patterns, source verification (found four errors on the live site), redrafts of 01-09, first draft of Pattern 13. Overnight run 2 - value-facets report, red-team findings for 01-08, Embed the Expert prep, speaking-venue research.
- **Connections:** Pattern 04 (recurring coordination, not delegated substantive work); Pattern 12 (records keep overnight work from becoming ghosts); Pattern 08 (red-team findings overnight, calls live); Pattern 03 (source verification is ideal overnight work). Strong talk story: site launched Monday, three overnight work cycles by Friday.
- **Open questions:** Final name? Category (Agentic?) and level (Practice?). Add to Coming Soon now?
- **Status:** Captured; first in the build queue.

## Pattern 14 - Embed the Expert (Agentic)

- **What:** A pattern about deliberately packaging an expert's judgment as a reusable **skill**, so it works without the expert in the room.
- **Decided by:** Greg, October 15, 2026.
- **Model to follow:** Pattern 08, Assemble the Team, which exists both as a pattern on the site and as a working skill people can run. Pattern 14 should do the same: explain the practice, then show what the expert-as-skill looks like in use.
- **Meaning of "skill":** A packaged, reusable instruction set an AI runs on demand (like the Assemble the Team skill), not "skill" in the general human sense. Define this explicitly in the pattern for accurate taxonomy.
- **How it differs from Pattern 12 (Ghost in the Workflow):** They are mirror images.
  - **12 is the failure mode.** Knowledge gets trapped inside undocumented AI artifacts and is lost when the builder leaves.
  - **14 is the intentional practice.** Expert knowledge is captured on purpose and made durable and transferable.
  - A well-built skill is self-documenting, so 14 can be cited in 12's Solution as one remedy.
- **How it differs from Pattern 09 (The Compressed Apprenticeship):** 09 is about people learning faster with AI; 14 is about turning one person's judgment into something others can run. Draw the line explicitly in the Context section.
- **Site status:** "Coming Soon" description on `index.html` updated to point at the skill framing.
- **Status:** Not started. Third in the build queue, after 12 and 13.

## Pattern 12 - Ghost in the Workflow (Governance)

- **What:** Renamed from "The Expert's Ghost" and reframed on October 15, 2026. The ghost is poorly documented AI agents, chats, prompts, and practices. It shows up when the person who built them leaves.
- **Category:** Moved from Conversational to Governance (`.tag-gov`).
- **Original idea (retired):** Tacit expert knowledge never articulated. That theme now lives in Pattern 14.
- **Angles worth using:** The irony that AI meant to capture knowledge creates a new kind of knowledge loss. Ties to AI tool sprawl - orphaned agents are sprawl's long tail.
- **Open question:** "Build for the Room" (in Coming Soon, Agentic) covers AI workflows only their creator can operate. It overlaps heavily with 12. Decide whether to merge it into 12, drop it, or narrow it to the bottleneck-while-present angle (12 covers the after-they-leave angle).
- **Status:** Next to build.

## New idea - Source search for Pattern 02, Onboard, Don't Program (tonight, Oct 18, 2026)
- **What:** Find credible, verifiable sources supporting the pattern - e.g., research on context or system prompts improving output quality, onboarding analogies, vendor guidance on providing context and asking the model to restate the brief.
- **Why:** Greg rejected expanding the page "for no reason" (red-team change 2); sources are the legitimate way to strengthen it.
- **Output:** Add findings to records/02 (create if missing) and sources/README.md, verified or marked unverified. Propose, don't apply, page edits.
- **Origin:** Greg, October 18, 2026, during the 01-08 red-team review.

## New idea - Real-world case for Pattern 06, AI as Amplifier (tonight, Oct 18, 2026)
- **What:** Find a verified, public case where someone shipped AI output they couldn't defend and it cost money or carried legal consequence - e.g., lawyers sanctioned for AI-fabricated citations (Mata v. Avianca, 2023, and later cases), or a financial misstatement traced to unchecked AI work.
- **Why:** Red-team change 2 (Omar): the three current examples are embarrassing, not costly. A fourth with financial or legal stakes makes the cost concrete.
- **Output:** Draft the fourth example with source, verified or marked unverified, in records and sources/README.md. Propose, don't apply.
- **Origin:** Greg, October 18, 2026, during the 01-08 red-team review.

## Monday Oct 19 add-on - Category review for Patterns 06 and 07
- **What:** Decide whether 06 (AI as Amplifier) and 07 (Own the Thinking) stay in Accuracy. Ben's point: both are about the person, not the output's accuracy.
- **When:** With the Governance filter tab work on Monday, since categories and filters change then.
- **Origin:** Red-team change 4 for 06; Greg, October 18, 2026.
- **Decided (Greg, October 19, 2026):** Leave 06 and 07 in Accuracy. Closed.

## New idea - Pair AI with people: human capability matters more with AI (Sandra Loughlin) - captured October 19, 2026
- **Link:** https://lnkd.in/p/gHdc4SQX
- **Source:** Sandra Loughlin, PhD (Chief Learning Scientist, EPAM) LinkedIn post, about early October 2026, sharing a post by Dr. Marianne Roux. Full text in `sources/sandra-loughlin-human-capability.md`.
- **What it says:** Because AI amplifies the cognition, intention, and judgment of the person using it, understanding the person matters more than ever - personality (trait activation theory), epistemic beliefs, relational reasoning, regulatory focus, temporal depth, sensory gating, and even whether someone wants to slow down or go faster right now. Understanding and optimizing human capability becomes a primary source of competitive differentiation. "There's more to life than skills."
- **Greg's framing:** "about pairing AI with people."
- **Connections (Claude's notes, not yet discussed):** Pattern 06, AI as Amplifier (her "AI amplifies" line is 06's thesis); Pattern 09, The Compressed Apprenticeship; Embed the Expert (14); The Staged Journey (people adopt at different speeds); Ten People, One Idea.
- **Contributor:** Sandra Loughlin - also the source for Redesign the Stream, Not the Role; she called the site "AWESOME." Credit approach not yet discussed. Marianne Roux's original post not read.
- **Decided (Greg, October 19, 2026):** Add to Pattern 06; no new pattern. Sandra is good with credit on the site. Done - Notes paragraph and Inspired by credit on 06.

## New idea - Webinar series to get the patterns out now (Greg, October 18, 2026)
- **Why:** Greg: "We need to work on getting this out there. Those options are too far in the future." Conference and venue calls (Minnebar, PMI Madison PDD, etc.) are months out; webinars can start in weeks.
- **Options discussed:**
  1. Host our own - 30 minutes every two weeks on LinkedIn Live or Zoom, one pattern per session: the failure, the pattern run live, Q&A. First session: Avoid AI Slop (Joe Bitter's favorite; the live interview demos well). Doubles as rehearsal for the "Ore is not gold" talk; recordings become site and LinkedIn content; registrations build a contact list.
  2. Guest on others' webinars - PMI chapters, ISACA, Global AI Milwaukee virtual sessions; PPM vendor and partner webinars via Greg's Planview network.
  3. Co-host with contributors - Jeff Toppall; Sandra Loughlin (Redesign the Stream).
- **Recommendation:** Start with 1 for the reps; pitch 2 to two or three chapters at the same time.
- **Open:** Platform (LinkedIn Live, Zoom, Teams) and first session date - Greg to decide.
- **Deliverables once decided:** series plan and schedule, first session outline and deck, registration page, pitch email for chapter programs.

## Talk evidence - "AI acceleration": more decisions, faster (Simon Raitt) - captured October 19, 2026
- **Link:** https://lnkd.in/p/gvrNghtK
- **Source:** Simon Raitt (CEO) LinkedIn post, about October 15, 2026. Full text in `sources/simon-raitt-ai-acceleration.md`.
- **What it says:** AI isn't dumbing people down - it's making them work harder. Delegating to a colleague gave natural breathing room to think; AI returns output almost instantly, so you go straight to the next decision. "Instead of fewer decisions, I'm making more of them, faster."
- **Decision (Claude, at Greg's request, October 19, 2026): talk evidence, not a new pattern.** One CEO's experience, not data, and it describes a cost rather than a practice. Uses:
  - **"Ore is not gold" talk:** the human side of the productivity story - output speeds up, but the decisions don't shrink; they pile up on the person. Pairs with McKinsey's 80% productivity vs. 37% profit.
  - **The Night Shift (15):** the pattern is part of the answer - batching AI work overnight and making the calls in one morning review gives back the breathing room. Possible future Notes line, without naming him unless credit is cleared.
  - **Watch for:** if more evidence of AI decision fatigue turns up (research, not posts), revisit as a pattern.
- **Credit:** Simon Raitt is a 3rd+ connection; not contacted. Use as "one CEO wrote..." in talks, or ask before naming him on the site.

## New idea - Update all pattern images to the photorealistic theme (Greg, October 19, 2026)
- **What:** Bring every pattern image in line with the photorealistic style the site has moved to.
- **Current state (checked October 19, 2026):**
  - Photorealistic already: 01 Begin with the End in Mind, 08 Assemble the Team.
  - Flat illustration style, to redo: 02 Onboard, Don't Program; 03 Test Adversarially; 04 The AI Operations Manager (these also have the title baked into the image).
  - Icon diagram, to redo: 05 Avoid AI Slop (workflow diagram).
  - No image yet (placeholder): 06, 07, 09, 10, 11, 12, 13, 14.
- **First:** Pattern 12, Ghost in the Workflow - needed now, as it publishes this week. Photorealistic prompt drafted October 19, 2026 (in chat).
- **How:** Greg generates images in his image tool from prompts Claude drafts per pattern; Claude places them on the pages with alt text. Match 01 and 08: real office settings, natural light, professional people, AI elements as subtle screen or holographic overlays, no title text in the image.
- **Origin:** Greg, October 19, 2026, while preparing Pattern 12 for publishing.
- **Publishing rule (Greg, October 20, 2026):** redos of existing images go live immediately; new images for patterns not yet published (13, 14, etc.) wait for that pattern's publish. Redos 02, 03, 04, 05 all live October 20, 2026; 13 and 14 images held on branch publish-13. Still needed: 06, 07, 09, 10, 11, 15. **Greg, October 20, 2026:** for patterns not yet published that still need images, hold the prompts until the day each pattern is published - generate then. Prompts stay in records/image-prompts.md; on publish day, surface that pattern's prompt as part of the publish prep.

## Publishing next - Pattern 13, Automate the Invisible (Greg, October 19, 2026)
- Greg: 13 is next to publish, after 12 (published October 19). Still within the 2-per-week cadence. Needs a photorealistic image (prompt in tonight's run) before publishing.

## Announce Pattern 12 - LinkedIn Article vs. post (Greg, October 19, 2026)
- Greg wants to include the documentation built for Pattern 12 using Pattern 12 itself (its handoff record) - likely too long for a post.
- Recommendation (Claude): a LinkedIn Article that walks through the pattern and shows its own handoff record as the worked example, plus a short post linking to it. Greg to decide.

## Site redesign - look and feel options (Greg, October 19, 2026)
- **What:** New look and feel for aisuccesspatterns.com. Full brief saved verbatim in sources/greg-site-redesign-brief.md.
- **Key points:** Mantra "make the complex simple." Problem today: utilitarian, boring colors, lots of reading, no imagery. Two paths: the encyclopedia user (fast search, scan the catalog) and the browser (leave with 2-3 usable patterns). Newcomer path as a 3-part story, easy to hard: Avoid AI Slop, Assemble the Team, Ghost in the Workflow. Own identity - not Level 5ive's palette; footer credit stays. References: LinkedIn (simple), Amazon (shopping/search-and-browse), Epic MyChart (calm cards). Nothing is sacred.
- **Repo check:** Not Jekyll - plain static HTML on GitHub Pages.
- **Overnight October 19-20, 2026:** produce a couple of design options as clickable mockups on a branch, for Greg to compare. No live changes.
- **Related:** Photorealistic image theme (backlog entry, same night); Greg also mentioned a possible Fiverr redesign.
- **Origin:** Greg, October 19, 2026.

## Publishing cadence - updated (Greg, October 19, 2026)
- Moving a pattern into In Review does NOT count toward the publishing limit.
- Up to 5 patterns a week move into In Review.
- For now, up to 2 a week move to Published.
- Supersedes the October 16 note that counted In Review moves.

## Nightly cadence - the Night Shift, applied (Greg, October 19, 2026)
- **Every night, two In Review pipeline items:**
  1. **Draft one new pattern** from the build queue: first-pass Problem, Value, Context, Solution, Notes plan, handoff record, questions for Greg. Build queue order: The Staged Journey (16), Right Tool, Right Job (17), Avoid the Naughty List (18). The live red team with Greg happens the next day, then it moves to In Review.
  2. **Red-team one existing In Review pattern** - findings only, as numbered proposed changes; Greg makes the calls live the next morning (Night Shift Step 2/4). Only for In Review patterns that don't yet have a red team - Greg, October 19, 2026: none currently lack one. October 19-20 is a light night (image prompts + draft The Staged Journey); October 20-21 is the first night with two patterns, plus the site-redesign options.
- **Plus** any one-off overnight items Greg adds that day (e.g., image prompts, research).
- **Night Shift rules for every run:** work from BACKLOG.md; one new branch per night; nothing goes to main; findings, not changes; morning summary in records/overnight-YYYY-MM-DD.md including what couldn't be done and why; update records, backlog, and dashboard; push the branch.
- **Keeping it going:** each night's run ends by scheduling the next night's run into this session (about 11:30 PM CT), so the cadence continues without manual setup.
- **Pace check:** one draft a night fits Greg's target of 5 a week into In Review; 2 a week to Published.

## Nightly cadence addition - "Use this pattern" drafts (Greg, October 19, 2026)
- **Every night:** draft the "Use this pattern" section (copy-and-paste instructions, like 01, 03, 05, 08) for ONE pattern that's missing it. Draft only, on the night's branch; Greg reviews in the morning.
- **Missing as of October 19, 2026 (11):** 02, 04, 06, 07, 09, 10, 11, 12, 13, 14, 15.
- **Order:** 12 first (just published, and item 15 already named it first), then 13 (publishing next), 14, 15, then 02, 04, 06, 07, 09, 10, 11.
- **Standard going forward (adds to item 14, standard practice for new patterns):** every new pattern gets a "Use this pattern" section before it moves to In Review. The nightly draft of a new pattern includes a first pass at it.
- **Starts:** tomorrow night, October 20-21 (tonight stays light per Greg).

## New pattern - Research Partner, Not Oracle (Greg, October 19, 2026)
- **What:** Using AI as a research partner whose citations you always check at the source. Greg: "I would have never been able to research and quote sources like I can with you helping."
- **Category / level:** Accuracy (Greg); Practice (proposed).
- **Failure mode:** AI makes source-backed research possible for anyone - and equally makes it easy to cite sources that don't exist (Deloitte Australia refund; Mata v. Avianca).
- **The practice, as done on this library:** check every source at the original, not the AI's summary or a search snippet (the October 15 source check found four errors on the live site); mark each source verified or unverified and leave out what can't be confirmed (CSA 15% on 12, the $86K sanction, the 04 claim); follow the evidence even when it contradicts you (Pattern 03's self-critique line); keep the receipts - sources saved verbatim, recorded in handoff records.
- **Distinct from:** Pattern 03 (attacks the AI's reasoning; this is about evidence); Pattern 10 (same idea for numbers).
- **Build queue:** position 4 - after The Staged Journey, Right Tool, Right Job, and Avoid the Naughty List (Greg, October 19, 2026).
- **On the site:** Coming Soon card added October 19, 2026.
- **Talk story:** a library where every statistic was checked at its source, built by one person in a week.

## Nightly cadence update - red teams overnight (Greg, October 20, 2026)
- Red teams for new patterns now run in the overnight run as findings only (numbered proposed changes); Greg makes the calls the next morning. This replaces the October 16 rule that new patterns get a live red team.
- Rhythm: night 1 drafts a pattern; Greg answers its questions and approves the team the next day; night 2 red-teams it while drafting the next one.
- First: The Staged Journey (16), night of October 20-21, team Hank Dillard (adversarial), Priya Nair, Tom Becker, Lena Ortiz.

## Getting in front of people now - outreach channels (Greg, October 20, 2026)
- **Why:** Greg: "Let's get back to making money with this stuff. Since the conferences are too far in the future, let's brainstorm other ways to start talking more to people."
- **Options brainstormed (Claude, October 20, 2026):** 20-minute one-to-one pattern walkthroughs with EPMO leaders Greg knows (Mandi Turner first); introductions from contributors and fans (Sandra Loughlin, Joe Bitter, Jeff Toppall); ask live conversations (Aravo, Anaqua) about customer or internal sessions; free lunch-and-learns inside companies ("Ore is not gold"); PMI chapter virtual meetings; podcast guest spots; the webinar series; a weekly LinkedIn pattern post; commenting on Sandra / Kent Beck-type posts; a half-day paid "AI Patterns for your PMO" workshop as a first paid offer.
- **Greg's additions:**
  1. **RiverRun partnership (Joe Bitter).** Joe works for RiverRun in the Milwaukee area - a company that provides AI infrastructure to businesses and needs help teaching those businesses how to use it. Idea: the patterns as the "how to use it well" layer - co-hosted customer webinars or workshops, onboarding content, referrals. Not yet verified online (a quick search didn't find it) - Greg to share details: what RiverRun sells, to whom, and what Joe said.
  2. **MMAC and other business trade organizations.** Leads found October 20, 2026 (not yet researched): MMAC (2026 sponsorship guide public), Waukesha County Business Alliance, Vistage (speaker application), AEM 2026 Momentum event series in Milwaukee (AI and data), Summerfest TechAI (JCI on a panel), other local chambers.
- **Overnight October 21-22, 2026:** research and map these organizations - how each takes speakers or programs, next openings, cost, audience, contact - into records/outreach-venues.md (add RiverRun if anything public turns up).
- **Status:** Brainstormed; research scheduled. Outreach drafts (walkthrough message, lunch-and-learn offer) offered, not yet requested.

## Webinar series - build-out (Greg, October 20, 2026)
- **Decision:** Build the webinar series out in the overnight sessions, a piece per night (extends the October 18 webinar entry).
- **Pieces, in order:** (1) series plan - name, audience, cadence, length, format, platform options, and how it leads to engagements; (2) session lineup - one pattern per session, newcomer path first (Avoid AI Slop, Assemble the Team, Ghost in the Workflow); (3) Session 1 outline and slide plan (light backgrounds); (4) registration page copy; (5) promotion plan (LinkedIn posts, RiverRun / trade-org co-hosting); (6) follow-up offer (the 20-minute walkthrough or half-day workshop).
- **Open for Greg:** platform (LinkedIn Live, Zoom, Teams) and first date.
- **Update (Greg, October 20, 2026 - LLM Interview with "Diane"):** Piece 1 (series plan) built live instead of overnight - Claude Doc "AI Success Patterns Webinar Series - Plan" (https://claude.ai/code/artifact/4e2d4094-f0ee-4832-b7c8-cc83c269ab47). Key decisions: 10-minute sessions for people's "10 minute file" (JCI idea - things that sharpen the saw if you have 10 minutes), 20-minute max; one pattern each; hosted on a website; **no email wall** - Greg wants to see how many view and from where, and an easy follow-up to "teach this to my org"; must be fun (Friday bourbon post as the model); each session = problem, value, Use this pattern (skill or paste-in prompt); lineup: Avoid AI Slop, The Night Shift, Assemble the Team, Ghost in the Workflow (Slop first - its interviews build the backlog the Night Shift needs).
- **Status (Greg, October 20, 2026):** All synthesized items confirmed. Weekly on Tuesdays; recorded; hosted on aisuccesspatterns.com; follow-up uses the site's existing options (Talk to Greg, Book a meeting); site analytics, not sign-ups; the four-pattern path grows as patterns are added. Series name: "A Ten-Minute Taco 'bout AI" (Greg, October 20, 2026; Taco Tuesday theme - phrase free to use since Taco John's abandoned its trademark in 2023). Open: how value is quantified. Next pieces (Session 1 outline, page copy, promotion, follow-up offer) to come in overnight runs.
- **Production rhythm (Greg, October 20, 2026):** session prep runs in the Thursday night run; Greg records by Monday at the latest; publishes Tuesday. First: Session 1, Avoid AI Slop - prep Thursday October 22-23, record by Monday October 26, publish Tuesday October 27.
