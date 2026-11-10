`BUTTON[prev-day, current-week, next-day]`
```meta-bind-button
id: prev-day
class: phone-responsive
style: primary
label: ← Yesterday
hidden: true
actions:
  - type: open
    link: "[[/01 - Journal/Daily/Invalid date]]"
    newTab: false
```
```meta-bind-button
id: current-week 
style: primary
class: phone-responsive
label: This Week
hidden: true
actions:
  - type: open
    link: "[[/01 - Journal/Weekly/Invalid date]]"
    newTab: false
```
```meta-bind-button
id: next-day
style: primary
class: phone-responsive
label: Tomorrow →
hidden: true
actions:
  - type: open
    link: "[[/01 - Journal/Daily/Invalid date]]"
    newTab: false
```