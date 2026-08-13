---
tags:
  - Dashboard
  - RPG
cssclasses:
  - rpg-dashboard
---

# ⚔️ RPG LIFE SYSTEM DASHBOARD

![[99 - Meta/Character.md]]

---

## ⚡ TODAY'S ENERGY BARS

```dataviewjs
const todayStr = moment().format("YYYYMMDD");
let todayNote = dv.page(`01 - Daily/${todayStr}`) || dv.page(`"01 - Daily/${todayStr}"`);
if (!todayNote) {
    const pages = dv.pages('"01 - Daily"').sort(p => p.file.name, "desc");
    if (pages.length > 0) todayNote = pages[0];
}

const hp = todayNote?.hp ?? 85;
const mood = todayNote?.mood ?? 75;
const conc = todayNote?.concentration ?? 90;
const mot = todayNote?.motivation ?? 70;

const bars = [
    { label: "HEALTH (HP)", val: hp, color: "#ef4444", icon: "❤️" },
    { label: "MOOD", val: mood, color: "#f59e0b", icon: "😊" },
    { label: "CONCENTRATION", val: conc, color: "#06b6d4", icon: "🎯" },
    { label: "MOTIVATION", val: mot, color: "#8b5cf6", icon: "🔥" }
];

let html = `<div class="rpg-stat-grid">`;
for (let b of bars) {
    const p = Math.min(Math.max(b.val, 0), 100);
    html += `
    <div class="rpg-bar-item">
      <div class="rpg-bar-header">
        <span>${b.icon} <strong>${b.label}</strong></span>
        <span class="rpg-bar-val">${p}%</span>
      </div>
      <div class="rpg-progress-track">
        <div class="rpg-progress-fill" style="width: ${p}%; background: ${b.color}; box-shadow: 0 0 10px ${b.color}aa;"></div>
      </div>
    </div>`;
}
html += `</div>`;
dv.el("div", html, { raw: true });
```

---

## 📊 ATTRIBUTE STAT TREE

```dataviewjs
const stats = {
    "Physical": { icon: "⚔️", color: "#ef4444" },
    "Psyche":   { icon: "🧘", color: "#3b82f6" },
    "Intel":    { icon: "🧠", color: "#10b981" },
    "Craft":    { icon: "🛠️", color: "#f59e0b" },
    "Spiritual":{ icon: "✨", color: "#8b5cf6" },
    "Core":     { icon: "🛡️", color: "#64748b" }
};

const areaPages = dv.pages('#Area').concat(dv.pages('"99 - Meta/Areas"'));
const dailyPages = dv.pages('"01 - Daily"');
let xpTotals = { "Physical": 120, "Psyche": 90, "Intel": 210, "Craft": 150, "Spiritual": 80, "Core": 110 };

for (let p of areaPages) {
    if (p.stat && xpTotals[p.stat] !== undefined) xpTotals[p.stat] += (p.xp || 0);
}

for (let dp of dailyPages) {
    if (dp.file.tasks) {
        for (let t of dp.file.tasks) {
            if (t.completed && t.stat && xpTotals[t.stat] !== undefined) {
                xpTotals[t.stat] += (t.xp || 10);
            }
        }
    }
}

let html = `<div class="rpg-stat-tree">`;
for (let [name, data] of Object.entries(stats)) {
    const xp = xpTotals[name] || 0;
    const level = Math.floor(xp / 100) + 1;
    const progress = (xp % 100);
    html += `
    <div class="rpg-stat-row">
      <div class="rpg-stat-meta">
        <span>${data.icon} <strong>${name}</strong> (Level ${level})</span>
        <span class="rpg-stat-xp">${xp} XP</span>
      </div>
      <div class="rpg-progress-track">
        <div class="rpg-progress-fill" style="width: ${progress}%; background: ${data.color};"></div>
      </div>
    </div>`;
}
html += `</div>`;
dv.el("div", html, { raw: true });
```

---

## 🎯 QUEST PURSUITS

```dataviewjs
const pursuits = dv.pages('#Pursuit').concat(dv.pages('"99 - Meta/Pursuits"')).sort(p => p.file.name, "asc");

if (pursuits.length === 0) {
    dv.paragraph("*No active pursuits found.*");
} else {
    let html = `<div class="rpg-quest-grid">`;
    for (let p of pursuits) {
        const xp = p.xp || 0;
        const goal = p.xp_goal || 100;
        const percent = Math.min(Math.round((xp / goal) * 100), 100);
        const icon = p.icon || "⚔️";
        const status = p.status || "Active";
        
        html += `
        <div class="rpg-quest-card">
          <div class="rpg-quest-header">
            <span class="rpg-quest-icon">${icon}</span>
            <span class="rpg-quest-status">${status}</span>
          </div>
          <h3 class="rpg-quest-title">${p.title || p.file.name}</h3>
          <p class="rpg-quest-desc">${p.description || "Active quest line"}</p>
          <div class="rpg-quest-progress">
            <div class="rpg-quest-labels">
              <span>EXP</span>
              <span>${xp} / ${goal} (${percent}%)</span>
            </div>
            <div class="rpg-progress-track">
              <div class="rpg-progress-fill green" style="width: ${percent}%;"></div>
            </div>
          </div>
        </div>`;
    }
    html += `</div>`;
    dv.el("div", html, { raw: true });
}
```

---

## 🎲 REWARD SUMMONING

![[99 - Meta/Rewards.md]]
