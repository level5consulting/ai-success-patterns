# Plain-language review - aisuccesspatterns.com (branch overnight-2026-11-09)

Run: November 10, 2026, overnight. Findings only - no site file changed.
Asked for by Greg on Nov 5: "find places where the site is too tech talkie."
Method: Assemble the Team, with four non-technical readers:

- **Travel agent (TA)** - runs a small agency, uses ChatGPT for emails, has never opened a terminal.
- **Plant nursery general manager (GM)** - 40 staff, seasonal crews, spreadsheets yes, software jargon no.
- **HR director (HR)** - knows people processes, headcount and FTE language, but not IT terms.
- **Busy CEO on a phone (CEO)** - the adversarial voice. Stops reading at the first word they don't know.

## Summary

**Pages read: 40.** These were the home page; Services and its 3 ROI worksheet pages; the Sessions page and the 3 session READMEs; the starter-pack guide.html and 4 starter-pack READMEs (main, ChatGPT, ChatGPT plugin, Gemini); and all 26 pattern pages, including each "Use this pattern" prompt. I skipped mockups/, records/ and ops/.

**Pages with findings: 40.** Every page has at least one finding, but more than half have only light fixes. The pattern pages written most recently (Ten People, AI Friction, Staged Journey, Iterate) are already close to plain.

**The 3 worst pages:**
1. **Home (index.html).** The pop-up summaries behind the library cards for Onboard, Don't Program, Test Adversarially and The AI Operations Manager are the most technical text on the site, and they are the first thing a new visitor clicks. They also describe older versions of those patterns (see side notes).
2. **The AI Operations Manager.** It is written for people who already run AI agents ("agentic deployments", "tool-connected agents", "register the first agents").
3. **ChatGPT plugin README.** It tells the reader to use hidden folders, Terminal commands and a JSON file. No reader on the panel got past the second line.

The Night Shift and Ghost in the Workflow are close behind. Both are Start-here patterns, so they matter more than the in-review drafts.

**Most common offenders - fix these once, site-wide:**

| Term | Where | Fix once |
|---|---|---|
| **agent / agents** | Home pop-ups, AI Operations Manager, Ghost, Night Shift, Naughty List, Judge the Outcome, Services, ROI, starter packs | Define it the first time on each page: "an agent (an AI set up to do a job on its own, without you typing each step)". Elsewhere, "AI helper" or "AI tool" often works. |
| **Agentic / Conversational** (menu groups and home filter tabs) | Every page's menu, home filters | Rename the groups to plain words, e.g. "Runs on its own" and "In the chat". The CEO stopped at "Agentic" in the menu before reading any pattern. |
| **model / models / language model** (meaning "the AI") | About 15 pages | Say "the AI" or "AI tool". Keep "model" only where the difference between models matters (Right Tool, Right Job), and explain it there once. |
| **LLM** in "Avoid AI Slop with an LLM Interview" | Home, menu, pattern page, starter packs | Keep the name, but explain it once under the title: "LLM means large language model - the kind of AI behind ChatGPT, Claude and Copilot." |
| **sandbox, branch, staging, production, write access** | Night Shift, Naughty List, home pop-up | Say "a drafts folder or a practice copy - never the live version". |
| **script, code, query, Python** | Math, Naughty List, Dashboards, Judge the Outcome | Lead with "spreadsheet formula". Explain "script" once as "a short set of steps a computer runs, which a person can read and check first". |
| **skill, zip, unzip, SKILL.md, Customize > Skills, slugs like avoid-ai-slop-with-an-llm-interview** | Starter-pack guide and all READMEs | Explain "skill" once ("saved instructions your AI tool can run on request"), use pattern names instead of folder names, and move file names into a "for technical users" box. |
| **RAID log, RAG thresholds, PPM tool, EPMO, SPM** | Starter packs, Compressed Apprenticeship, Automate the Invisible, Dashboards | Spell each out once: RAID log (risks, assumptions, issues, dependencies), RAG (red/amber/green), PPM tool (portfolio software), EPMO (enterprise project management office). Note that "RAG" also means something else in AI, so spell it out. |
| **red team / red-teaming** | Test Adversarially, Night Shift, Chat Is Not Your Memory, starter packs | Explain it once on Assemble the Team (already done there) and use "challenge it" or "stress-test it" elsewhere. |
| **"Paste this into any AI system's custom instructions or at the start of a conversation"** | Every pattern page | Use one plain line site-wide: "Copy this and paste it at the start of a new chat in any AI tool." |
| **prompt text that says "skill", "invoked", "instantiate"** | Test Adversarially, Avoid AI Slop, Assemble the Team prompts | Visitors read these before they copy them. Say "these instructions" and "when you're asked to run this". |
| **Pattern numbers in body text** ("04 is...", "09 helps...", "red-team findings for 01-08") | Night Shift, Embed the Expert | Use the pattern names. |
| **Coinages a visitor can't decode** ("botwatch", "botcrap", "ore", "Taco 'bout") | AI as Amplifier, Judge the Outcome, AI Friction, Services | Either explain them on the page or drop them. |

**Side notes:** these are not plain-language findings, but the panel tripped on them while reading.

- **Judge the Outcome, Not the Craft:** the breadcrumb at the top of the page reads "Research Partner, Not All-Knowing Oracle" (line 164 of the HTML).
- **Home pop-ups are out of date:** the pop-ups for Onboard, Don't Program ("Write a job description... Treat the first week as a probationary period"), Test Adversarially ("Budget a minimum of half a day") and The AI Operations Manager ("manage the performance of every other AI agent in your stack") describe earlier versions of those patterns, not what the pages say now.
- **Stale "coming soon" labels:** several pages still mark patterns as "coming soon" that are now published or in review. Examples: Iterate to the Destination on Begin with the End in Mind; Redesign the Stream on The AI Operations Manager, Automate the Invisible and Staged Journey; Embed the Expert on Ghost in the Workflow; AI Friction on Automate the Invisible and Right Tool; Avoid the Naughty List on Redesign the Stream.
- **Menu count:** the menu says "All patterns 15", but 26 pattern pages exist (some are in review).
- **Starter-pack guide typo:** it says "a half-day Half-Day Session".

---

Pages appear below, worst first. Within each page, findings are also worst first. Quotes are the visible text, exactly as written. Reader codes: TA, GM, HR, CEO.

## 1. Home (index.html) - 8 findings (+4 more seen)

