`BUTTON[ai-rate-alias, ai-rate-only, ai-alias-only]`
```meta-bind-button
id: ai-rate-alias
style: primary
class: phone-responsive
label: ⚡ AI Rating + Alias
hidden: true
actions:
  - type: command
    command: templater-obsidian:<%* tR += (window?.timeGarden?.rootPath ?? "/").substring(1); _%>06 Templates/Components/Daily AI RateAndAlias.md
```
```meta-bind-button
id: ai-rate-only
style: primary
class: phone-responsive
label: ⭐ AI Rating
hidden: true
actions:
  - type: command
    command: templater-obsidian:<%* tR += (window?.timeGarden?.rootPath ?? "/").substring(1); _%>06 Templates/Components/Daily AI Rate.md
```
```meta-bind-button
id: ai-alias-only
style: primary
class: phone-responsive
label: 🏷️ AI Alias
hidden: true
actions:
  - type: command
    command: templater-obsidian:<%* tR += (window?.timeGarden?.rootPath ?? "/").substring(1); _%>06 Templates/Components/Daily AI Alias.md
```