`BUTTON[prev-quarter, current-year, next-quarter]`
```meta-bind-button
id: prev-quarter
style: primary
label: ← Previous Quarter
hidden: true
actions:
  - type: open
    link: "[[/01 - Journal/Quarterly/Invalid date]]"
    newTab: false
```
```meta-bind-button
id: current-year
style: primary
label: This Year
hidden: true
actions:
    - type: open  
      link: "[[/01 - Journal/Yearly/Invalid date]]"
      newTab: false
```
```meta-bind-button
id: next-quarter
style: primary
label: Next Quarter →
hidden: true
actions:
    - type: open
      link: "[[/01 - Journal/Quarterly/Invalid date]]"
      newTab: false
```