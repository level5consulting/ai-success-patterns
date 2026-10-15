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
