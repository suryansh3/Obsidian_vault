---
tags:
  - "#type/quarterly-note" 
cssclasses:
  - image-borders
  - image-small
  - timegarden-quarterly
  - quarter-invalid date
  - quarterly
# Not a quarterly note - banner not applied
date: Invalid date
alias:
aiAnswer: ""
QuarterSummary: ""
quarterlyWheelOfLifeCategoryChartType: line
quarterRating: 0
journal: quarterly
journal-date: Invalid date
journal-start-date: Invalid date
journal-end-date: Invalid date
---
# ✧ *Invalid date*

`BUTTON[prev-quarter, current-year, next-quarter]`
```meta-bind-button
id: prev-quarter
style: primary
label: ← Previous Quarter
hidden: true
actions:
  - type: open
    link: "[[undefined04 Quarterly/Invalid date]]"
    newTab: false
```
```meta-bind-button
id: current-year
style: primary
label: This Year
hidden: true
actions:
    - type: open  
      link: "[[undefined05 Yearly/Invalid date]]"
      newTab: false
```
```meta-bind-button
id: next-quarter
style: primary
label: Next Quarter →
hidden: true
actions:
    - type: open
      link: "[[undefined04 Quarterly/Invalid date]]"
      newTab: false
```

```meta-bind
INPUT[text(placeholder('Name this Quarter!'), class('custom-input')):alias]
```

```meta-bind
INPUT[editor(class(custom-editor)):QuarterSummary]
```

`BUTTON[generate-quarterly-summary, generate-quarterly-alias]`
```meta-bind-button
id: generate-quarterly-summary
style: primary
label: ✨ Generate Summary
hidden: true
actions:
  - type: command
    command: templater-obsidian:undefined06 Templates/Components/Quarterly AI Summarize.md
```
```meta-bind-button
id: generate-quarterly-alias
style: primary
label: 🏷️ Generate Alias
hidden: true
actions:
  - type: command
    command: templater-obsidian:undefined06 Templates/Components/Quarterly AI Alias.md
```

## Ratings ✮⋆˙
---
```tracker
searchType: frontmatter
searchTarget: dayRating
dateFormat: YYYY-MM-DD-dddd
datasetName: monthRating
startDate: Invalid date
endDate: Invalid date
summary:
    template: "Average Rating: {{average()}}" 
```

```dataviewjs
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/quarterly/quarterlyRatingChart", {container: this.container})
```
### <p hidden>PicturesHeader</p>
> [! pictures]- Gallery of QInvalid date

## Logs
---


## Month Overview
---
```dataviewjs
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/quarterly/quarterlyMonthDisplay", {container: this.container})
```

## Wheel of Life Overview
---
```dataviewjs
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/quarterly/quarterlyWheelOfLifeChart", {container: this.container})
```

**Chart Type:** `INPUT[suggester(title('chart type'), option(line), option(bar), option(pie), option(radar)):quarterlyWheelOfLifeCategoryChartType]`

```dataviewjs
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/quarterly/quarterlyWheelOfLifeProgression", {container: this.container})
```

## Q&A
---
```meta-bind
INPUT[text(placeholder('Write a question'), class('custom-input')):aiQuestion]
```
---
```meta-bind-button
label: 🔎 Ask your Quarter
icon: ""
style: primary
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: ""
hidden: false
actions:
  - type: command
    command: templater-obsidian:undefined06 Templates/Components/Quarterly AI QA Execute.md

```

```meta-bind
INPUT[editor(class(custom-editor)):aiAnswer]
```

