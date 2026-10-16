# Source Verification Report

**Run:** October 15, 2026 (overnight)
**Scope:** Every external statistic, study, quote, and named real-world case on pattern pages 01-12. Illustrative examples and sample prompts are listed separately and were not treated as factual claims.
**Result:** 5 verified as written, 4 need correction or softening, 1 unsourced.

Corrections marked **Applied on branch** were made in the `overnight-2026-10-15` branch for Greg's review. Nothing is live until Greg approves.

---

## Needs correction

### Pattern 11 - "A 2026 survey found that 32% of executives..."
- **Problem:** Wrong population. The survey was of hiring managers, not executives.
- **Actual source:** Robert Half survey of more than 2,000 hiring managers, April 2026. 32% of those who eliminated a role due to AI later rehired for the same or similar position. Reported by Outsource Accelerator: https://news.outsourceaccelerator.com/managers-rehire-ai-roles/
- **Fix:** "A 2026 Robert Half survey of more than 2,000 hiring managers found that 32% of those who eliminated a role because of AI had already rehired for the same or a similar position."
- **Status:** Applied on branch.

### Pattern 11 - Commonwealth Bank of Australia
- **Page says:** CBA cut more than 40 customer service staff, replaced them with an AI voice bot, then reversed the cuts "when the bot could not handle rising call volumes."
- **Verified:** 45 roles in Customer Service Direct, to be replaced by an AI voice bot; announced July 2025; reversed August 2025. Sources: Bloomberg (https://www.bloomberg.com/news/articles/2025-08-21/commonwealth-bank-reverses-job-cuts-decision-over-ai-chatbots), Information Age (https://ia.acs.org.au/article/2025/cba-reverses-ai-driven-job-cuts--admits--error-.html).
- **Problem:** The causal claim is stronger than the sources. CBA said its assessment did not adequately consider all relevant business factors. Rising call volumes were the Finance Sector Union's account, alongside weeks of worker pressure.
- **Fix:** "...then reversed the cuts weeks later, admitting its assessment had not considered all the relevant business factors. The union pointed to rising call volumes the bot was not handling."
- **Status:** Applied on branch.

### Pattern 11 - Ford rehiring 350 engineers
- **Page says:** Ford "replaced experienced quality engineers with automated systems, watched quality failures emerge that the systems could not catch, and rehired 350 engineers - reclaiming its first top JD Power ranking since 2010..."
- **Verified:** Ford's VP of vehicle hardware engineering, Charles Poon, said Ford wrongly believed AI could replace experienced workers and quality suffered. Ford rehired, newly hired, or promoted about 350 experienced engineers. Ford ranked first among mainstream brands in JD Power's 2026 Initial Quality Study, its first top spot in 16 years. Sources: The Next Web, June 26, 2026 (https://thenextweb.com/news/ford-rehired-350-engineers-ai-quality-jd-power), Forbes, June 30, 2026 (https://www.forbes.com/sites/joetoscano1/2026/06/30/ford-hiring-350-engineers-after-ai-failed-shows-human-value-in-ai-era/). First reported by The Verge.
- **Problem:** Slight overstatement. Sources say Ford believed AI could replace experienced engineers and they left; not a documented one-for-one replacement. The 350 includes rehires, new hires, and promotions. "Top JD Power ranking" is among mainstream brands.
- **Fix:** "Ford believed AI could stand in for experienced quality engineers, watched quality suffer after they left, and brought back or added about 350 experienced engineers - then ranked first among mainstream brands in JD Power's 2026 Initial Quality Study, its first top spot in 16 years."
- **Status:** Applied on branch.

### Pattern 08 - OpenAI sycophancy rollback date
- **Page says:** "In May 2025, OpenAI was forced to roll back a GPT-4o update..."
- **Verified:** OpenAI's post "Sycophancy in GPT-4o: what happened and what we're doing about it" is dated April 29, 2025, and contains the quoted phrase. Fortune's coverage (the page's link) is May 1, 2025. Source: https://openai.com/index/sycophancy-in-gpt-4o/
- **Fix:** Change "May 2025" to "April 2025" in the body and attribution.
- **Convention note:** This is a direct quote. The site's convention is no direct quotes in "Inspired by" credits; a short quote from a company statement is a different case, but Greg should confirm it is acceptable.
- **Status:** Date applied on branch. Quote left as is pending Greg.

---

## Unsourced

### Pattern 04 - "Organizations that implement it at the team level... report the highest satisfaction with AI ROI."
- **Problem:** Reads as a survey finding but cites nothing. No source found.
- **Options:** Find a source, reframe as Greg's field observation ("In my experience..."), or cut.
- **Status:** Not changed - Greg to decide.

---

## Verified as written

| Pattern | Claim | Source |
|---|---|---|
| 07 | Chinese student study: homework scores +18%, completion time -30%, closed-book exam scores -20% within six months | Strömberg, Lei, Wu, "The Generative AI Learning Penalty: Evidence from Chinese Secondary Education," CEPR Discussion Paper DP21577, June 2026 (26,811 students, 30 months). https://cepr.org/publications/dp21577 - **Recommend adding this citation to the page; it currently names no source.** |
| 08 | OpenAI quote "overly flattering or agreeable" | OpenAI, April 29, 2025 (see date fix above) |
| 12 | Gallup: replacing an employee costs one-half to two times annual salary | Gallup, 2019. https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses-trillion.aspx |
| 12 | Gartner: 150,000+ agents per average global Fortune 500 enterprise by 2028 | Gartner press release, April 28, 2026. https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartner-identifies-six-steps-to-manage-artificial-intelligence-agent-sprawl |
| 09 | Spaced repetition produces stronger retention than single exposure | Well-established learning science; general claim, no specific figure. Acceptable without citation. |

---

## Not factual claims (no verification needed)

- Pattern 10: the 73% vs. 91% resource-utilization example is presented as a hypothetical ("Consider a program manager...").
- Pattern 12: the $120,000 role is labeled illustrative.
- Sample prompts in Patterns 01, 03, 05, 09, 10 are instructions, not claims.

---

## Recommendations

1. Add a source line to Pattern 07 for the Chinese student study.
2. Decide on Pattern 04's unsourced claim.
3. Confirm whether the OpenAI direct quote in Pattern 08 fits the site's quoting convention.
4. Rerun this check whenever a pattern moves from In Review to Published.
