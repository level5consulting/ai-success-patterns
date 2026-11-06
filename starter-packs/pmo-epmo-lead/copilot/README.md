# PMO / EPMO Lead Starter Pack - Copilot version (v0.2, being tested)

The same five Start-here patterns plus the pmo-start-here guide, for Microsoft 365 Copilot.

Most Copilot users don't have plugins or skills. Those only work in **Copilot Cowork**, which your organization has to turn on. So start with the first option below - it works in ordinary Copilot.

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

## Option 3 - If your organization has Copilot Cowork
Not sure? Ask your IT admin. If you don't see Cowork in Copilot, you don't have it.
1. Download `pmo-copilot-plugin.zip`. Don't unzip it.
2. In Cowork, select **+ > Customize > Plugins > Upload plugin**, and choose the zip.
3. Share it with "Only you" to test, then select **Apply**.
4. Open a new chat and say: "Start here - I'm a PMO lead."

## Set up your workspace
- **One place per project you manage** (or per program, if your projects are small), such as a Copilot notebook or a SharePoint or OneDrive folder, with many short chats that read from it - The Chat Is Not Your Memory.
- In that place: a **project record**, **reference files** (charter, RAID log, last steering deck, templates) and **standing instructions** (report format, tone, RAG thresholds).
- **One short chat per task.** Each chat reads the record, does the job, asks for the agenda, and updates the record with it. The agenda opens the next chat.
- **One separate portfolio place** for health checks, cross-project prioritization and documenting your AI assets.
- First move: run The Chat Is Not Your Memory on one project to create the record.

Bringing back the past to help our future. - aisuccesspatterns.com
