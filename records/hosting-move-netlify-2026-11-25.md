# Site hosting move: GitHub Pages -> Netlify (decided Nov 25, 2026)

## Why (Greg)
- GitHub Pages deploys failed all of Nov 25 (artifact uploaded, deploy-pages couldn't fetch it - GitHub-side). Greg: "I think this is a sign to move off GitHub for site hosting. I have been thinking about that anyway."
- Greg: "I want to be able to have more things behind email gathering walls. I want simple. I want to keep GitHub as source and Chat is not your memory, ghost, ai ops, etc."

## Decisions
- 2026-11-25: Host on **Netlify**, connected to the GitHub repo (GitHub stays the source; publish rule unchanged - main deploys).
- 2026-11-25: Email gates use **HubSpot forms** (system of record; gated sign-ups land as contacts with their source). Netlify forms only as a backup.
- 2026-11-25: Night runs, records, Ghost in the Workflow, AI Operations Manager stay in GitHub - nothing moves but hosting.
- 2026-11-25: Schedule it for next week, about an hour with Greg in chat. Greg may do it today (Wed) or Fri Nov 27 if he has time.
- 2026-11-25: The upload-pages-artifact v3 -> v4 bump is on main (Greg: publish); it didn't fix the failure.

## Plan (with Greg, in chat)
1. Netlify: connect the repo; site runs on a Netlify test address beside the live site.
2. One HubSpot form on one gated item; test end to end (email -> delivery -> contact in HubSpot with source).
3. Point aisuccesspatterns.com at Netlify (domain DNS, managed in Microsoft 365); check the site and link previews (Post Inspector); keep GitHub Pages as fallback for a week, then turn it off.

## Open
- Which item goes behind the first gate? Candidates: ROI worksheets, the starter-pack handout, the full skill pack. (Greg to pick.)
- The link-preview redirect error (Nov 19) - recheck after the domain points at Netlify.

## Update - Nov 25, 3:27 PM
- Greg ran an LLM interview in ChatGPT on hosting; the output is saved word for word in records/hosting-handoff-chatgpt-interview-2026-11-25.md (source, not yet decisions).
- It recommends Cloudflare Workers first and Netlify second, plus a bigger reader flow: email verified with a one-time link, LLM choice, feedback, likes and "I used this" votes, all recorded in HubSpot.
- GitHub Pages recovered at 2:23 PM (the deploy retry worked), so the move isn't urgent.
- Open: Cloudflare or Netlify; the size of the first test (one gated pattern).

## Decision - Nov 25, 3:32 PM (Greg)
- Stay on GitHub Pages for now. No Netlify or Cloudflare move.
- Next week: test the simple path - a HubSpot form (email + LLM) on one pattern page, HubSpot emails the download link, the file lives in HubSpot's file manager, not the public repo. First check whether Greg's HubSpot tier includes the automatic follow-up email; if not, link on the thank-you page.
- The full reader flow from the ChatGPT interview (one-time links, votes, feedback) is parked as too complicated.
- Late December: follow-up interview with the consultant who interviewed Greg (reminder set for Mon Dec 28).
