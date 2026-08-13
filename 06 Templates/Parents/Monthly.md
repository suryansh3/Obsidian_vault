---
tags:
  - "#type/monthly-note" 
cssclasses:
  - image-borders
  - image-small
  - timegarden-monthly
  - invalid date
  - monthly
# Not a monthly note - banner not applied
date: Invalid date
alias:
aiAnswer: ""
MonthSummary: ""
monthlyWheelOfLifeCategoryChartType: line
journal: monthly
journal-date: Invalid date
journal-start-date: Invalid date
journal-end-date: Invalid date
---
# ✧ *Invalid date*

`BUTTON[prev-month, current-quarter, next-month]`
```meta-bind-button
id: prev-month
style: primary
class: phone-responsive
label: ← Previous Month
hidden: true
actions:
  - type: open
    link: "[[undefined03 Monthly/Invalid date]]"
    newTab: false
```
```meta-bind-button
id: current-quarter
style: primary
class: phone-responsive
label: This Quarter
hidden: true
actions:
    - type: open  
      link: "[[undefined04 Quarterly/Invalid date]]"
      newTab: false
```
```meta-bind-button
id: next-month
style: primary
class: phone-responsive
label: Next Month →
hidden: true
actions:
    - type: open
      link: "[[undefined03 Monthly/Invalid date]]"
      newTab: false
```

```meta-bind
INPUT[text(placeholder('Name this Month!'), class('custom-input')):alias]
```

```meta-bind
INPUT[editor(class(custom-editor)):MonthSummary]
```

`BUTTON[generate-monthly-summary, generate-monthly-alias]`
```meta-bind-button
id: generate-monthly-summary
style: primary
label: ✨ Generate Summary
hidden: true
actions:
  - type: command
    command: templater-obsidian:undefined06 Templates/Components/Monthly AI Summarize.md
```
```meta-bind-button
id: generate-monthly-alias
style: primary
label: 🏷️ Generate Alias
hidden: true
actions:
  - type: command
    command: templater-obsidian:undefined06 Templates/Components/Monthly AI Alias.md
```

## Ratings ✮⋆˙
---
```tracker
searchType: frontmatter
searchTarget: dayRating
dateFormat: YYYY-MM-DD-dddd
datasetName: dayRating
startDate: Invalid date
endDate: Invalid date
summary:
    template: "Average Rating: {{average()}}" 
```

```dataviewjs
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/monthly/monthlyRatingChart", {container: this.container})
```

### <p hidden>PicturesHeader</p>
> [! pictures]- Gallery of MInvalid date

## Logs
---


## Week Overview
---
```dataviewjs
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/monthly/monthlyWeekDisplay", {container: this.container})
```
## Wheel of Life Overview
---
```dataviewjs
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/monthly/monthlyWheelOfLifeChart", {container: this.container})
```

**Chart Type:** `INPUT[suggester(title('chart type'), option(line), option(bar), option(pie), option(radar)):monthlyWheelOfLifeCategoryChartType]`

```dataviewjs
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/monthly/monthlyWheelOfLifeProgression", {container: this.container})
```

## Q&A
---
```meta-bind
INPUT[text(placeholder('Write a question'), class('custom-input')):aiQuestion]
```
---
```meta-bind-button
label: 🔎 Ask your Month
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
    command: templater-obsidian:undefined06 Templates/Components/Monthly AI QA Execute.md

```

```meta-bind
INPUT[editor(class(custom-editor)):aiAnswer]
```

