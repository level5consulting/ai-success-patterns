# Plain language - ChatGPT plugin README (Nov 11, 2026)

Page: starter-packs/pmo-epmo-lead/chatgpt/plugin/README.md (page 3 in records/plain-language-review-2026-11-09.md).
Findings only - nothing on the page was changed.

Same panel as the Nov 9-10 review: travel agent (TA), plant nursery general manager (GM), HR director (HR), busy CEO on a phone (CEO, adversarial).

The Nov 9-10 review held 5 findings for this page (Plugin 1-5). This file adds 3 new ones (marked NEW) to make 8, ordered worst first. The page is only 13 lines, so these 8 cover nearly every line. Quotes are exact, including the code formatting.

**README 1.** "Unzip it into your home folder. On a Mac, in Terminal: `unzip ~/Downloads/pmo-chatgpt-plugin.zip -d ~`" (Install, step 2) - was Plugin 1
- **Who trips and why:** All four. It asks them to type a command into Terminal. The CEO and the TA both quit here.
- **Rewrite:** Put a box at the top: "This version is for technical users. Everyone else: use the paste-a-prompt route in the ChatGPT README - it takes two minutes and needs no setup." Keep the command below the box.

**README 2.** "(If you already have a `~/.agents/plugins/marketplace.json`, don't overwrite it - add this plugin's entry to it.)" (Install, step 2) - was Plugin 3
- **Who trips and why:** All four. It assumes the reader can find a hidden file and edit JSON by hand. Getting it wrong breaks their other plugins.
- **Rewrite:** "(If you've installed other ChatGPT plugins this way before, ask whoever set them up to add this one, so the old ones keep working.)"

**README 3.** "The zip holds two hidden folders that go in your home folder:" (opening) - was Plugin 2
- **Who trips and why:** TA, GM. "Hidden folders" and "home folder" are both unfamiliar, and hidden folders can't be seen without extra steps.
- **Rewrite:** "Technical setup: the download contains two hidden folders that need to go in your computer's home folder."

**README 4 (NEW).** "`.agents/plugins/marketplace.json` - tells ChatGPT where the plugin is" (opening list)
- **Who trips and why:** HR, GM, CEO. A file path, the word "marketplace" (sounds like a store they'll be charged in) and "JSON", with no plain description.
- **Rewrite:** "A small settings file that tells ChatGPT where to find the plugin."

**README 5.** "`.codex/plugins/ai-success-patterns-pmo/` - the plugin (plugin.json and the six skills)" (opening list) - was Plugin 4
- **Who trips and why:** CEO, TA. Folder paths and file names, and "skills" is never explained.
- **Rewrite:** "The plugin itself: the six PMO patterns, saved as instructions ChatGPT can run on request." (Tweaked from the Nov 9 rewrite, which still said "skills".)

**README 6 (NEW).** "ChatGPT plugin version (v0.1)" (page title)
- **Who trips and why:** CEO, TA. "Plugin" is never explained, and "v0.1" reads like unfinished software.
- **Rewrite:** "ChatGPT add-on (desktop app)" with one line under it: "A plugin is an add-on that puts the six PMO patterns inside the ChatGPT app on your computer, so you can run each one by name."

**README 7.** "Open Plugins, choose the "AI Success Patterns" marketplace, and install "ai-success-patterns-pmo"." (Install, step 4) - was Plugin 5
- **Who trips and why:** TA. The thing they're told to install has a code-style name.
- **Rewrite:** "Open Plugins, choose AI Success Patterns, and install the PMO starter pack." (If the app shows the code name, add: "it appears as ai-success-patterns-pmo".)

**README 8 (NEW).** "Download `pmo-chatgpt-plugin.zip`." (Install, step 1)
- **Who trips and why:** TA, HR. It doesn't say where to download it from, and the code-style file name looks like something only IT should touch.
- **Rewrite:** "Download the plugin file (pmo-chatgpt-plugin.zip) - it's in the same folder as this page."

Side note (not a plain-language finding): the page never says whether this works in ChatGPT in a web browser or on a phone. If it is desktop-only, say so in the first line. [4 PM] check.
