# ChatGPT add-on (desktop app)

A plugin is an add-on that puts the six PMO patterns inside the ChatGPT app on your computer, so you can run each one by name.

> **This version is for technical users.** Everyone else: use the paste-a-prompt route in the ChatGPT README (`../README.md`) - it takes two minutes and needs no setup.

Technical setup: the download contains two hidden folders that need to go in your computer's home folder:
- `.codex/plugins/ai-success-patterns-pmo/` - the plugin itself: the six PMO patterns, saved as instructions ChatGPT can run on request.
- `.agents/plugins/marketplace.json` - a small settings file that tells ChatGPT where to find the plugin.

## Install
1. Download the plugin file (pmo-chatgpt-plugin.zip) - it's in the same folder as this page.
2. Unzip it into your home folder. On a Mac, in Terminal: `unzip ~/Downloads/pmo-chatgpt-plugin.zip -d ~`
   (If you've installed other ChatGPT plugins this way before, ask whoever set them up to add this one, so the old ones keep working.)
3. Quit and reopen the ChatGPT desktop app.
4. Open Plugins, choose AI Success Patterns, and install the PMO starter pack (it appears as ai-success-patterns-pmo).
5. Open a new chat and say: "Start here - I'm a PMO lead."
