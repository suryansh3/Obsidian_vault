---
type: config
tags:
  - quest-config
daily_xp_target: 100
roll_cost_xp: 50
quick_xp: 5
slots:
  - "🌅 Morning Musts"
  - "💻 Deep Work"
  - "🌙 Evening Routine"
stats:
  - { name: "Physical", icon: "⚔️", color: "#ef4444" }
  - { name: "Psyche", icon: "🧘", color: "#3b82f6" }
  - { name: "Intel", icon: "🧠", color: "#10b981" }
  - { name: "Craft", icon: "🛠️", color: "#f59e0b" }
  - { name: "Spiritual", icon: "✨", color: "#a855f7" }
  - { name: "Core", icon: "🛡️", color: "#94a3b8" }
quests:
  - { id: "wake", icon: "⏰", name: "Wake up on time", stat: "Core", xp: 10, slot: "🌅 Morning Musts" }
  - { id: "water", icon: "💧", name: "Hydration ritual (500 ml)", stat: "Physical", xp: 10, slot: "🌅 Morning Musts" }
  - { id: "workout", icon: "🏋️", name: "Physical training (30 min)", stat: "Physical", xp: 25, slot: "🌅 Morning Musts" }
  - { id: "plan", icon: "📝", name: "Plan the day (top 3 tasks)", stat: "Core", xp: 10, slot: "🌅 Morning Musts" }
  - { id: "study", icon: "🧠", name: "Deep study block (1 hr)", stat: "Intel", xp: 30, slot: "💻 Deep Work" }
  - { id: "code", icon: "💻", name: "Code / build a project (1 hr)", stat: "Craft", xp: 30, slot: "💻 Deep Work" }
  - { id: "dsa", icon: "🧩", name: "Solve 1 DSA problem", stat: "Intel", xp: 20, slot: "💻 Deep Work" }
  - { id: "read", icon: "📚", name: "Knowledge ingestion (15 min read)", stat: "Intel", xp: 15, slot: "🌙 Evening Routine" }
  - { id: "review", icon: "📓", name: "Daily reflection & log", stat: "Psyche", xp: 15, slot: "🌙 Evening Routine" }
  - { id: "meditate", icon: "🧘", name: "Meditate (10 min)", stat: "Spiritual", xp: 15, slot: "🌙 Evening Routine" }
  - { id: "shutdown", icon: "🔌", name: "Digital sunset (no screens 30 min before bed)", stat: "Spiritual", xp: 20, slot: "🌙 Evening Routine" }
---
# ⚙️ Quest Config

This note is the **rules engine** of the [[Home|dashboard]]. Edit the properties above (Properties panel or source mode) and the dashboard updates the next time it is opened.

| Setting | Meaning |
| --- | --- |
| `daily_xp_target` | XP that fills the "Daily XP" bar |
| `roll_cost_xp` | Every this-many XP earned today unlocks one gacha roll ([[Rewards]]) |
| `quick_xp` | XP given by the quick-win buttons on the dashboard |
| `stats` | The six attributes shown on the radar - each has a matching note in [[Quest Board#Areas|Areas]] |
| `quests` | The daily checklist. `id` must be unique; `stat` must match a stat name; `slot` groups quests |

## How XP flows
1. Tick a quest on [[Home]] -> it is saved in today's [[Journal|daily note]] (`quests_done`, `xp`, `statxp`).
2. Stat total = the **base XP** in the matching area note + all daily XP ever earned.
3. Total XP / 100 = your **level**. Rank: E (<10) -> D -> C (20) -> B (30) -> A (45) -> S (60).
4. Pursuits (long-term goals) get XP with the **+10 XP** button on their card.

Related: [[Character]] · [[Rewards]] · [[Rules for Life]] · [[Dopamine Menu]] · [[Quest Board]]

↑ Up: [[Quest Board]] · [[MOC]]
