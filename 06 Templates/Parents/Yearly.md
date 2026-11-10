---
tags:
  - "#type/yearly-note" 
cssclasses:
  - image-borders
  - image-small
  - yearly
  - timegarden-yearly
banner:
  - - YearlyBanner.jpg
banner-y: 50
banner-x: 30
content-start: 200
banner-display: cover
banner-repeat: true
banner-height: 400
banner-fade: -75
banner-radius: 25
date: 2026-01-01
alias:
aiAnswer: ""
YearSummary: ""
yearlyWheelOfLifeCategoryChartType: line
journal: yearly
journal-date: 2026-01-01
---
# ✧ 2026-07-25 Vault Cross-Linking & Organisation

`BUTTON[prev-year, next-year]`
```meta-bind-button
id: prev-year
style: primary
class: phone-responsive
label: ← Previous Year
hidden: true
actions:
  - type: open
    link: "[[/01 - Journal/Yearly/2025]]"
    newTab: false
```
```meta-bind-button
id: next-year
class: phone-responsive
style: primary
label: Next Year →
hidden: true
actions:
    - type: open
      link: "[[/01 - Journal/Yearly/2027]]"
      newTab: false
```

```meta-bind
INPUT[text(placeholder('Name this Year!'), class('custom-input')):alias]
```

```meta-bind
INPUT[editor(class(custom-editor)):YearSummary]
```

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

## Ratings ✮⋆˙
---
```tracker
searchType: frontmatter
searchTarget: dayRating
dateFormat: YYYY-MM-DD-dddd
datasetName: yearRating
startDate: 2026-01-01-Thursday
endDate: 2026-12-31-Thursday
summary:
    template: "Average Rating: {{average()}}" 
```

```dataviewjs
dv.view("06 Templates/Scripts/templater/dataviewjs/yearly/yearlyRatingChart", {container: this.container})
```

## Top Days ✮⋆˙
---
```dataview
TABLE WITHOUT ID file.link as Date, alias as Day
FROM "01 - Journal/Daily"
WHERE date.year = date(this.file.day).year
AND dayRating >= 9
SORT dayRating DESC
```

## Gallery
---
> [! pictures]- Yearly Gallery
> ![[2026/2026-Q1#<p hidden>PicturesHeader</p>]]
> ![[2026/2026-Q2#<p hidden>PicturesHeader</p>]]
> ![[2026/2026-Q3#<p hidden>PicturesHeader</p>]]
> ![[2026/2026-Q4#<p hidden>PicturesHeader</p>]]

## Quarters Overview
---
```dataview
TABLE without id file.link as Quarter, alias
FROM "01 - Journal/Quarterly"
WHERE date.year = date(this.file.day).year
SORT file.day ASC
```

## Wheel of Life Overview
---
```dataviewjs
dv.view("06 Templates/Scripts/templater/dataviewjs/yearly/yearlyWheelOfLifeChart", {container: this.container})
```

**Chart Type:** `INPUT[suggester(title('chart type'), option(line), option(bar), option(pie), option(radar)):yearlyWheelOfLifeCategoryChartType]`

```dataviewjs
dv.view("06 Templates/Scripts/templater/dataviewjs/yearly/yearlyWheelOfLifeProgression", {container: this.container})
```
## Q&A
---
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
    command: templater-obsidian:06 Templates/Components/Yearly AI QA Execute.md

```

```meta-bind
INPUT[editor(class(custom-editor)):aiAnswer]
```

