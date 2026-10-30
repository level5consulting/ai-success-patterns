# Proposal - Contributors section, voting and comments (overnight, October 29-30, 2026)

Greg asked October 28: a Contributors section on aisuccesspatterns.com, a way to vote on what comes next, and possibly comments. Proposal only - branch contributors-proposal-2026-10-29; nothing on main. Mock page: contributors/index.html (not linked from the menu).

## 1. Contributors section

**Listed on the mock page (consent recorded in the records):**
| Person | Contribution | Patterns | Consent on record |
|---|---|---|---|
| Justin J MacBale | AI fails from missing context, data or nuance, not just hallucination; trust vs. validity | 03, 06 | Greg confirmed Oct 16 |
| Eric Olson | Core insight of Own the Thinking | 07 | Greg confirmed (records/07) |
| Max Meinke | The argument behind the Productivity-to-Headcount Trap | 11 | Greg confirmed Oct 16 |
| Louise Allen | Named example of an expert worth packaging (former Planview CTO) | 14 | Louise said yes Oct 18 |

**Flagged - credited on live pages, but no consent recorded in the repo:**
- **Scott Baker** - "Inspired by" credit is live on Pattern 17 (his Automation and AI Decision Tree). records/red-team-17.md says "credit pending Scott's consent." **17 publishes Monday - confirm Scott's consent before then, or remove the credit.**
- **Kent Beck** - "Inspired by" credit on 09 (BACKLOG item 11 plans credit on three humanistic patterns). No consent line recorded.
- **Sandra Loughlin, PhD** - "Inspired by" credit on 06 (and planned on 21). No consent line recorded.
If Greg has their OK, I'll record it and add them to the page.

**Not listed (credit pending consent):** Shubham Dwivedi (20), Fabio Moioli (22), Chen Y. (22), Tom Buyckx (23), Maribeth Achterberg (Free the Humans). **Michael Polanyi** (credited idea on 14) is a historical source, not a contributor - leave him on the pattern page only.

**Page copy (draft):** "These patterns come from practitioners. Each person below shaped a pattern with an idea, an example or a hard question - and agreed to be named." Each card: role (Contributor / Reviewer / Inspired by / Named example), name, one sentence, links to the patterns. Plus a "Contribute an idea" box and the voting box.

## 2. Voting on what comes next

| Option | Sign-in for voters | Privacy | Spam | Cost | How Greg reads results |
|---|---|---|---|---|---|
| **Microsoft Forms** (verified: "Anyone can respond" needs no sign-in; embeddable in a web page) | None | Responses stay in Greg's Microsoft 365 | Some risk with no sign-in; one-response limits need sign-in | Included in Greg's M365 | Forms results page / Excel export |
| Google Forms | None (optional) | Google account | Same | Free | Sheets |
| GitHub Discussions + giscus (reactions as votes) | GitHub account required (could not re-verify giscus.app tonight - permission prompt timed out) | Public on GitHub | Low | Free | Reactions count per discussion |
| Hosted poll widget (various) | Usually none | Third-party tracking/ads on free tiers | Varies | Free tier with branding, paid to remove | Vendor dashboard |
| claude.ai artifact with shared database | Viewers must be signed-in claude.ai users to write | Private to the artifact | Low | Included | Claude reads it directly into the Morning Review form |

**Recommendation: Microsoft Forms.** No sign-in for visitors (your audience is EPMO and executives, mostly without GitHub accounts), already paid for, results in Excel, embeds on the page. Form: one multi-select question listing the Coming Soon titles, optional "what's missing?" text, optional email. Weekly, I summarize results into the form and the Patterns Tracker.

## 3. Comments

- **None to start (recommended), plus a "Send feedback" Microsoft Form** on each pattern page: name optional, pattern pre-filled, comment, permission to quote/credit (yes/no - this also captures consent for credits).
- giscus later if a public discussion grows - needs GitHub sign-in and moderation (delete/lock in GitHub).
- Moderation: forms are private by default, so nothing appears publicly without Greg. Feed: the nightly run reads new responses (when an export is shared or Forms is reachable through the Microsoft 365 connector), files ideas in BACKLOG.md and puts anything needing a decision in the Morning Review form.

## 4. Build plan (rough)
1. Greg confirms the contributors list and the three flagged credits (Scott before Monday). - 10 min
2. Greg creates two Microsoft Forms (vote; feedback) - about 20 min with a draft question list from Claude. Forms creation isn't available through the connector here.
3. Claude builds the Contributors page from the mock, adds the vote embed, a "Contributors" menu link, and a "Send feedback" link on every pattern page - one overnight run.
4. Weekly vote summary into the form and tracker - ongoing, about 5 minutes per run.

## Questions for Greg
1. Contributors list: approve the four; do you have consent for Scott Baker, Kent Beck and Sandra Loughlin?
2. Voting: Microsoft Forms (recommended), Google Forms, giscus, or a poll widget?
3. Comments: none plus a feedback form (recommended), giscus, or skip?
4. When to build: next week, or after the PMO starter pack?

Sources: Microsoft Support, "Send a form and collect responses" - https://support.microsoft.com/en-us/forms/send-a-form-and-collect-responses
