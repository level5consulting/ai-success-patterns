# PMO / EPMO Lead Starter Pack - Copilot version 

The same five Start-here patterns plus the pmo-start-here guide, for Microsoft 365 Copilot.

Copilot doesn't take a whole pack at once. You add the patterns one at a time - each takes a couple of minutes.

## Option 1 - Make each pattern a Copilot agent (most people)
Do this once per pattern. Start with pmo-start-here.
1. Open `skills/pmo-start-here/SKILL.md` and copy everything below the top block (the lines between the two `---`).
2. In Copilot, go to **Agents > New agent** (Agent Builder).
3. Choose **Configure**. Name it "PMO Start Here" and paste the text into **Instructions**.
4. Select **Create**, then open the agent and say: "Start here - I'm a PMO lead."
5. Repeat for the other five skills you want, one agent each.

Each skill fits within Agent Builder's instruction limit.

## Option 2 - Paste it into a chat (fastest)
Open any `skills/<name>/SKILL.md`, copy everything below the top block, and paste it at the start of a Copilot chat. Or attach the file to the chat.

## Set up your workspace
- **One place per project you manage** (or per program, if your projects are small), such as a Copilot notebook or a SharePoint or OneDrive folder, with many short chats that read from it - The Chat Is Not Your Memory.
- In that place: a **project record**, **reference files** (charter, RAID log, last steering deck, templates) and **standing instructions** (report format, tone, RAG thresholds).
- **One short chat per task.** Each chat reads the record, does the job, asks for the agenda, and updates the record with it. The agenda opens the next chat.
- **One separate portfolio place** for health checks, cross-project prioritization and documenting your AI assets.
- First move: run The Chat Is Not Your Memory on one project to create the record.

Bringing back the past to help our future. - aisuccesspatterns.com
