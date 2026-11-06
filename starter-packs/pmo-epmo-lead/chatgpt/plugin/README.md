# ChatGPT plugin version (v0.1)

For the ChatGPT desktop app. The zip holds two hidden folders that go in your home folder:
- `.codex/plugins/ai-success-patterns-pmo/` - the plugin (plugin.json and the six skills)
- `.agents/plugins/marketplace.json` - tells ChatGPT where the plugin is

## Install
1. Download `pmo-chatgpt-plugin.zip`.
2. Unzip it into your home folder. On a Mac, in Terminal: `unzip ~/Downloads/pmo-chatgpt-plugin.zip -d ~`
   (If you already have a `~/.agents/plugins/marketplace.json`, don't overwrite it - add this plugin's entry to it.)
3. Quit and reopen the ChatGPT desktop app.
4. Open Plugins, choose the "AI Success Patterns" marketplace, and install "ai-success-patterns-pmo".
5. Open a new chat and say: "Start here - I'm a PMO lead."
