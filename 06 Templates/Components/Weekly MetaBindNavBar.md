`BUTTON[prev-week, current-month, next-week]`
```meta-bind-button
id: prev-week
style: primary
class: phone-responsive
label: ← Previous Week
hidden: true
actions:
  - type: open
    link: "[[undefined02 Weekly/Invalid date/Invalid date-Invalid date]]"
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
      link: "[[undefined03 Monthly/Invalid date]]"
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
      link: "[[undefined02 Weekly/Invalid date/Invalid date-Invalid date]]"
      newTab: false
```