# Red team - Pattern 24, Dashboards That Answer a Question (November 3, 2026)

Findings only - nothing applied. Greg decides each item in the Morning Review form. Reviewed: patterns/24-dashboards-that-answer-a-question.md (draft 1.1, Greg's October 30 answers applied).

**Team (approved by Greg, October 30, 2026):**
- **Diane Kowalski (adversarial)** - VP of finance who wants every metric visible "in case someone asks."
- **Marcus Reyes** - EPMO director who owns forty project status dashboards.
- **Leah Brandt** - BI analyst who now builds dashboards with AI in an hour.
- **Tom Okafor** - COO who reads dashboards on his phone between meetings.

---

## Round 1 - Problem and Value

**Diane (adversarial):** Your premise is that showing everything means answering nothing. My problem is the opposite: the day I cut a metric is the day the board asks about it. You need to say where the other numbers go, not that they go away. "Detail page or nowhere" sounds like you're hiding things from auditors.

**Marcus:** The portfolio grader story is the best thing in this pattern and it's sitting in Notes. Open the Problem with it. Every EPMO director has the "fancy dashboard, zero impact" story; the grader is the turn.

**Tom:** The Problem says "what do I need to do this week?" - that's my question. But Value never says the dashboard should fit on one screen. If I have to scroll on my phone, I don't read it.

**Leah:** The Problem names the trap - an AI dashboard looks finished - but Value only says "someone checked it." Say who and when: the figure is checked against the source before its first use and after any change to the query.

**Round 1 proposed changes:**
1. Open the Problem with Greg's portfolio grader story (fancy dashboards, zero impact, then the A-F grader). (Marcus)
2. Step 2: say where the other numbers go - a detail page or the source system, findable but off the main view - not "nowhere." (Diane)
3. Value: add "fits on one screen, phone included" as a goal for the main view. (Tom)
4. Value and Step 4: each figure is checked against its source before first use and again after any change to its query. (Leah)

## Round 2 - Context, Solution and Use this pattern

**Diane (adversarial):** Step 5, "delete it," will never get past my compliance team. Say "archive it with the date and the decision it served."

**Marcus:** Step 1's one sentence is great, but most of my dashboards serve three audiences. Tell me what to do then: one dashboard per decision, or one page with the decision at the top of each section.

**Leah:** Use this pattern, Phase 3, says "consider a grade." Give the grader its own step in the prompt - a grade with a "what to fix" line is the most useful thing AI can propose here.

**Tom:** Phase 3 should also ask how the person will see it - phone, wall screen, a slide in the steering meeting. It changes the design completely.

**Round 2 proposed changes:**
5. Step 5: "archive it with the date and the decision it served," not "delete it." (Diane)
6. Step 1: if a dashboard serves several people, build one view per decision - or one page with the decision sentence at the top of each section. (Marcus)
7. Use this pattern, Phase 3: offer a grade with a "what to fix" line as a standard option, not a maybe. (Leah)
8. Use this pattern, Phase 3: ask how the person will see it (phone, wall screen, slide) before designing. (Tom)
