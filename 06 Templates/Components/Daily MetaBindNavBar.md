`BUTTON[prev-day, current-week, next-day]`
```meta-bind-button
id: prev-day
class: phone-responsive
style: primary
label: ← Yesterday
hidden: true
actions:
  - type: open
    link: "[[<%* tR += (window?.timeGarden?.rootPath ?? "/"); _%>01 - Journal/Daily/<% fileDate = moment(tp.file.title, 'YYYY-MM-DD-dddd').subtract(1, 'd').format('YYYY/MM-MMMM/YYYY-MM-DD-dddd') %>]]"
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
    link: "[[<%* tR += (window?.timeGarden?.rootPath ?? "/"); _%>01 - Journal/Weekly/<% fileDate = moment(tp.file.title, 'YYYY-MM-DD-dddd').format('YYYY/YYYY-[W]WW') %>]]"
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
    link: "[[<%* tR += (window?.timeGarden?.rootPath ?? "/"); _%>01 - Journal/Daily/<% fileDate = moment(tp.file.title, 'YYYY-MM-DD-dddd').add(1, 'd').format('YYYY/MM-MMMM/YYYY-MM-DD-dddd') %>]]"
    newTab: false
```