**Home 1.** "Treating AI agents as tools to program focuses on syntax - getting instructions right so the output looks correct." (pop-up: Onboard Don't Program, Problem)
- **Who trips and why:** CEO, TA, GM. "Agents", "program" and "syntax" all in the first line a curious visitor clicks.
- **Rewrite:** "Most people give AI a list of commands and hope the wording is right. It works on the example they tried and fails on the next one."

**Home 2.** "Create an AI agent whose explicit job is to manage the performance of every other AI agent in your stack." (pop-up: The AI Operations Manager, Solution)
- **Who trips and why:** CEO, all readers. It assumes the reader already runs several AI agents, and "stack" is IT slang. It also doesn't match the pattern page.
- **Rewrite:** "Give AI a standing job: the weekly status, the meeting prep, the follow-ups. Every result lands on one page you check."

**Home 3.** "You are building or deploying an AI agent - a persistent AI capability that will perform a job repeatedly over time. You are about to write instructions, configure parameters, or design a prompt chain." (pop-up: Onboard Don't Program, Context)
- **Who trips and why:** TA, GM, HR. "Deploying", "configure parameters" and "prompt chain" assume the reader builds software.
- **Rewrite:** "You're starting real work with AI - a project, a report, a recurring job - and you want it to understand your situation before it starts."

**Home 4.** "You have built a prompt, a chain, or an agent and it appears to be working." (pop-up: Test Adversarially, Context)
- **Who trips and why:** CEO. "Chain" and "agent" are undefined.
- **Rewrite:** "You have an AI answer, or an AI setup, that looks right, and you're about to rely on it."

**Home 5.** "Agentic 4" (menu group and filter tab, on every page)
- **Who trips and why:** CEO, GM. This is the first insider word on the site, and it sits in the menu.
- **Rewrite:** "Runs on its own 4" (and "In the chat 4" for Conversational).

**Home 6.** "In 1994, Gamma, Helm, Johnson, and Vlissides published Design Patterns - not to invent new programming concepts, but to name and codify patterns experienced developers were already using intuitively. Singleton. Observer. Factory. Decorator."
- **Who trips and why:** TA, GM, CEO. Four surnames and four programming terms before the point arrives.
- **Rewrite:** "In 1994, four software engineers wrote a book that gave names to habits good programmers already had. Those names became the shared language of their trade for thirty years."

**Home 7.** "Interview yourself first. It fills the backlog everything else runs on." (Start here, Step 1)
- **Who trips and why:** GM, CEO. "Backlog" is project-office talk, and "interview yourself" undersells the idea, which is that the AI interviews you.
- **Rewrite:** "Have AI interview you first. Your answers become the to-do list everything else runs on."

**Home 8.** "Avoid AI Slop with an LLM Interview" (Start here, Step 1 title)
- **Who trips and why:** CEO. "LLM" is the first acronym on the page, and it's never explained.
- **Rewrite:** keep the name, and add under it: "LLM means large language model - the kind of AI behind ChatGPT, Claude and Copilot."

**4 more seen on this page:**
- "You are about to use a chat-based AI model" (Begin with the End pop-up)
- "Asking AI to write the formula or script that calculates" (Math card)
- "AI brings the ability to automate to a whole new group of people."
- "AI Success Patterns · v0.1 · Public Domain" (version number and legal term in the footer)

## 2. The AI Operations Manager (patterns/04-ai-operations-manager.html) - 8 findings (+3 more seen)

**AI Ops 1.** "This pattern is the entry point for most agentic AI deployments in professional services."
- **Who trips and why:** CEO, all readers. Two insider terms in a section heading's opening line.
- **Rewrite:** "For most firms, this is the first job they hand to an AI that works on its own."

**AI Ops 2.** "The pattern extends naturally into tool-connected agents (calendar, email, project management) when those integrations are available."
- **Who trips and why:** TA, GM. "Tool-connected agents" and "integrations" are both undefined.
- **Rewrite:** "If your AI can connect to your calendar, email or project tools, it can do even more of this for you."

**AI Ops 3.** "Paste this into any AI system's custom instructions or at the start of a conversation to run The AI Operations Manager. It sets up an AI operations manager for your work: one dashboard where every agent reports its results, a simple way to add new agents, and the jobs it runs for you."
- **Who trips and why:** CEO. "Agents", three times in one line, without a definition.
- **Rewrite:** "Copy this and paste it at the start of a new chat. It sets up an AI operations manager: one page where every recurring AI job reports what it did, an easy way to add new jobs, and the jobs it runs for you."

**AI Ops 4.** "Define a recurring coordination role and assign it to AI as a persistent function - not a one-time task. The coordination tax on every knowledge worker's week drops substantially."
- **Who trips and why:** CEO, GM. This is the first line of the page, and it's abstract nouns all the way down.
- **Rewrite:** "Give AI a standing job - the weekly status, the meeting prep, the follow-ups - not a one-off favor. The busywork in everyone's week shrinks."

**AI Ops 5.** "Inside Anthropic, the share of employees’ AI sessions spent managing agents - writing instructions, building dashboards, monitoring pipelines - rose from 10% to 22% in about six months, and one engineer set up an “agent chief of staff” to triage agent requests (Wilmers, Catipon, Massenkoff and McCrory, “How Employment is Changing at Anthropic,” Anthropic, October 16, 2026)."
- **Who trips and why:** CEO, HR. One 60-word sentence with "pipelines", "triage" and "agent" twice.
- **Rewrite:** "At Anthropic, the company that makes Claude, the time staff spent managing their AI helpers more than doubled in six months. One engineer even set up an AI 'chief of staff' to sort the requests. That is this pattern, run for real."

**AI Ops 6.** "Multi-step workflows, project coordination, or any recurring process that involves organizing information, tracking status, routing tasks, or synthesizing inputs from multiple sources."
- **Who trips and why:** GM, TA. "Routing" and "synthesizing inputs" make a simple list sound technical.
- **Rewrite:** "Any work that repeats: tracking status, getting the right task to the right person, and pulling notes from several places into one summary."

**AI Ops 7.** "Async Updates" / "Route information to the right summary document or channel"
- **Who trips and why:** CEO, GM. "Async" is software slang, and "channel" assumes Slack or Teams.
- **Rewrite:** "Updates between meetings" / "Send each piece of news to the right summary or team chat."

**AI Ops 8.** "Explain how to add a new agent: write its one-line registration, add it to the list, and it reports to the dashboard with the same fields as every other agent." (prompt, Phase 4)
- **Who trips and why:** HR, TA. "Registration" and "fields" read like a database manual.
- **Rewrite:** "Explain how to add a new AI job: write one line saying what it does, when it runs and who owns it, add it to the list, and have it report on the same page as every other job."

**3 more seen:**
- "Synthesize project status from notes, emails, or tool exports"
- the image alt text "a sprint board"
- "Treat each session as a handoff, not a cold start."

## 3. ChatGPT plugin README (starter-packs/pmo-epmo-lead/chatgpt/plugin/README.md) - 5 findings

**Plugin 1.** "Unzip it into your home folder. On a Mac, in Terminal: `unzip ~/Downloads/pmo-chatgpt-plugin.zip -d ~`"
- **Who trips and why:** All four readers. It asks them to type a command into Terminal. The CEO and the TA both quit here.
- **Rewrite:** Put a box at the top: "This version is for technical users. Everyone else: use the paste-a-prompt route in the ChatGPT README - it takes two minutes and needs no setup." Keep the command below the box.

**Plugin 2.** "The zip holds two hidden folders that go in your home folder:"
- **Who trips and why:** TA, GM. "Hidden folders" and "home folder" are both unfamiliar, and hidden folders can't be seen without extra steps.
- **Rewrite:** "Technical setup: the download contains two hidden folders that need to go in your computer's home folder."

**Plugin 3.** "(If you already have a `~/.agents/plugins/marketplace.json`, don't overwrite it - add this plugin's entry to it.)"
- **Who trips and why:** All four. It assumes the reader can edit a JSON file.
- **Rewrite:** "(If you've installed other ChatGPT plugins this way before, ask whoever set them up to add this one, so the old ones keep working.)"

**Plugin 4.** "`.codex/plugins/ai-success-patterns-pmo/` - the plugin (plugin.json and the six skills)"
- **Who trips and why:** CEO. Folder paths and file names, with no plain description of what's in them.
- **Rewrite:** "The plugin itself: the six PMO skills, packaged for the ChatGPT desktop app."

**Plugin 5.** "Open Plugins, choose the "AI Success Patterns" marketplace, and install "ai-success-patterns-pmo"."
- **Who trips and why:** TA. The thing they're told to install has a code-style name.
- **Rewrite:** "Open Plugins, choose AI Success Patterns, and install the PMO starter pack." (If the app shows the code name, add: "it appears as ai-success-patterns-pmo".)

## 4. Ghost in the Workflow (patterns/12-ghost-in-the-workflow.html) - 8 findings (+5 more seen)

**Ghost 1.** "The person who built your AI workflow understood it. They knew why the prompt was worded that way, what the agent was never supposed to touch, and which outputs needed a second look."
- **Who trips and why:** CEO. "Workflow", "prompt" and "agent" all arrive in the opening two sentences, and none is defined.
- **Rewrite:** "The person who set up your AI process understood it. They knew why the instructions were worded that way, what the AI was never supposed to touch, and which results needed a second look."

**Ghost 2.** "That includes agents running on a schedule or triggered by events, prompts a team reuses, chat workflows built into how a process gets done, and any AI that touches business systems or data."
- **Who trips and why:** GM, TA. "Triggered by events" and "chat workflows" are developer phrasing.
- **Rewrite:** "That includes AI that runs on its own on a schedule, instructions a team copies and reuses, chats that are now part of how a job gets done, and any AI that can see or change company data."

**Ghost 3.** "Store it alongside the agent, prompt, or workflow it describes, wherever the team already keeps shared work, and version it with every change."
- **Who trips and why:** HR, GM. "Version it" is a developer verb.
- **Rewrite:** "Keep it next to the AI setup it describes, wherever your team keeps shared files, and save a new dated copy every time it changes."

**Ghost 4.** "Gartner's own guidance on agent sprawl calls for a central inventory and lifecycle rules."
- **Who trips and why:** CEO. "Agent sprawl" and "lifecycle rules" are analyst jargon.
- **Rewrite:** "Gartner says companies need one list of every AI agent they run, and rules for when each one gets reviewed and retired."

**Ghost 5.** "Security writers call these "orphaned agents" and focus on credentials that outlive their owners."
- **Who trips and why:** HR, TA. "Credentials" means logins, but says it less plainly.
- **Rewrite:** "Security writers call these 'orphaned agents' and worry most about logins and passwords that outlive the person who set them up."

**Ghost 6.** "A human verifies this against the actual system configuration - the AI knows what it was told it can reach, not necessarily what it can."
- **Who trips and why:** GM. "System configuration" is IT language.
- **Rewrite:** "Have someone check this against the real settings - the AI knows what it was told it can reach, not what it actually can."

**Ghost 7.** "An AI workflow's logic sits in its tuning history: the revisions, the rejected outputs, the conversations that shaped it. None of that is visible in the finished agent."
- **Who trips and why:** CEO. "Tuning history" is unfamiliar.
- **Rewrite:** "An AI setup's logic sits in how it got that way: the rewrites, the rejected answers, the conversations that shaped it. None of that shows in the finished setup."

**Ghost 8.** "Stay free to change models. When an AI workflow documents its purpose, inputs, prompts and owner outside any one tool, you can move it to a different model without rebuilding it from memory."
- **Who trips and why:** TA, CEO. "Models" is used for "AI tools".
- **Rewrite:** "Stay free to switch AI tools. When the record of what it does, what it uses and who owns it lives outside any one tool, you can move it without rebuilding it from memory."

**5 more seen:**
- "Nothing errors out."
- "Which data sources, policies, fields, and upstream processes it relies on."
- "buries it inside prompts and agent configurations"
- "reverse-engineering it"
- prompt text "a custom assistant, an agent, an automated workflow"

## 5. The Night Shift (patterns/15-the-night-shift.html) - 8 findings (+4 more seen)

**Night 1.** "Engineers solved this long ago. Overnight builds and batch jobs run unattended every night, and teams trust them because the work lands in staging behind a review gate, never straight into production."
- **Who trips and why:** All four readers. Five software terms in one sentence: builds, batch jobs, staging, review gate, production.
- **Rewrite:** "Factories and IT teams solved this long ago. Work runs overnight, but it lands in a holding area someone checks in the morning, never straight into the live system."

**Night 2.** "Unattended work can only reach a sandbox, a branch, or a drafts folder. It has no write access to anything live, so the speed doesn't cost you control."
- **Who trips and why:** CEO, TA, GM. "Sandbox", "branch" and "write access".
- **Rewrite:** "Overnight work can only touch a drafts folder or a practice copy - never the real thing. So the speed doesn't cost you control."

**Night 3.** "Give unattended work access only to a sandbox, a branch, or a drafts folder, never write access to live systems, and only the minimum access the task needs."
- **Who trips and why:** HR, GM. The same jargon again, in the step people actually follow.
- **Rewrite:** "Let overnight work see only what the task needs, and change only a drafts folder or a practice copy - never your live files, systems or customer records."

**Night 4.** "Treat everything the AI reads overnight - emails, web pages, documents - as data, not instructions."
- **Who trips and why:** CEO, TA. The words are plain, but the reason is missing, so it reads as code-speak.
- **Rewrite:** "Anything the AI reads overnight - emails, web pages, documents - could contain instructions someone planted. It reads them; it never follows them."

**Night 5.** "It is also not the same as The AI Operations Manager: 04 is recurring coordination work; this pattern is delegating substantive work and reviewing it later."
- **Who trips and why:** All four. A pattern number shows up as shorthand.
- **Rewrite:** "It's also not the same as The AI Operations Manager. That one runs the same coordination jobs every week; this one hands off real work and has you review it later."

**Night 6.** (Run 2) "A value report across every pattern, red-team findings for 01-08, a first draft of Embed the Expert, and speaking-venue research."
- **Who trips and why:** CEO. Pattern numbers and "red-team" are insider shorthand.
- **Rewrite:** "Run 2: A value report across every pattern, challenge reviews of the first eight patterns, a first draft of Embed the Expert, and research on where to speak."

**Night 7.** "A fair critique of "human in the loop" designs is that they leave the person at the start and the finish line, waiting, while the work happens without them - and that real collaboration means steering the work as it goes."
- **Who trips and why:** HR, CEO. The jargon "human in the loop", inside a 40-word sentence.
- **Rewrite:** "A fair criticism: in many AI setups the person only shows up at the start and the end, while the work happens without them. Real teamwork means steering as you go."

**Night 8.** "Offer a morning review dashboard: one page with one card per decision. If this AI can build pages or artifacts, build it as a page; if not, use the same structure as a numbered list in the morning summary." (prompt, Phase 4b; Phase 3 of the prompt also repeats "a sandbox, a branch")
- **Who trips and why:** TA. "Artifacts" is a Claude-specific term, and "diff" appears two lines later.
- **Rewrite:** "Offer a one-page morning review with one card per decision. If you can build a web page, do that; if not, use a numbered list."

**4 more seen:**
- "Hand off one task the first night, not a pipeline."
- "And it needs a place for results to wait for you: a branch, a draft folder, a review queue."
- "AI agent hours outnumbered employee hours 6 to 1"
- prompt "never a diff or comparison view"

## 6. PMO starter pack guide (starter-packs/pmo-epmo-lead/guide.html) - 8 findings (+1 more seen)

**Guide 1.** "Unzip the pack. Inside is one small zip per skill."
- **Who trips and why:** TA, GM, CEO. "Zip" twice, and it's the first instruction.
- **Rewrite:** "Open the download (double-click it). Inside are six small files, one per skill - leave those as they are."

**Guide 2.** "In Claude: download the Claude version, then Customize > Skills - upload the six skill zips; you can select all six in one step."
- **Who trips and why:** CEO. A menu path and file-format talk, with "skill" never defined.
- **Rewrite:** "In Claude: download the Claude version. Go to Customize, then Skills, and upload all six files at once. (A skill is a set of saved instructions Claude runs when you ask.)"

**Guide 3.** "Set up one Claude project per project you manage (one more for portfolio work), with a project record from The Chat Is Not Your Memory and one short chat per task, each ending the same way: ask for the agenda, update the record with it."
- **Who trips and why:** HR, CEO. A 45-word sentence that needs reading three times.
- **Rewrite:** "Make one Claude project for each project you manage, plus one for portfolio work. Keep a project record in each (The Chat Is Not Your Memory sets it up). Use one short chat per task, and end every chat the same way: ask for the agenda, then update the record with it."

**Guide 4.** "Any work that runs past one session. Decisions, sources and the RAID log live in a project record the AI reads first."
- **Who trips and why:** CEO, HR. "RAID log" is never explained. PMO leads know it; their sponsors may not.
- **Rewrite:** "Any work that runs past one chat. Decisions, sources and the RAID log (risks, assumptions, issues, dependencies) live in a project record the AI reads first."

**Guide 5.** "Portfolio health checks, report drafts and RAID reviews that can run while you're in meetings. Findings only - nothing changes in your PPM tool."
- **Who trips and why:** CEO. "PPM tool" is an unexplained acronym.
- **Rewrite:** "...Findings only - nothing changes in your project portfolio software."

**Guide 6.** "AI SUCCESS PATTERNS - PMO / EPMO LEAD STARTER PACK"
- **Who trips and why:** HR, CEO. Two acronyms in the title, never spelled out on the page.
- **Rewrite:** Keep the title, and add a subtitle: "For leaders of project management offices (PMOs) and enterprise PMOs (EPMOs)."

**Guide 7.** "For every AI prompt, agent or automation your PMO depends on - so it outlasts the person who built it."
- **Who trips and why:** CEO. "Agent" is undefined.
- **Rewrite:** "For every AI instruction set, AI helper or automated job your PMO depends on - so it outlasts the person who built it."

**Guide 8.** "Or a half-day Half-Day Session for your leadership team or PMI chapter."
- **Who trips and why:** CEO. The repeated words read as a mistake, and PMI is not spelled out (PMO leads know it).
- **Rewrite:** "Or a Half-Day Session for your leadership team or your local PMI (Project Management Institute) chapter."

**1 more seen:** "Who owns that agent - is there a record?"

## 7. PMO starter pack README (starter-packs/pmo-epmo-lead/README.md) - 7 findings

**Pack 1.** "**Claude Code:** `/plugin marketplace add level5consulting/ai-success-patterns`, then `/plugin install ai-success-patterns-pmo@ai-success-patterns`."
- **Who trips and why:** All four. Developer commands sit in the middle of the install list.
- **Rewrite:** Move it to the end, under "For developers using Claude Code:".

**Pack 2.** "**Claude (web, desktop):** download `pmo-claude-skills.zip`, unzip it, and go to Customize > Skills and upload the six skill zips from `claude/zips/` - you can select all six in one step."
- **Who trips and why:** TA, GM. File names and folder paths.
- **Rewrite:** "Claude (web or desktop app): download the Claude version and open it. Go to Customize, then Skills, and upload the six files inside - all at once is fine."

**Pack 3.** "The five Start-here AI Success Patterns as skills, each with a "For PMO and EPMO leads" section, plus a **pmo-start-here** guide."
- **Who trips and why:** CEO. "Skills" is undefined, and the guide is named like a file.
- **Rewrite:** "The five Start-here AI Success Patterns as skills (saved instructions your AI tool runs when you ask), each with a section for PMO and EPMO leads, plus a Start Here guide."

**Pack 4.** "In the project: a **project record** ..., **reference files** (charter, RAID log, last steering deck, templates) and **standing instructions** (report format, tone, RAG thresholds)."
- **Who trips and why:** HR, CEO. "RAID" and "RAG", and RAG also has a different, technical meaning in AI.
- **Rewrite:** "...(charter, RAID log of risks, assumptions, issues and dependencies, last steering deck, templates) and standing instructions (report format, tone, and what counts as red, amber or green)."

**Pack 5.** The skill table lists "avoid-ai-slop-with-an-llm-interview", "the-chat-is-not-your-memory", and so on.
- **Who trips and why:** CEO, TA. These are folder names, not pattern names.
- **Rewrite:** "Avoid AI Slop with an LLM Interview", "The Chat Is Not Your Memory", and so on.

**Pack 6.** "| assemble-the-team | Red-teaming a business case or prioritization decision |"
- **Who trips and why:** HR, GM. "Red-teaming" is undefined.
- **Rewrite:** "Assemble the Team | Hearing the tough questions (CFO, skeptical sponsor, delivery lead) before a business case or prioritization decision goes out"

**Pack 7.** "No projects on your plan? Keep the project record as a file and paste or attach it at the start of each chat."
- **Who trips and why:** TA. "Projects" here means a Claude feature, which isn't said.
- **Rewrite:** "Does your Claude plan not include Projects (folders that hold files and chats together)? Keep the project record as a document and attach it at the start of each chat."

## 8. Models Are Not Good at Math - But They Can Program (patterns/10-models-are-not-good-at-math.html) - 8 findings (+2 more seen)

**Math 1.** "Calculations are performed by a deterministic engine, not a probabilistic one - the same inputs produce the same outputs every time"
- **Who trips and why:** All four. "Deterministic" and "probabilistic" in a Value bullet.
- **Rewrite:** "The math is done by a spreadsheet, which gives the same answer every time - not by the AI, which makes its best guess."

**Math 2.** "Then run it yourself - in Excel, in Google Sheets, in Python, in whatever environment you have available. The model handles the logic. A deterministic engine handles the arithmetic."
- **Who trips and why:** GM, TA. "Python", "environment" and "deterministic engine".
- **Rewrite:** "Then run it yourself in Excel or Google Sheets. The AI writes the steps; the spreadsheet does the math."

**Math 3.** "Asking an AI to calculate is the wrong move. Asking an AI to write code that calculates is almost always the right one."
- **Who trips and why:** CEO, TA. The opening line tells non-coders the fix is code.
- **Rewrite:** "Asking AI to do the math is the wrong move. Asking it to write the spreadsheet formula that does the math is almost always the right one."

**Math 4.** "Models Are Not Good at Math - But They Can Program" (page title)
- **Who trips and why:** CEO, GM. "Models" and "program" in the title, for a pattern whose real advice is "use a formula".
- **Rewrite:** For Greg to decide: "AI Can't Do Math - But It Can Write the Formula". At minimum, add a subtitle: "Ask for the formula, not the answer."

**Math 5.** "The code is auditable - anyone can read the logic, challenge an assumption, and rerun it with different inputs"
- **Who trips and why:** GM. "Code" and "auditable".
- **Rewrite:** "Anyone can read the formula, question it, and rerun it with new numbers."

**Math 6.** "For most enterprise practitioners, the spreadsheet formula is the right default. If you need something more repeatable across data sets, a Python script adds that."
- **Who trips and why:** TA, GM. "Enterprise practitioners" and "Python script".
- **Rewrite:** "For most people, a spreadsheet formula is the right choice. If you'll run the same math on many files, ask a technical colleague about turning it into a small program."

**Math 7.** "Language models generate text."
- **Who trips and why:** CEO. "Language models" is never explained.
- **Rewrite:** "Tools like ChatGPT and Claude write text. They don't do math - they write what an answer usually looks like."

**Math 8.** "There, the model's probabilistic reasoning is appropriate."
- **Who trips and why:** HR, GM. "Probabilistic" again.
- **Rewrite:** "There, AI's best-guess reasoning is fine."

**2 more seen:**
- "One more step: After the script runs" (should say "formula")
- "This uses the model's pattern recognition strength rather than its arithmetic weakness."

## 9. Avoid the Naughty List (patterns/18-avoid-the-naughty-list.html) - 8 findings (+1 more seen)

**Naughty 1.** "Have AI audit the data, write cleanup scripts people can review and rerun, and send each owner the exact fixes they need."
- **Who trips and why:** GM, TA, CEO. "Scripts" in the opening line, with no explanation.
- **Rewrite:** "Have AI check the data, write the fixes as step-by-step instructions someone can read before they run, and send each owner the exact fixes they need."

**Naughty 2.** "Give it an export or a read-only view, in a tool your organization has approved, with any personal data the audit doesn't need removed or masked."
- **Who trips and why:** GM, HR. "Read-only view" and "masked".
- **Rewrite:** "Give it a copy of the data that it can look at but not change, in a tool your company has approved. Remove or hide any personal details it doesn't need."

**Naughty 3.** "Every script does a dry run first - reporting what would change, with a count and a sample - and has a way to undo."
- **Who trips and why:** TA. "Script" and "dry run".
- **Rewrite:** "Every fix does a practice run first - showing what would change, how many records, and a few examples - and has a way to undo it."

**Naughty 4.** "It is not a way to let AI change production data on its own."
- **Who trips and why:** CEO, GM. "Production data" is IT talk for "the real records".
- **Rewrite:** "It is not a way to let AI change your real records on its own."

**Naughty 5.** "For problems that can be fixed by rule - formats, duplicates, obvious mappings - ask for a cleanup script, not direct edits."
- **Who trips and why:** HR, GM. "Mappings" and "script".
- **Rewrite:** "For problems with a clear rule - formats, duplicates, obvious matches like 'WI' to 'Wisconsin' - ask for a fix someone can check first, not direct edits."

**Naughty 6.** "Have an agent watch the log and send the reminders (The AI Operations Manager), so nobody has to chase."
- **Who trips and why:** CEO. "Agent" is undefined.
- **Rewrite:** "Have AI watch the log and send the reminders (The AI Operations Manager), so nobody has to chase."

**Naughty 7.** "Instead of AI editing records directly, it writes a cleanup script people can read, test, and run again next time (the same principle as Models Are Not Good at Math - But They Can Program: have the model write code, not do the work in its head)."
- **Who trips and why:** TA, CEO. A long sentence that ends in "code" and "model".
- **Rewrite:** "Instead of AI editing records directly, it writes the fix as steps people can read, test and run again next time. Same idea as Models Are Not Good at Math: have AI write the steps, not do the work in its head."

**Naughty 8.** "Use the audit to see which errors keep coming back and where they start - a form, an integration, a missing default - and fix that."
- **Who trips and why:** GM. "Integration" and "default".
- **Rewrite:** "...where they start - a form, a link between two systems, a blank that should be filled in automatically..."

**1 more seen:** "AI changing records directly" vs "point a tool at the database" (fine on its own, but it adds to the tech tone).

## 10. ChatGPT README (starter-packs/pmo-epmo-lead/chatgpt/README.md) - 6 findings

**ChatGPT 1.** "Skills use the open Agent Skills format: a folder with a SKILL.md file."
- **Who trips and why:** All four. A file format name, in the second sentence.
- **Rewrite:** "Each skill is a small folder of written instructions ChatGPT can use."

**ChatGPT 2.** "Each skill still works as a prompt. Open `skills/<name>/SKILL.md`, copy everything below the top block, and paste it at the start of a chat."
- **Who trips and why:** TA, GM. A placeholder path and "top block".
- **Rewrite:** "Each skill still works if you just paste it. Open the skill's folder, open the file inside, copy everything below the short header at the top, and paste it at the start of a chat."

**ChatGPT 3.** "Download `pmo-chatgpt-skills.zip` and unzip it. Inside are six small zips, one per skill. Don't unzip those."
- **Who trips and why:** CEO. "Zip" four times.
- **Rewrite:** "Download the ChatGPT version and open it. Inside are six small files, one per skill. Upload those as they are."

**ChatGPT 4.** "ChatGPT can pick a skill on its own, or you can @-mention one."
- **Who trips and why:** HR, TA. "@-mention" is chat-app slang.
- **Rewrite:** "ChatGPT can pick a skill on its own, or you can type @ and the skill's name."

**ChatGPT 5.** "In the project: a **project record**, **reference files** (charter, RAID log, last steering deck, templates) and **standing instructions** (report format, tone, RAG thresholds)."
- **Who trips and why:** CEO, HR. Same issue as Pack 4.
- **Rewrite:** Same as Pack 4.

**ChatGPT 6.** "On Plus and other personal plans, use the plugin instead: see `plugin/README.md` and download `plugin/pmo-chatgpt-plugin.zip`."
- **Who trips and why:** TA. It sends a non-technical reader to the hardest route.
- **Rewrite:** "On Plus and other personal plans, the easiest route is pasting each skill (above). A plugin version exists for technical users - see the plugin folder."

## 11. Gemini README (starter-packs/pmo-epmo-lead/gemini/README.md) - 5 findings

**Gemini 1.** "Skills use the open Agent Skills format: a folder with a SKILL.md file."
- **Who trips and why:** All four.
- **Rewrite:** "Each skill is a small folder of written instructions Gemini can use."

**Gemini 2.** "Open `skills/<name>/SKILL.md`, copy everything below the top block, and paste it at the start of a chat."
- **Who trips and why:** TA, GM.
- **Rewrite:** Same as ChatGPT 2.

**Gemini 3.** "Download `pmo-gemini-skills.zip` and unzip it. Inside are six folders, one per skill. Keep the folder names as they are."
- **Who trips and why:** CEO.
- **Rewrite:** "Download the Gemini version and open it (double-click). Inside are six folders, one per skill. Don't rename them."

**Gemini 4.** "In that folder: a **project record**, **reference files** (charter, RAID log, last steering deck, templates) and **standing instructions** (report format, tone, RAG thresholds)."
- **Who trips and why:** CEO, HR.
- **Rewrite:** Same as Pack 4.

**Gemini 5.** "One short chat per task. Attach the record, do the job, ask for the agenda, and update the record with it. The agenda opens the next chat."
- **Who trips and why:** HR. "The agenda opens the next chat" is insider shorthand.
- **Rewrite:** "...ask for the agenda, update the record with it, and paste that agenda in to start your next chat."

## 12. Services (services/index.html) - 8 findings (+2 more seen)

**Services 1.** "Governance built in: who owns each AI tool and agent, and what it can reach."
- **Who trips and why:** CEO, GM. "Governance" and "agent" in a line about what the buyer is paying for.
- **Rewrite:** "Clear ownership built in: who is responsible for each AI tool or AI helper, and what company information it can see."

**Services 2.** "Training stops at the individual. Patterns go to the team and the process. Cutting people after a productivity gain. Scaling a pilot that works 80% of the time. Nobody owning the agent."
- **Who trips and why:** CEO. Three sentence fragments, and the last ends in "agent".
- **Rewrite:** "Training stops at the individual. Patterns cover the team and the process: whether to cut staff after a productivity gain, whether to roll out a pilot that works 80% of the time, and who owns each AI tool."

**Services 3.** "Training says "give it context." Patterns show how. Onboard, Don't Program is five parts and a playback, so you can see what the AI understood before it starts."
- **Who trips and why:** TA, GM. "A playback" is insider shorthand.
- **Rewrite:** "...Onboard, Don't Program is a five-part brief, and the AI repeats it back in its own words before it starts."

**Services 4.** "Not included: IT or security setup, licenses, custom integrations."
- **Who trips and why:** GM, TA. "Integrations".
- **Rewrite:** "Not included: IT or security setup, software licenses, or connecting AI to your other systems."

**Services 5.** "The starter pack installed and tuned to your team's work and words."
- **Who trips and why:** CEO. "Starter pack" is never defined on this page.
- **Rewrite:** "The starter pack - ready-made AI instructions for your role - set up and tuned to your team's work and words."

**Services 6.** "For a team lead - PMO first"
- **Who trips and why:** TA, GM, CEO. "PMO" is an unexplained acronym in a section label.
- **Rewrite:** "For a team lead - starting with project offices (PMOs)"

**Services 7.** "A half-day, live session in the style of A Ten-Minute Taco 'bout AI, with those patterns run on your group's own work."
- **Who trips and why:** CEO. An insider show name with no link or explanation.
- **Rewrite:** "A half-day live session in the style of Greg's weekly ten-minute show, with those patterns run on your group's own work."

**Services 8.** "At Planview Connect, I led a Practical AI workshop where everyone left with 3 usable prompts."
- **Who trips and why:** TA, GM. "Planview Connect" is unknown outside project-office circles, and "prompts" is undefined.
- **Rewrite:** "At Planview Connect, a project management conference, I led a hands-on AI workshop where everyone left with three AI instructions they could use the next day."

**2 more seen:**
- "Not ready yet? Start with the free Start-here path, or watch a ten-minute session. Bringing back the past to help our future." (The tagline lands mid-paragraph and reads like a stray sentence.)
- "In 6 months your teams will be talking a new language and delivering value you never could have imagined." (Hype, not jargon, but the CEO discounted the page here.)

## 13. Test Adversarially (patterns/03-test-adversarially.html) - 7 findings

**Test 1.** "## What this skill does" / "When invoked, examine the output to be tested - either the most recent AI-generated output in this session, or whatever the user pastes in - and run an adversarial review using the appropriate lenses." (prompt)
- **Who trips and why:** TA, CEO. "Skill" and "invoked" are the first words they see after clicking View instructions.
- **Rewrite:** "## What these instructions do" / "When the user asks you to run this, take the answer to be tested - your most recent answer, or whatever the user pastes in - and challenge it using the checks that fit."

**Test 2.** "There is a second failure mode that is harder to catch: the model can be wrong not because it hallucinated, but because it never had what it needed."
- **Who trips and why:** CEO, GM. "Hallucinated" and "failure mode".
- **Rewrite:** "There's a second problem that's harder to catch: the AI can be wrong not because it made something up, but because it never had what it needed."

**Test 3.** "Fluency is a style property, not an accuracy signal."
- **Who trips and why:** HR, GM. Abstract.
- **Rewrite:** "Sounding good tells you about the writing, not the facts."

**Test 4.** "AI models are optimized to be helpful and fluent."
- **Who trips and why:** CEO. "Models" and "optimized".
- **Rewrite:** "AI tools are built to sound helpful and smooth."

**Test 5.** "Treat the critique as a list of leads, not a verdict: research from Google DeepMind found that models struggle to correct their own reasoning without outside feedback, and sometimes make it worse (Huang et al., ICLR 2024)."
- **Who trips and why:** CEO. A long sentence with two names they don't know.
- **Rewrite:** "Treat the critique as a list of leads, not a verdict. Google researchers found AI is poor at catching its own mistakes without outside input - and sometimes makes them worse."

**Test 6.** "Building verification into the workflow itself is the structural version, and a candidate for a future pattern."
- **Who trips and why:** HR, GM.
- **Rewrite:** "Building the checks into the process itself is the bigger fix, and a likely future pattern."

**Test 7.** "Run the adversarial review in a fresh session by default."
- **Who trips and why:** TA. "Adversarial review" and "session".
- **Rewrite:** "Run the challenge in a brand-new chat."

## 14. Begin with the End in Mind (patterns/01-begin-with-end-in-mind.html) - 6 findings

**Begin 1.** "The user iterates. Tokens accumulate. Quality drifts. Time is lost."
- **Who trips and why:** All four. "Tokens" is pure insider vocabulary.
- **Rewrite:** "You go back and forth. Each round costs time. The quality drifts."

**Begin 2.** "Applies at the start of a conversation, prompt sequence, or agentic workflow."
- **Who trips and why:** CEO, TA.
- **Rewrite:** "Use it at the start of any AI chat, or any job you hand AI to run on its own."

**Begin 3.** "Then give the task. The model aligns its generation to the destination, not just the request."
- **Who trips and why:** GM, HR.
- **Rewrite:** "Then give the task. The AI aims at what you described, not just at what you asked for."

**Begin 4.** "Any technique that helps specify the desired output before prompting is an instance of this pattern."
- **Who trips and why:** HR.
- **Rewrite:** "Anything that pins down what you want back before you ask counts as this pattern."

**Begin 5.** "Define what "done" looks like before you describe what you want AI to do. A common source of wasted iterations isn't bad prompts - it's no destination."
- **Who trips and why:** CEO. "Iterations" in the opening line.
- **Rewrite:** "Define what 'done' looks like before you tell AI what to do. Most wasted back-and-forth isn't bad wording - it's no destination."

**Begin 6.** "Do not over-engineer the intake; the goal is a clear destination, not a completed form" (prompt, Behavior rules)
- **Who trips and why:** TA.
- **Rewrite:** "Keep the questions light; the goal is a clear destination, not a filled-in form."

## 15. The Compressed Apprenticeship (patterns/09-compressed-apprenticeship.html) - 8 findings

**Apprentice 1.** "A strong engineer asked to lead a portfolio-level initiative is junior to the EPMO norms they have not lived yet."
- **Who trips and why:** All four. "EPMO" is never explained.
- **Rewrite:** "A strong engineer asked to lead a company-wide project is a junior in how the project office runs."

**Apprentice 2.** "Organizations are deploying AI at the productivity layer while leaving the development layer untouched."
- **Who trips and why:** CEO, GM.
- **Rewrite:** "Companies use AI to get work done faster, and skip using it to make their people better."

**Apprentice 3.** "Practitioners who study AI-narrated work and repeat it across spaced intervals develop durable skill - not just familiarity with the output."
- **Who trips and why:** HR, GM.
- **Rewrite:** "People who study how the AI reasoned, then try the same kind of task again a few weeks later, keep the skill."

**Apprentice 4.** "The compressed apprenticeship compresses the transferable portion of what mentorship provides - the domain reasoning, the tradeoff logic, the failure modes. The situated, contextual portion still requires human mentors."
- **Who trips and why:** CEO.
- **Rewrite:** "AI can teach the general part of what a mentor knows - how to reason about the work, which tradeoffs matter, what usually goes wrong. The part that's about your company and your people still needs a human mentor."

**Apprentice 5.** "Beck's work on Extreme Programming and software craftsmanship has long emphasized that how you build matters as much as what you build."
- **Who trips and why:** TA, GM. It assumes the reader knows software methods.
- **Rewrite:** "Beck, a software pioneer, has long argued that how you build matters as much as what you build."

**Apprentice 6.** "The feedback loop that produces competence runs at the speed of whoever has the most competing demands on their time."
- **Who trips and why:** HR.
- **Rewrite:** "So you learn at the speed of the busiest person you know."

**Apprentice 7.** "This surfaces the load-bearing choices rather than leaving you to guess what matters."
- **Who trips and why:** GM.
- **Rewrite:** "This shows you the calls that hold the whole thing up, so you don't have to guess what matters."

**Apprentice 8.** "Visual coming. The image will show the expertise gap between senior and junior practitioners, and the AI-enabled bridge between them."
- **Who trips and why:** CEO. A placeholder in consultant-speak.
- **Rewrite:** "Picture coming: a senior expert, a junior colleague, and AI helping close the gap."

## 16. Own the Thinking (patterns/07-own-the-thinking.html) - 6 findings

**Own 1.** "AI used in the articulation layer builds on your capability. AI used in the discovery and synthesis layer substitutes for it."
- **Who trips and why:** All four. The opening line is the most abstract sentence on the site.
- **Rewrite:** "Use AI to help you say what you already worked out, and you get stronger. Use it to work things out for you, and you get weaker."

**Own 2.** "When AI is in the synthesis loop, it earns the learning. You get the output. It keeps the lesson."
- **Who trips and why:** CEO.
- **Rewrite:** "When AI does the figuring out, it gets the lesson. You get the document."

**Own 3.** "Keep AI in the articulation layer" (Solution heading)
- **Who trips and why:** TA, GM.
- **Rewrite:** "Let AI help you say it, not think it"

**Own 4.** "This isn't a failure of AI. It's a failure of how AI is positioned in the workflow."
- **Who trips and why:** HR.
- **Rewrite:** "This isn't a failure of AI. It's a failure of where we use it in the work."

**Own 5.** "AI accelerates output without quietly degrading the expertise behind it - the gap the CEPR study found, where better homework came with 20% lower exam scores"
- **Who trips and why:** CEO. "CEPR" is an unexplained acronym.
- **Rewrite:** "...the gap the student study found, where better homework came with 20% lower exam scores"

**Own 6.** "Any professional context where AI assistance is available and the goal is not just producing output - but retaining and building the capability to produce that output independently."
- **Who trips and why:** HR, CEO. Long and abstract.
- **Rewrite:** "Any work where you need to get better at the job, not just get the job done."

## 17. Redesign the Stream, Not the Role (patterns/21-redesign-the-stream-not-the-role.html) - 7 findings

**Stream 1.** "It fits work that crosses roles and teams: order to cash, quote to contract, intake to delivery, hire to productive, incident to resolution."
- **Who trips and why:** TA, GM. Process-consultant shorthand.
- **Rewrite:** "It fits work that passes between teams: from a customer's order to getting paid, from a quote to a signed contract, from a new hire to someone fully up to speed."

**Stream 2.** "We used AI to answer RFP questions, and it was great - that part got much faster."
- **Who trips and why:** GM, HR. "RFP" is never spelled out.
- **Rewrite:** "We used AI to answer RFP questions (the long questionnaires buyers send vendors), and that part got much faster."

**Stream 3.** "Use it when an organization is planning AI-driven work redesign, an operating-model change, or role changes tied to AI - and when AI tools are already deployed but the business results haven't followed."
- **Who trips and why:** CEO.
- **Rewrite:** "Use it when you're planning to change jobs or teams because of AI - or when everyone has AI tools and the business results haven't followed."

**Stream 4.** "Start with a tiger team."
- **Who trips and why:** TA, HR.
- **Rewrite:** "Start with one small, hand-picked team."

**Stream 5.** "None of this is new. Lean teams have mapped value streams for decades."
- **Who trips and why:** TA, CEO. "Lean" is unexplained.
- **Rewrite:** "None of this is new. Manufacturers have mapped how work flows from order to delivery for decades."

**Stream 6.** "The invisible work gets seen - handoffs, workarounds and tacit knowledge show up on the map, so they get fixed or protected instead of broken."
- **Who trips and why:** GM.
- **Rewrite:** "...handoffs, workarounds and the know-how only some people have show up on the map..."

**Stream 7.** "Data is usually the hidden barrier. Mapping the stream often shows that the data feeding it is the biggest obstacle - and the biggest unlock. Avoid the Naughty List, covers it (coming soon)."
- **Who trips and why:** CEO. "Unlock" is jargon, there's a stray comma, and the "coming soon" label is stale.
- **Rewrite:** "...the biggest obstacle - and the biggest opportunity. Avoid the Naughty List covers it."

## 18. Avoid AI Slop with an LLM Interview (patterns/05-avoid-ai-slop.html) - 7 findings

**Slop 1.** "Avoid AI Slop with an LLM Interview" (title)
- **Who trips and why:** CEO. "LLM" is never explained anywhere on the page.
- **Rewrite:** Add under the title: "LLM means large language model - the kind of AI behind ChatGPT, Claude and Copilot."

**Slop 2.** "## What this skill does" / "This skill runs in three phases. Do not skip or merge them." (prompt; later "## If invoked after a draft already exists")
- **Who trips and why:** TA.
- **Rewrite:** "## What these instructions do" / "This runs in three phases..." / "## If the user already has a draft"

**Slop 3.** "When you hand AI a content task, it generates from its training data - patterns, structures, and phrasings it has seen thousands of times."
- **Who trips and why:** GM, CEO. "Training data".
- **Rewrite:** "When you ask AI to write something, it writes from everything it has read - phrasings it has seen thousands of times."

**Slop 4.** "This pattern is a specific instance of Begin with the End in Mind (Begin with the End in Mind): the "interview first" step defines the content's actual source material before generation begins."
- **Who trips and why:** HR. Doubled name and jargon.
- **Rewrite:** "This is a version of Begin with the End in Mind: the interview decides what the content is built from before any writing starts."

**Slop 5.** "Variation: Run the interview in a fresh session without providing the presentation brief first. This surfaces what you actually know versus what you think you know about the topic - a useful gap analysis before any high-stakes delivery."
- **Who trips and why:** GM.
- **Rewrite:** "Variation: run the interview in a new chat without telling the AI what the talk is for. You'll find out what you actually know versus what you think you know - useful before any big presentation."

**Slop 6.** "The result is technically correct, well-organized, and completely indistinct."
- **Who trips and why:** TA. "Indistinct" is an odd word choice.
- **Rewrite:** "The result is correct, well-organized, and forgettable."

**Slop 7.** "Now draft [the content] using only what I told you in my answers. Do not add information I didn't provide. Mirror my language and level of specificity. Flag any section where you're synthesizing beyond what I said."
- **Who trips and why:** GM, TA. This is the prompt the reader copies, and "synthesizing" is the one hard word in it.
- **Rewrite:** "...Flag any part where you went beyond what I said."

## 19. Onboard, Don't Program (patterns/02-onboard-dont-program.html) - 6 findings

**Onboard 1.** "This pattern scales into persistent system prompts for teams and organizations."
- **Who trips and why:** All four.
- **Rewrite:** "For a team, the same document becomes standing instructions that every person's AI starts from."

**Onboard 2.** "This isn't programming or jailbreaking - and it isn't instead of clear instructions."
- **Who trips and why:** CEO, HR. "Jailbreaking".
- **Rewrite:** "This isn't coding or tricking the AI - and it doesn't replace clear instructions."

**Onboard 3.** (Constraints) "Budget, timeline, technology stack, regulatory environment"
- **Who trips and why:** GM, TA. "Technology stack".
- **Rewrite:** "Constraints: budget, timeline, the tools you use, the rules you work under"

**Onboard 4.** (Who I am) "EPMO director at a 4,000-person manufacturer; 15 years in portfolio management"
- **Who trips and why:** TA, GM. "EPMO" is unexplained in the example.
- **Rewrite:** "Who I am: Head of the project office at a 4,000-person manufacturer; 15 years running project portfolios"

**Onboard 5.** "Extended AI-assisted work sessions where the model needs to understand your context, role, constraints, and preferences before producing useful output."
- **Who trips and why:** CEO.
- **Rewrite:** "Longer AI work where the AI needs to know who you are and what you're up against before it can help."

**Onboard 6.** "Treat AI like a new team member, not a search engine. The investment in context at the start pays forward across every interaction in the session."
- **Who trips and why:** HR. "Session" and "interaction".
- **Rewrite:** "...A few minutes of context at the start pays off in every answer after it." (The prompt already says it this way.)

## 20. Assemble the Team (patterns/08-assemble-the-team.html) - 6 findings

**Team 1.** "This isn't a flaw - it's the architecture. In April 2025, OpenAI was forced to roll back a GPT-4o update after acknowledging the model had become "overly flattering or agreeable." They called it sycophantic."
- **Who trips and why:** CEO, TA. "Architecture", "roll back", "GPT-4o" and "sycophantic".
- **Rewrite:** "This isn't a glitch - it's how these tools are built. In April 2025, the company behind ChatGPT pulled an update because it had become 'overly flattering or agreeable.'"

**Team 2.** "When one person uses AI alone, the model is working with a single framing, a single set of assumptions, and an optimization toward completing the request."
- **Who trips and why:** GM.
- **Rewrite:** "When you use AI alone, it sees the problem one way - yours - and it's built to finish the job, not question it."

**Team 3.** "If the skill is invoked at or near the start of a session with no prior context, note briefly that this pattern works best with a clear goal, then ask what the user is working on." (prompt)
- **Who trips and why:** TA.
- **Rewrite:** "If you're asked to run this at the very start of a chat, say it works best with a clear goal, then ask what the user is working on."

**Team 4.** "The user is always The Human - never instantiate that as an AI voice." (prompt)
- **Who trips and why:** CEO. "Instantiate".
- **Rewrite:** "The user is always The Human - never play that role yourself."

**Team 5.** "It pays the biggest dividend in early-stage thinking, when the framing is still forming and a bad assumption will propagate through everything that follows."
- **Who trips and why:** GM.
- **Rewrite:** "It pays most early on, while the idea is still forming and a bad assumption would spread into everything after it."

**Team 6.** "Parallel takes only - voices respond to the work, not to each other" (prompt, Behavior rules)
- **Who trips and why:** HR.
- **Rewrite:** "Each voice reacts to the work on its own - not to the other voices"

## 21. Dashboards That Answer a Question (patterns/24-dashboards-that-answer-a-question.html) - 6 findings

**Dash 1.** "We built very fancy dashboards with AI to demonstrate our SPM solutions."
- **Who trips and why:** All four. "SPM" is never explained.
- **Rewrite:** "We built very fancy dashboards with AI to show off our portfolio management software."

**Dash 2.** "The figures come from code or queries the AI writes against the source data - never from the AI's own arithmetic (Models Are Not Good at Math - But They Can Program)."
- **Who trips and why:** GM, TA. "Queries".
- **Rewrite:** "The numbers come from formulas the AI writes and your spreadsheet or reporting tool runs - never from the AI's own arithmetic."

**Dash 3.** "Have AI write the code, not the numbers." (Step 4 heading)
- **Who trips and why:** TA.
- **Rewrite:** "Have AI write the formulas, not the numbers."

**Dash 4.** "Numbers you can trust - every figure shows where it came from, and it's checked against its source before first use and again after any change to its query."
- **Who trips and why:** GM.
- **Rewrite:** "...checked against its source before first use and again whenever the formula behind it changes."

**Dash 5.** "PMOs know this one well."
- **Who trips and why:** TA, GM. "PMO" is not spelled out on this page.
- **Rewrite:** "Project offices (PMOs) know this one well."

**Dash 6.** "This library's own example. The Patterns Tracker answers "what's published, in review and coming?" Plans in Motion answers "what needs me this week?""
- **Who trips and why:** CEO. Internal tool names the reader can't see.
- **Rewrite:** "This library's own example: one page answers 'what's published, in review and coming?' Another answers 'what needs me this week?'"

## 22. The Productivity-to-Headcount Trap (patterns/11-productivity-to-headcount-trap.html) - 6 findings

**Trap 1.** "Multiply by headcount, convert to FTEs, present to the board as ROI."
- **Who trips and why:** GM, TA. "FTEs" (HR and the CEO are fine with it).
- **Rewrite:** "Multiply by headcount, turn it into full-time jobs, and present it to the board as savings."

**Trap 2.** "This is also a governance question, not just an operational one. Organizations that treat AI workforce impact as a finance decision rather than a redesign decision are making structural choices without structural analysis."
- **Who trips and why:** CEO.
- **Rewrite:** "This is a leadership question, not just a finance one. Cutting jobs before you've redesigned the work is a big decision made on a small amount of analysis."

**Trap 3.** "The edge cases, exception loads, and validation demands of a newly automated process are still being discovered."
- **Who trips and why:** GM.
- **Rewrite:** "The odd cases, the exceptions and the checking a new process needs are still turning up."

**Trap 4.** "That includes board-level ROI discussions where FTE savings are the primary metric, CFO requests for workforce impact modeling, and transformation programs where productivity gains are being translated directly into staffing targets."
- **Who trips and why:** TA, GM.
- **Rewrite:** "That includes board talks where jobs saved is the main number, a CFO asking how many roles AI will cut, and programs that turn time saved straight into staffing targets."

**Trap 5.** "Account for the work that is genuinely new: AI oversight, output validation, exception escalation, and the customer or stakeholder interactions the AI cannot handle."
- **Who trips and why:** GM.
- **Rewrite:** "Count the work that's new: watching the AI, checking its output, handling what it gets stuck on, and the customer conversations it can't have."

**Trap 6.** "...specifically on moving organizations from AI pilots to genuine organizational capability through process redesign and operational change management." (contributor note)
- **Who trips and why:** CEO.
- **Rewrite:** "...helping companies turn AI trials into everyday practice by redesigning how the work gets done."

## 23. Automate the Invisible (patterns/13-automate-the-invisible.html) - 7 findings

**Invisible 1.** "Map one end-to-end process, from request to resolution, using value-stream mapping."
- **Who trips and why:** TA, GM. "Value-stream mapping" is unexplained.
- **Rewrite:** "Pick one process and follow it from the customer's request to the finish, step by step."

**Invisible 2.** "Before anything changes, measure what each candidate costs today: cycle time, days in queue, touches per transaction, rework hours, repeat contacts."
- **Who trips and why:** GM, HR. A string of operations metrics.
- **Rewrite:** "Before anything changes, measure what each one costs today: how long it takes, how long it waits, how many people handle it, how much gets redone, and how often customers have to call back."

**Invisible 3.** "...use AI to read the tickets, emails, system logs, and process documents and draft the map in a day, then have the people who do the work correct it."
- **Who trips and why:** TA. "Tickets" and "system logs".
- **Rewrite:** "...use AI to read the help-desk requests, emails and process documents and draft the map in a day..."

**Invisible 4.** "Where there isn't one, it is whoever owns the intake decision today - often the EPMO or the portfolio review - and that owner applies the same test."
- **Who trips and why:** CEO, GM. "EPMO" and "intake".
- **Rewrite:** "Where there isn't one, it's whoever decides today which projects get started - often the project office - and they apply the same test."

**Invisible 5.** "Related. Redesign the Stream, Not the Role (coming soon) - the invisible work is what value-stream mapping surfaces; this pattern is related, but is not necessarily that method's first step."
- **Who trips and why:** HR. Confusing, and the "coming soon" label is stale.
- **Rewrite:** "Related. Redesign the Stream, Not the Role maps the whole process; the invisible work is what that map shows."

**Invisible 6.** "That includes portfolio and intake reviews, AI steering committee agendas, vendor pitches promising headcount savings in customer-facing roles, and any business case built mainly on reducing visible work."
- **Who trips and why:** TA, GM.
- **Rewrite:** "That includes project funding reviews, AI committee meetings, vendor pitches promising to cut customer service jobs, and any business case built on cutting work customers can see."

**Invisible 7.** "Visible work is easy to count - headcount, volume, handle time - so the business case writes itself."
- **Who trips and why:** GM. "Handle time" is call-center jargon.
- **Rewrite:** "Visible work is easy to count - people, calls, minutes per call - so the business case writes itself."

## 24. AI as Amplifier, Not Foundation (patterns/06-ai-as-amplifier.html) - 6 findings

**Amplifier 1.** "I call that checking the botwatch. Skip it and you're shipping botcrap."
- **Who trips and why:** CEO, HR. Two coinages that aren't explained; HR would not forward a page with the second one.
- **Rewrite:** "That's the checking. Skip it and you're shipping work you can't stand behind."

**Amplifier 2.** "You can’t defend what you didn’t read. AI now produces more than people can review: in Anthropic’s study of its own workforce, reading everything employees’ agents produced would have taken half the work week (Wilmers, Catipon, Massenkoff and McCrory, “How Employment is Changing at Anthropic,” Anthropic, October 16, 2026)."
- **Who trips and why:** CEO. "Agents" and a long citation.
- **Rewrite:** "You can't defend what you didn't read. AI now produces more than people can review: at Anthropic, the company that makes Claude, reading everything staff's AI helpers produced would have taken half the work week."

**Amplifier 3.** "Provided feedback during the in-review phase, noting that AI failure extends beyond human credibility gaps to include structural model limitations - missing context, inaccessible data, and nuance the model had no way to account for."
- **Who trips and why:** GM.
- **Rewrite:** "Pointed out that AI can also fail for reasons that aren't the user's fault: missing context, data it couldn't see, and details it had no way to know."

**Amplifier 4.** "Her point that AI amplifies the cognition, intention, and judgment of the person using it - so understanding people matters more than ever - shaped the "know the person" note."
- **Who trips and why:** HR.
- **Rewrite:** "Her point that AI amplifies the thinking, intentions and judgment of whoever uses it..."

**Amplifier 5.** "A consultant can produce a framework-laden recommendation in minutes."
- **Who trips and why:** TA.
- **Rewrite:** "A consultant can produce a recommendation full of models and charts in minutes."

**Amplifier 6.** "Applies to analysts, consultants, managers, and executives who use AI to produce work product they don't fully own - documents, analyses, recommendations, or responses that will face scrutiny."
- **Who trips and why:** GM. "Work product" is legal and consulting phrasing.
- **Rewrite:** "...who use AI to produce work they don't fully own..."

## 25. The Chat Is Not Your Memory (patterns/25-the-chat-is-not-your-memory.html) - 6 findings

**Memory 1.** "A repository such as GitHub works too; it's what this library uses."
- **Who trips and why:** TA, GM, CEO. "Repository" and "GitHub" in a Start-here pattern.
- **Rewrite:** "A shared online folder that keeps every version works too - this library uses one built for software teams."

**Memory 2.** "After weeks of building this library with one AI, Greg pointed ChatGPT at the project's GitHub repository."
- **Who trips and why:** TA.
- **Rewrite:** "After weeks of building this library with one AI, Greg pointed ChatGPT at the project's shared files."

**Memory 3.** "I learned it the hard way building this library: one morning the handoff note misstated what was published, a red team left no trace, and a day's backlog was nearly lost."
- **Who trips and why:** CEO. Insider terms "handoff note", "red team" and "backlog".
- **Rewrite:** "I learned it the hard way: one morning my notes were wrong about what was published, a whole review had vanished, and a day's to-do list was nearly lost."

**Memory 4.** "Switch models without starting over - the record isn't tied to one AI. Point a different model at it and it picks up the work, so changing tools is a decision, not a restart."
- **Who trips and why:** GM.
- **Rewrite:** "Switch AI tools without starting over - the record isn't tied to one AI. Hand it to a different tool and it picks up the work."

**Memory 5.** "It matters most when the work depends on things the AI can't re-derive: text you pasted, decisions you made, corrections you gave, and the reasons behind them."
- **Who trips and why:** HR.
- **Rewrite:** "...things the AI can't work out again on its own..."

**Memory 6.** "Long AI work loses its memory. Sessions get compressed, restarted, or handed to a new tool, and the AI quietly forgets what you told it - then rebuilds it, confidently and wrong."
- **Who trips and why:** CEO. "Compressed" is unexplained in the opening line.
- **Rewrite:** "Long AI work loses its memory. Long chats get trimmed, restarted or moved to a new tool, and the AI quietly forgets what you told it - then fills the gap, confidently and wrong."

## 26. Judge the Outcome, Not the Craft (patterns/26-judge-the-outcome-not-the-craft.html) - 5 findings

**Judge 1.** "This is your botwatch: the human check before it ships."
- **Who trips and why:** CEO. An unexplained coinage.
- **Rewrite:** "This is the human check before it ships."

**Judge 2.** "The AI equivalent of a peer is another model: use it to check the work."
- **Who trips and why:** TA, GM.
- **Rewrite:** "The AI version of a peer is a second AI tool: use it to check the work."

**Judge 3.** "AI agents can already do work you can't do yourself - and can't check line by line."
- **Who trips and why:** CEO. "Agents" in the opening line.
- **Rewrite:** "AI can already do work you can't do yourself - and can't check line by line."

**Judge 4.** "Less dependence on one black box - no single model, agent or person becomes the only one who understands a critical piece of work."
- **Who trips and why:** GM.
- **Rewrite:** "...no single AI tool or person becomes the only one who understands a critical piece of work."

**Judge 5.** "Use a fresh chat, a different model if you can, and ask what's wrong with the work - not whether it's right."
- **Who trips and why:** TA.
- **Rewrite:** "Use a new chat, a different AI tool if you can..."

## 27. Right Tool, Right Job (patterns/17-right-tool-right-job.html) - 4 findings

**Tool 1.** "Every exception has an approved data path. Each extra tool is another place company data goes, so no exception goes live without one."
- **Who trips and why:** CEO, GM. "Approved data path".
- **Rewrite:** "Every extra tool is approved for the data it touches. Each one is another place company data goes, so none goes live without that sign-off."

**Tool 2.** "Models aren't interchangeable. Some are stronger at long documents, some at code, some at careful reasoning, some at speed and cost. Some can search the web or run code; some can't."
- **Who trips and why:** TA. "Models" and "run code".
- **Rewrite:** "AI tools aren't interchangeable. Some are better at long documents, some at careful reasoning, some at speed and price. Some can search the web; some can't."

**Tool 3.** ""What's the best AI?" is the wrong question. Best for what? Different models are good at different jobs - and so are tools that aren't AI at all."
- **Who trips and why:** CEO. "Models" in the opening line.
- **Rewrite:** "...Different AI tools are good at different jobs..."

**Tool 4.** "Before choosing, describe the task: what goes in (a 200-page contract, a spreadsheet, a code base), how sensitive that data is, and how much data the job actually needs..."
- **Who trips and why:** GM. "Code base".
- **Rewrite:** "...(a 200-page contract, a spreadsheet, a stack of emails)..."

## 28. Embed the Expert (patterns/14-embed-the-expert.html) - 4 findings

**Expert 1.** "The Compressed Apprenticeship is the companion: 09 helps people learn faster with AI; this pattern turns one person's judgment into something others can run."
- **Who trips and why:** All four. A pattern number used as shorthand.
- **Rewrite:** "The Compressed Apprenticeship is the companion: it helps people learn faster with AI; this pattern turns one person's judgment into something others can run."

**Expert 2.** "The architect who spots the integration that will fail."
- **Who trips and why:** GM, TA. "Architect" and "integration" in the IT sense.
- **Rewrite:** "The IT lead who knows which system hookup will fail."

**Expert 3.** "The senior PM who can read a project plan and say exactly where it will slip."
- **Who trips and why:** TA. "PM".
- **Rewrite:** "The senior project manager who can read a plan and say exactly where it will slip."

**Expert 4.** "Keep it tool-neutral: a skill is saved instructions, and works in any AI tool that lets you save and reuse them."
- **Who trips and why:** CEO. "Tool-neutral" is fine, but the line is close to the code-speak cluster.
- **Rewrite:** "Write it so it works in any AI tool: a skill is just saved instructions, and most AI tools let you save and reuse them." (Low priority.)

## 29. ROI worksheets (services/roi/setup.html, workshop.html, retainer.html) - 3 findings

**ROI 1.** "Your loaded hourly cost and headcount in scope - the example uses $75/hour." (all three pages)
- **Who trips and why:** GM, TA. "Loaded" is finance shorthand (HR and the CEO know it).
- **Rewrite:** "Your fully loaded hourly cost (pay plus benefits and overhead) and how many people are included - the example uses $75/hour."

**ROI 2.** "Governance: who owns each AI tool and agent, and what it can reach" (retainer)
- **Who trips and why:** CEO.
- **Rewrite:** "Clear ownership: who is responsible for each AI tool, and what company information it can see"

**ROI 3.** "Pull your AI tool's usage report (Copilot, ChatGPT or Claude): how many paid seats are used weekly?" (setup)
- **Who trips and why:** GM. "Seats".
- **Rewrite:** "...how many of the licenses you pay for get used each week?"

## 30. Research Partner, Not All-Knowing Oracle (patterns/19-research-partner-not-oracle.html) - 3 findings

**Research 1.** "Deloitte didn't say AI caused the errors, but the revised report disclosed that it had used Azure OpenAI."
- **Who trips and why:** TA, GM. "Azure OpenAI".
- **Rewrite:** "...disclosed that it had used Microsoft's version of the AI behind ChatGPT."

**Research 2.** "Read the sources you rely on yourself. AI can now produce far more than anyone can check: when Anthropic studied its own workforce, reading everything employees’ agents produced would have taken half the work week..."
- **Who trips and why:** CEO. "Agents".
- **Rewrite:** "...reading everything staff's AI helpers produced would have taken half the work week..."

**Research 3.** "Pasted sources are saved word for word, so anyone can retrace them."
- **Who trips and why:** HR. It's unclear what "pasted sources" means.
- **Rewrite:** "Every article or document I gave the AI is saved word for word, so anyone can check it."

## 31. Ten People, One Idea (patterns/22-ten-people-one-idea.html) - 3 findings

**Ten 1.** "If your strategy comes from the same model your competitors use, it isn't a strategy. It's theirs too."
- **Who trips and why:** CEO. "Model".
- **Rewrite:** "If your strategy comes from the same AI your competitors use, it isn't a strategy. It's theirs too."

**Ten 2.** "Ten people bring ten proposals that make the same points and reach the same recommendation - because they all asked the same model."
- **Who trips and why:** TA.
- **Rewrite:** "...because they all asked the same AI."

**Ten 3.** "The usual way, everyone prompts the same AI first and the session ends with three versions of one idea."
- **Who trips and why:** GM.
- **Rewrite:** "The usual way, everyone asks the same AI first and the meeting ends with three versions of one idea."

## 32. The Staged Journey (patterns/16-the-staged-journey.html) - 3 findings

**Staged 1.** "Use a structured assessment; for example, the GO Framework's Personal AI Readiness Assessment scores people across five dimensions."
- **Who trips and why:** CEO. "GO Framework" is unexplained on this page.
- **Rewrite:** "Use a simple assessment - for example, Level 5ive's Personal AI Readiness Assessment, which scores people on five areas."

**Staged 2.** "The Concerns-Based Adoption Model, developed for school change in the 1970s, shows that people need different help at each stage, as their concerns move from "what is this?" to "what does it mean for me?" to "how do I manage it?" to "how do I make it better?""
- **Who trips and why:** HR, CEO. A 50-word sentence.
- **Rewrite:** "A model built for schools in the 1970s shows people need different help at each stage. Their questions move from 'what is this?' to 'what does it mean for me?' to 'how do I manage it?' to 'how do I make it better?'"

**Staged 3.** "It is not a maturity model for scoring teams against each other."
- **Who trips and why:** GM. "Maturity model" is consultant jargon.
- **Rewrite:** "It is not a scorecard for ranking teams against each other."

## 33. AI Friction (patterns/23-ai-friction.html) - 2 findings

**Friction 1.** "A 20-second reply to a colleague turns into a 10-minute prompting session."
- **Who trips and why:** GM. "Prompting".
- **Rewrite:** "A 20-second reply to a colleague turns into 10 minutes of back-and-forth with the AI."

**Friction 2.** "Ore is not gold. More polished output with no impact is more ore, not more gold. Usage counts measure the ore."
- **Who trips and why:** CEO, if they arrive here first. The metaphor is only explained on the home page.
- **Rewrite:** "Ore is not gold: more polished output with no impact is just more raw material, not more value. Counting how often people use AI measures the ore."

## 34. Iterate to the Destination (patterns/20-iterate-to-the-destination.html) - 2 findings

**Iterate 1.** "Some skip the destination and just start prompting."
- **Who trips and why:** GM.
- **Rewrite:** "Some skip the destination and just start asking."

**Iterate 2.** "The first plan for our ten-minute sessions was eight slides and a linear run sheet. It didn't tell the story the way it needed to. The destination was rewritten - a five-act arc, about ten minutes, half of it live..."
- **Who trips and why:** TA. "Run sheet" and "five-act arc" are production insider terms.
- **Rewrite:** "The first plan for our ten-minute sessions was eight slides and a script read top to bottom... The destination was rewritten - a story in five parts, about ten minutes, half of it live..."

## 35. Sessions (sessions/index.html) - 2 findings

**Sessions 1.** "In this session, Greg Stellflue runs the fix live: hand off the work, not the decisions - with limits in access, findings instead of changes, and a one-page morning review."
- **Who trips and why:** GM. "Limits in access" and "findings instead of changes" are compressed.
- **Rewrite:** "...hand off the work, not the decisions - with limits on what the AI can touch, suggestions instead of changes, and a one-page morning review."

**Sessions 2.** "The prompt: The Night Shift - Use this pattern."
- **Who trips and why:** TA. "The prompt" is undefined for a first-time visitor.
- **Rewrite:** "The instructions to paste into your AI: The Night Shift - Use this pattern."

## 36. Session READMEs (sessions/session-01, -02, -03 README.md) - 1 finding

**Session README 1.** "- Red team: red-team-webinar-01.md" (and the same lines in sessions 2 and 3, plus "Recording sheet with Act III paste-ins")
- **Who trips and why:** All four, if they land here from the public repo. These are internal production notes made of file lists.
- **Rewrite:** Add one plain line at the top: "Behind-the-scenes files for this session. To watch it, go to aisuccesspatterns.com/sessions." Or keep these files out of the public view.
