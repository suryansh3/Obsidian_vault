---
type: hub
tags:
  - hub
  - quests
up: "[[MOC]]"
---
# ⚔️ Quest Board

The RPG layer of the vault. Progress is shown on [[Home]]; the rules live in [[Quest Config]].

**Up:** [[MOC]] · **Dashboard:** [[Home]] · [[Character]] · [[Rewards]] · [[Rules for Life]] · [[Dopamine Menu]]

## Pursuits
- 🚀 [[Career]] ↔ [[Projects]], [[Academics & CS]]
- 🎥 [[YouTube]] ↔ [[Content Creation]]
- 💰 [[Income]] ↔ [[Career]]
- ✍️ [[Content Creation]] ↔ [[Second Brain]]

```dataview
TABLE WITHOUT ID file.link AS "Pursuit", status AS "Status", xp AS "XP", xp_goal AS "Goal", description AS "About"
FROM "02 - Quests/Pursuits"
SORT file.name
```

## Areas
- ⚔️ [[Physical]] ↔ [[Clippings Index#Fitness & Looks|fitness clippings]]
- 🧘 [[Psyche]] ↔ [[Clippings Index#Self Improvement|self-improvement clippings]]
- 🧠 [[Intel]] ↔ [[Academics & CS]], [[AI & ML Roadmap]]
- 🛠️ [[Craft]] ↔ [[Projects]]
- ✨ [[Spiritual]] ↔ [[Rules for Life]]
- 🛡️ [[Core]] ↔ [[Journal]]

```dataview
TABLE WITHOUT ID file.link AS "Area", stat AS "Stat", xp AS "Base XP", description AS "About"
FROM "02 - Quests/Areas"
SORT file.name
```
