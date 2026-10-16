# Pattern 13 - Automate the Invisible

**Category:** Governance (Greg, October 16, 2026 - this pattern is about selecting which AI projects get green-lit)
**Maturity level:** Leadership (proposed - deciding *which* work to automate is an organizational call; confirm)
**Status:** DRAFT - Problem and Value red-teamed live and revised October 16, 2026. Context and Solution drafted October 16, 2026; live red team next. Notes not started. Not built as HTML.

**Coming Soon card (current, live):** Organizations automate the most visible, most human-facing work first. They hollow out the relationship that differentiates them and keep all the friction the customer never sees.

---

## Problem
**AI gets pointed at the relationship, not at the friction behind it**

Ask leaders where they plan to use AI first, and the answer usually lands on the most visible work they have. Often that's the contact center or the customer chat window, but it can be the sales follow-up, the account review, or the client check-in. Visible work is easy to count - headcount, volume, handle time - so the business case writes itself. It demos well. And it's what most AI vendors are selling.

Visible work isn't automatically the wrong target. Routine, high-volume requests - a password reset, an outage status, a balance check - are often better served by automation, and customers are glad not to wait. The failure is narrower: automating the **relationship moments**. These are the high-emotion, high-judgment interactions where a customer decides whether they trust you - a dispute, a retention call, a complaint, a moment of loss. Automate those and you don't just save cost; you remove the thing that made you different from a competitor with a cheaper price.

Meanwhile, the work that should be automated first sits untouched: work that is **low in visibility and low in regulatory risk**. The handoffs between teams. The status chasing. The re-keying of data from one system to another. The same question asked twice because nobody passed the answer along. Customers never see this work, but they feel it - as delays, as transfers, as "let me check and get back to you." And it stays exactly where it was.

Klarna is the clearest public example. After moving aggressively to AI-first customer service, its CEO told Bloomberg in May 2025 that the chatbots were cheaper but delivered lower-quality service, and the company began hiring human agents again so customers could always reach a person. Klarna didn't fail because it automated customer service. It failed because it automated the moments that needed a person.

The result is the worst of both: the relationship is hollowed out, and the friction is fully intact. The organization has automated its differentiator and kept its dysfunction.

**Definitions used in this pattern**
- **Relationship work** - high-emotion, high-judgment, high-consequence interactions where trust is won or lost. Keep people here.
- **Invisible work** - low-visibility, low-regulatory-risk work that creates friction customers feel but never see: coordination, status tracking, data movement, repeated requests. Automate here first.
- **Not invisible work** - low visibility does not mean low stakes. Work that is hidden but regulated or high-consequence (revenue recognition, compliance reporting, financial reconciliation) needs its own controls and is not a first target.

## Value
**More time for the work only people should do**

- **People move to high-touch, high-impact, high-risk work** - the time freed from coordination and data movement goes to the relationship moments, the judgment calls, and the decisions that carry real consequence
- **Customers feel the difference** - fewer transfers, fewer repeated questions, fewer waits, because the friction behind the conversation is gone
- **The relationship stays a differentiator** - the moments where customers decide whether to trust you are still handled by people
- **Green-light decisions you can defend** - AI investments are selected by where friction is highest and risk is lowest, not by what is easiest to count or demo

## Context
**When this pattern applies**

This pattern applies when an organization is deciding which AI initiatives to fund and launch - especially the first ones. That includes portfolio and intake reviews, AI steering committee agendas, vendor pitches promising headcount savings in customer-facing roles, and any business case built mainly on reducing visible work.

It applies most when the obvious candidate is a relationship moment. If the proposal automates the conversations where customers decide whether to trust you, slow down and look behind it.

The relationship and the friction are connected. When customers complain, it's rarely about the person on the line. It's about being transferred, asked the same thing twice, or promised a callback that never comes - and every one of those is invisible work failing upstream. Fixing that work doesn't just free time; it makes the human conversation better. Automating the front of a broken process only gives customers a faster way to hear "I don't know where your case is."

It does not mean visible work is off limits. Routine, high-volume requests are often the right target. The pattern is about order and selection: friction first, relationship moments last, if ever.

