---
tags:
  - "#type/weekly-note" 
cssclasses:
- image-borders
- image-small
- weekly
- timegarden-weekly
- week-invalid date
# Not a weekly note - banner not applied
date: Invalid date
journal: weekly
journal-date: Invalid date
journal-start-date: Invalid date
journal-end-date: Invalid date
alias:
aiAnswer: ""
WeekSummary: ""
wheelOfLife:
  spiritual: 
  spiritualSummary: ""
  career: 
  careerSummary: ""
  relationships: 
  relationshipsSummary: ""
  health: 
  healthSummary: ""
  growth: 
  growthSummary: ""
  recreation: 
  recreationSummary: ""
  social: 
  socialSummary: ""
  finance: 
  financeSummary: ""
---
# ✧ weekly MetaBindWheelOfLifeDisplay
[[Invalid date|]] 
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

```meta-bind
INPUT[text(placeholder('Name this Week!'), class('custom-input')):alias]
```

```meta-bind
INPUT[editor(class(custom-editor)):WeekSummary]
```

`BUTTON[generate-weekly-summary, generate-weekly-alias]`
```meta-bind-button
id: generate-weekly-summary
style: primary
class: phone-responsive
label: ✨ Generate Summary
hidden: true
actions:
  - type: command
    command: templater-obsidian:undefined06 Templates/Components/Weekly AI Summarize.md
```
```meta-bind-button
id: generate-weekly-alias
style: primary
class: phone-responsive
label: 🏷️ Generate Alias
hidden: true
actions:
  - type: command
    command: templater-obsidian:undefined06 Templates/Components/Weekly AI Alias.md
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
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/weekly/weeklyRatingChart", {container: this.container})
```
### <p hidden>PicturesHeader</p>
> [! pictures]- Pictures of Wundefined
> ![[Invalid date#📁 Pictures]]
> ![[Invalid date#📁 Pictures]]
> ![[Invalid date#📁 Pictures]]
> ![[Invalid date#📁 Pictures]]
> ![[Invalid date#📁 Pictures]]
> ![[Invalid date#📁 Pictures]]
> ![[Invalid date#📁 Pictures]]
## Logs
---
Error: Unable to extract date range from filename.

Error: Unable to extract date range from filename.

Error: Unable to extract date range from filename.

## General Overview
---
```dataview
table alias, dayRating
from [[Invalid date]] WHERE file.name != "tp.file.title"
```

## Wheel of Life
---
```dataviewjs
dv.view("undefined06 Templates/Scripts/templater/dataviewjs/weekly/weeklyWheelOfLifeChart", {container: this.container})
```
```meta-bind-button
id: generate-wheel-of-life
style: primary
class: centered-button phone-responsive
label: 🌟 Generate Wheel of Life Analysis
actions:
  - type: command
    command: templater-obsidian:undefined06 Templates/Components/Weekly AI WheelOfLife.md
```

<span style="color: rgba(103, 58, 183, 0.8); font-weight: bold; font-size: 35px;">Spiritual</span> | `INPUT[number(class(centeredNumberInput), placeholder('🧘 Spiritual Rating')):wheelOfLife.spiritual]` | `INPUT[slider(minValue(1), maxValue(10)):wheelOfLife.spiritual]`
`VIEW[{wheelOfLife.spiritualSummary}][text(renderMarkdown)]`

#### <span style="color: rgba(3, 169, 244, 0.8); font-weight: bold; font-size: 35px;">Career/Work</span> | `INPUT[number(class(centeredNumberInput), placeholder('💼 Career Rating')):wheelOfLife.career]` | `INPUT[slider(minValue(1), maxValue(10)):wheelOfLife.career]`
`VIEW[{wheelOfLife.careerSummary}][text(renderMarkdown)]`
#### <span style="color: rgba(233, 30, 99, 0.8); font-weight: bold; font-size: 35px;">Love/Relationships</span> | `INPUT[number(class(centeredNumberInput), placeholder('❤️ Relationships Rating')):wheelOfLife.relationships]` |`INPUT[slider(minValue(1), maxValue(10)):wheelOfLife.relationships]`
`VIEW[{wheelOfLife.relationshipsSummary}][text(renderMarkdown)]`

#### <span style="color: rgba(0, 150, 136, 0.8); font-weight: bold; font-size: 35px;">Health/Fitness</span> | `INPUT[number(class(centeredNumberInput), placeholder('🏃 Health Rating')):wheelOfLife.health]` | `INPUT[slider(minValue(1), maxValue(10)):wheelOfLife.health]`
`VIEW[{wheelOfLife.healthSummary}][text(renderMarkdown)]`

#### <span style="color: rgba(255, 87, 34, 0.8); font-weight: bold; font-size: 35px;">Personal Growth</span> | `INPUT[number(class(centeredNumberInput), placeholder('🌱 Growth Rating')):wheelOfLife.growth]` | `INPUT[slider(minValue(1), maxValue(10)):wheelOfLife.growth]`
`VIEW[{wheelOfLife.growthSummary}][text(renderMarkdown)]`

#### <span style="color: rgba(255, 193, 7, 0.8); font-weight: bold; font-size: 35px;">Fun/Recreation</span> | `INPUT[number(class(centeredNumberInput), placeholder('🎮 Recreation Rating')):wheelOfLife.recreation]` | `INPUT[slider(minValue(1), maxValue(10)):wheelOfLife.recreation]`
`VIEW[{wheelOfLife.recreationSummary}][text(renderMarkdown)]`

#### <span style="color: rgba(156, 39, 176, 0.8); font-weight: bold; font-size: 35px;">Social</span> | `INPUT[number(class(centeredNumberInput), placeholder('👥 Social Rating')):wheelOfLife.social]` | `INPUT[slider(minValue(1), maxValue(10)):wheelOfLife.social]`
`VIEW[{wheelOfLife.socialSummary}][text(renderMarkdown)]`

#### <span style="color: rgba(76, 175, 80, 0.8); font-weight: bold; font-size: 35px;">Finance</span> | `INPUT[number(class(centeredNumberInput), placeholder('💰 Finance Rating')):wheelOfLife.finance]` | `INPUT[slider(minValue(1), maxValue(10)):wheelOfLife.finance]`
`VIEW[{wheelOfLife.financeSummary}][text(renderMarkdown)]`

---
## Q&A
---
```meta-bind
INPUT[text(placeholder('Write a question'), class('custom-input')):aiQuestion]
```
---
```meta-bind-button
label: 🔎 Ask your Week
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
    command: templater-obsidian:undefined06 Templates/Components/Weekly AI QA Execute.md

```

```meta-bind
INPUT[editor(class(custom-editor)):aiAnswer]
```

