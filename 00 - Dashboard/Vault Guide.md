---
type: guide
tags:
  - guide
up: "[[MOC]]"
---
# 📘 Vault Guide

**Map:** [[MOC]] · **Dashboard:** [[Home]]

## What opens at launch
The **Homepage** plugin opens [[Home]] (Reading view, replaces all tabs). It reads today's journal note, your stat areas and pursuits, and renders the level HUD, radar, quests, gacha and more. Tick quests and click energy bars directly on it - values are stored in today's daily note.

## Folder map
| Folder | Purpose |
| --- | --- |
| `00 - Dashboard` | [[Home]], [[MOC]], this guide |
| `01 - Journal` | Daily → Yearly notes ([[Journal]]) |
| `02 - Quests` | RPG engine: [[Quest Config]], [[Character]], [[Rewards]], areas, pursuits ([[Quest Board]]) |
| `03 - AI & ML` | [[AI & ML Roadmap]] |
| `04 - Academics & CS` | semesters → courses → notes ([[Academics & CS]]) |
| `05 - Second Brain & Knowledge` | [[Second Brain]]: clippings, drawings, handwritten notes, reference |
| `06 Templates` | Time Garden templates & scripts (**plugin-owned: don't rename**) + `Notes/` for your own |
| `07 - Archives` | unlinked attachments etc. (excluded from search/graph) |
| `08 - Resources` | PDFs and guides |
| `99 - Meta` | attachments, Gemini Scribe data, CSS notes (excluded from search/graph) |

## Linking rules (keeps the second brain connected)
1. Every new note gets an **Up** link to its hub (course page, clippings index, quest board…) - and the hub gets a link back.
2. Link by concept: threads in Java ↔ [[Operating Systems]]; DIP clippings ↔ [[IPA]].
3. Prefer unique file names (`OS Assignment-5`, not `Assignment-5`).
4. Check the health panel below monthly.

## Everyday workflow
- Open Obsidian → [[Home]] → tick quests, press **+10 XP** on a pursuit after working on it.
- Journal: calendar in the left sidebar (Journals plugin) or the **📓 Today's journal** button.
- Change quests/XP/reward odds in [[Quest Config]] and [[Rewards]]. Re-theme by editing `--rpg-accent` in `.obsidian/snippets/rpg-dashboard.css`.

## Health panel
**Notes with no links at all**
```dataview
LIST FROM -"06 Templates" AND -"99 - Meta" AND -"07 - Archives" AND -"01 - Journal"
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
LIMIT 30
```
**Empty stubs**
```dataview
LIST FROM -"06 Templates" AND -"99 - Meta" AND -"07 - Archives"
WHERE file.size = 0
LIMIT 30
```

## Cautions
- Never run *Templater: Replace templates in the active file* on anything inside `06 Templates` - that is what corrupted the templates before (restored from git).
- Secrets: the Pexels API key (`pexels-banner/data.json`) and a Telegram token in [[Library Pass System]] were committed to git - revoke/rotate them.
