`BUTTON[prev-week, current-month, next-week]`
```meta-bind-button
id: prev-week
style: primary
class: phone-responsive
label: ← Previous Week
hidden: true
actions:
  - type: open
    link: "[[/01 - Journal/Weekly/2026/2026-W06]]"
    newTab: false
```
```meta-bind-button
id: current-month
style: primary
class: phone-responsive
label: This Month
hidden: true
actions:
    - type: open  
      link: "[[/01 - Journal/Monthly/2026/2026-02-February]]"
      newTab: false
```
```meta-bind-button
id: next-week
style: primary
class: phone-responsive
label: Next Week →
hidden: true
actions:
    - type: open
      link: "[[/01 - Journal/Weekly/2026/2026-W08]]"
      newTab: false
```