# AI Success Patterns hosting and Night Shift handoff

## Purpose

Keep the Claude Night Shift publishing patterns from GitHub while planning for email-verified source and starter pack delivery, reader feedback, and consulting leads in HubSpot.

## Owner and status

Greg Stellflue wants to run the site himself and personally reviews every campaign email before sending. The Night Shift already generates and publishes patterns through the existing GitHub repository. GitHub Pages publishing was blocked during the discussion. Claude reported a possible internal GitHub error. Recovery and root cause were unverified. The new host, download flow, and HubSpot changes are proposals.

## How it works

- **Publishing today.** The Claude Night Shift uses the existing GitHub repository to generate and publish patterns. Keep that repository as the publishing source.
- **Reader flow planned.** A reader clicks **Use this pattern**, enters their email each time at launch, and chooses their LLM. After verifying their inbox through an expiring one-time link, they can copy or download the requested source or starter pack.
- **Reader feedback planned.** Capture pattern ideas and feedback, plus likes and **I used this** votes.
- **HubSpot planned.** Record the verified email, pattern, and LLM. Follow up with relevant patterns and an invitation to discuss the reader's needs. For someone who used The Night Shift and Ghost in the Workflow, ask whether it was easy to build the backlog and set up the records. Tailor campaigns for people who use multiple patterns.
- **Campaign review.** Greg helps build the email template, adds his personal touches, and reviews each campaign email before it sends. Have The Night Shift prepare campaign drafts for review. [Inferred - confirm] An automatic verification email using a template Greg approves is a separate proposal.

## Dependencies and access

- The current workflow depends on Claude, the existing [GitHub repository](https://github.com/level5consulting/ai-success-patterns), and GitHub Pages. The workflow's exact GitHub permissions are unverified.
- The proposed delivery service depends on a host that can run server-side code, a verification email sender, private files, and HubSpot. Use read-only GitHub App access scoped to a dedicated private download repository if the existing private customer repository contains other customer materials. The download repository and integration permissions are pending.
- The proposed service needs permission to record verified requests in HubSpot. The Night Shift's proposed HubSpot access covers campaign drafts and requires confirmation. Campaign sending remains subject to Greg's review.

## Hosting decision

| Option | Cost discussed | Fit |
| --- | --- | --- |
| Cloudflare Workers | Free tier. Paid starts at $5/month plus applicable usage. | First choice for serving the public site and running verification, delivery, and feedback code together. [Pricing](https://developers.cloudflare.com/workers/platform/pricing/) |
| Netlify | Free tier. Personal starts at $9/month. | Second choice. Deploy previews are available and the free plan pauses when monthly credits run out. [Pricing](https://www.netlify.com/pricing/) |
| Vercel Pro | Starts at $20/month plus applicable usage. | Revisit if the site moves to Next.js. Hobby is limited to personal, noncommercial use. [Pricing](https://vercel.com/pricing) |
| GitHub Pages | Current host | Static hosting. Keeping it would require a separate service for verified downloads and feedback. Paying for Pages would add private repository publishing but would leave those features to a separate service. [Limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |

The recommended first test is a Cloudflare preview on a temporary URL, with the production domain staying where it is during testing. If the repository is accessible, this can proceed independently of GitHub Pages publishing. Verify that a GitHub push deploys and existing pattern URLs work. Then test one pattern through verification, private delivery, and HubSpot before deciding whether to move the domain.

## Known limits and review

- Email verification establishes control of an inbox. Packs reserved for existing customers also need an eligibility check. Files exposed through the public repository or site can bypass the gate.
- The host recommendation is provisional. Preview deployment, verification, private delivery, and HubSpot permissions still need testing.
- Discussion captured November 25, 2026. Revisit when the preview results are in or when the host, repository access, email delivery, or campaign approval process changes. Update this record in the same session as any workflow change.