## Solution
**Find the friction, count it, and green-light there first**

**Step 1: Map the work - don't ask about it.** People have normalized invisible work, so asking "where's the friction?" rarely finds it. Walk one end-to-end process, from request to resolution, and record every handoff, wait, re-entry of data, repeated question, and status check. (See Redesign the Stream, Not the Role.)

**Step 2: Sort what you find.**
- **Relationship work** - high emotion, high judgment, high consequence. Keep people here.
- **Invisible work** - low visibility, low regulatory risk. Your first AI candidates.
- **Hidden but regulated work** - low visibility, high consequence. Not a first target; needs its own controls.

**Step 3: Count the friction.** For each candidate, measure what it costs today: cycle time, days in queue, touches per transaction, rework hours, repeat contacts. That gives invisible work a business case that can compete with the headcount line.

**Step 4: Green-light by friction and risk, not visibility.** At intake, rank proposals by how much friction they remove and how low their risk is, not by how easy they are to demo. Ask every proposal that targets visible work: is this routine work, or a relationship moment?

**Step 5: Reinvest the time where it matters.** Decide up front where the freed time goes - to the high-touch, high-impact, high-risk work. If it isn't redirected on purpose, it gets absorbed and the value disappears. (See Pattern 11.)

---

## Notes (draft)

**Related: Redesign the Stream, Not the Role.** The invisible work - handoffs, status chasing, the "human glue" between steps - is exactly what value-stream mapping surfaces. This pattern is related to that method but is not necessarily its first step (Greg, October 16, 2026). It stands on its own: even without a full value-stream redesign, pointing automation at invisible friction instead of the customer relationship is the better first move.

## Origin

- **Greg Stellflue** - from his own experience talking to people about AI (confirmed October 16, 2026). No outside source to credit.

## Sources

- Klarna reversal: CEO Sebastian Siemiatkowski to Bloomberg, reported by Entrepreneur, May 9, 2025 - https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 (paraphrased; no direct quotes, per convention). Verify against the Bloomberg original before publishing.
- Commonwealth Bank of Australia's reversed voice-bot cuts (already used in Pattern 11) is a second example of the same failure - decide whether to reuse it or keep it in 11 only.

## Questions for Greg

**Answered October 16, 2026:**
- Origin: Greg's own experience talking to people about AI.
- Relationship to Redesign the Stream: related, but not necessarily the first step.
- Category: Governance - decided in the live red team.

**Still open:**
2. **Relationship to Pattern 04, The AI Operations Manager** - cite 04 as a Solution starting point, or keep them separate?
4. **Relationship to AI Friction** - reference each other, or keep separate?
5. **A story from your conversations** - one anonymized exchange where a leader named the visible work first would anchor the Problem in your experience.

## Red team log

- **October 16, 2026 - Problem and Value, live** (Assemble the Team: Rafael Ortiz, COO, Fortune 500 telecom - adversarial; Denise Kowalczyk, VP EPMO, manufacturer; Hannah Pierce, CFO; Marcus Lee, Head of CX, regional bank).
  - **Applied:**
    - The pattern is about the relationship, not the role or the channel (Rafael; Greg: "absolutely about the relationship"). Contact center is one example, not a rule; routine visible work can be the right target.
    - "Back-office" replaced with low-visibility, low-regulatory-risk work; definitions added (Rafael, Denise - Greg: they were saying the same thing). Hidden-but-regulated work explicitly excluded (Rafael's billing reconciliation point).
    - Value reframed around freeing time for high-touch, high-impact, high-risk work (Hannah, reframed by Greg); added a green-light bullet.
    - Category set to Governance - selecting which AI projects get green-lit (Greg, leaning on Denise's point).
  - **Not yet addressed:** Hannah's measurement point - give leaders a way to count invisible friction (cycle time, rework hours, touches per transaction, days in queue). Candidate for Solution. Marcus's point that the front-line conversation fails *because* the back end is broken - fixing invisible work improves the human conversation; candidate for Context or Notes. Denise's point that invisible work is found by mapping, not by asking - candidate for Solution, ties to Redesign the Stream.
