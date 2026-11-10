`BUTTON[generate-yearly-summary, generate-yearly-alias]`
```meta-bind-button
id: generate-yearly-summary
style: primary
class: phone-responsive
label: ✨ Generate Summary
hidden: true
actions:
  - type: command
    command: templater-obsidian:06 Templates/Components/Yearly AI Summarize.md
```
```meta-bind-button
id: generate-yearly-alias
style: primary
class: phone-responsive
label: 🏷️ Generate Alias
hidden: true
actions:
  - type: command
    command: templater-obsidian:06 Templates/Components/Yearly AI Alias.md
```