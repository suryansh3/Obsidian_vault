---
type: hub
tags:
  - hub
  - journal
up: "[[MOC]]"
---
# 📓 Journal

Time Garden journal: daily -> weekly -> monthly -> quarterly -> yearly. Notes are created by the **Journals** plugin (the calendar in the left sidebar); today's note is created automatically at launch so the [[Home|dashboard]] can store quests, XP and energy in it.

**Up:** [[MOC]] · **Dashboard:** [[Home]] · **Rules engine:** [[Quest Config]]

## Recent daily notes
```dataview
TABLE WITHOUT ID file.link AS "Day", dayRating AS "Rating", xp AS "XP", alias AS "Title"
FROM "01 - Journal/Daily"
SORT file.name DESC
LIMIT 14
```

## Folders
- `Daily/YYYY/MM-Month/` · `Weekly/YYYY/` · `Monthly/YYYY/` · `Quarterly/YYYY/` · `Yearly/`
- Templates: `06 Templates/Parents` (do not run *Templater: replace templates in active file* inside `06 Templates`).

## Related
- [[Second Brain]] · [[Academics & CS]] · [[Quest Board]] · [[Spiritual]] · [[Core]]
