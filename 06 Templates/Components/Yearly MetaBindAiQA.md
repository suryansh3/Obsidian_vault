```meta-bind
INPUT[text(placeholder('Write a question'), class('custom-input')):aiQuestion]
```
---
```meta-bind-button
label: 🔎 Ask your Year
icon: ""
style: primary
class: phone-responsive
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: ""
hidden: false
actions:
  - type: command
    command: templater-obsidian:undefined06 Templates/Components/Yearly AI QA Execute.md

```

```meta-bind
INPUT[editor(class(custom-editor)):aiAnswer]
```