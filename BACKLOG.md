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

## 2. Red team published patterns 01-07 with Assemble the Team

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
- **Status:** Idea captured. Not in the build queue yet.

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
