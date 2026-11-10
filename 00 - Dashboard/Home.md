---
cssclasses:
  - rpg-dashboard
tags:
  - dashboard
type: dashboard
---
```dataviewjs
// ===== Life Gamification dashboard (Dataview JS) =====
const A = app;
const root = dv.container;
const P = {
  cfg: "02 - Quests/Quest Config.md", char: "02 - Quests/Character.md", rew: "02 - Quests/Rewards.md",
  rules: "02 - Quests/Rules for Life.md", menu: "02 - Quests/Dopamine Menu.md",
  areas: "02 - Quests/Areas/", pursuits: "02 - Quests/Pursuits/", daily: "01 - Journal/Daily/",
  hero: "06 Templates/Images/DashboardBanner.gif", banners: "06 Templates/Images/Daily Notes/",
};
const DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const pad = (n) => String(n).padStart(2, "0");
const ymd = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
const jpath = (d) => `${P.daily}${d.getFullYear()}/${pad(d.getMonth() + 1)}-${MONTHS[d.getMonth()]}/${ymd(d)}-${DAYS[d.getDay()]}.md`;
const getFile = (p) => A.vault.getAbstractFileByPath(p);
const fmOf = (f) => (f ? A.metadataCache.getFileCache(f)?.frontmatter ?? {} : {});
const num = (v, d = 0) => { const n = Number(v); return Number.isFinite(n) ? n : d; };
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const resUrl = (p) => { const f = getFile(p); return f ? A.vault.getResourcePath(f) : ""; };
const filesIn = (prefix) => A.vault.getMarkdownFiles().filter((f) => f.path.startsWith(prefix));
const arr = (v) => (Array.isArray(v) ? v : []);

// ---------- config ----------
const cfg = fmOf(getFile(P.cfg));
const char = fmOf(getFile(P.char));
const STATS = arr(cfg.stats).length ? cfg.stats : [
  { name: "Physical", icon: "⚔️", color: "#ef4444" }, { name: "Psyche", icon: "🧘", color: "#3b82f6" },
  { name: "Intel", icon: "🧠", color: "#10b981" }, { name: "Craft", icon: "🛠️", color: "#f59e0b" },
  { name: "Spiritual", icon: "✨", color: "#a855f7" }, { name: "Core", icon: "🛡️", color: "#94a3b8" },
];
const QUESTS = arr(cfg.quests);
const SLOTS = arr(cfg.slots).length ? cfg.slots : ["Morning Musts", "Evening Routine"];
const TARGET = num(cfg.daily_xp_target, 100);
const ROLL_COST = num(cfg.roll_cost_xp, 50);
const QUICK = num(cfg.quick_xp, 5);
const PER = Math.max(1, num(char.xp_per_level, 100));
const statColor = (n) => (STATS.find((s) => s.name === n) || {}).color || "#22c55e";
const statIcon = (n) => (STATS.find((s) => s.name === n) || {}).icon || "⭐";

const now = new Date();
const todayKey = ymd(now);
const todayPath = jpath(now);
const dayOfYear = Math.floor((now - new Date(now.getFullYear(), 0, 0)) / 86400000);

// ---------- state ----------
function readToday() {
  const f = getFile(todayPath);
  const fm = fmOf(f);
  return {
    exists: !!f, hp: num(fm.hp, 80), mood: num(fm.mood, 80), concentration: num(fm.concentration, 80), motivation: num(fm.motivation, 80),
    done: arr(fm.quests_done).slice(), bonus: fm.bonus && typeof fm.bonus === "object" ? { ...fm.bonus } : {},
    rolls: num(fm.rolls, 0), loot: arr(fm.loot).slice(),
  };
}
function calc(st) {
  const per = {}; STATS.forEach((s) => (per[s.name] = 0));
  let total = 0;
  for (const q of QUESTS) if (st.done.includes(q.id)) { per[q.stat] = (per[q.stat] || 0) + num(q.xp); total += num(q.xp); }
  for (const [k, v] of Object.entries(st.bonus)) { per[k] = (per[k] || 0) + num(v); total += num(v); }
  return { per, total };
}
function loadHistory() {
  const h = {};
  for (const f of filesIn(P.daily)) {
    const key = f.basename.slice(0, 10);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(key) || key === todayKey) continue;
    const fm = fmOf(f);
    h[key] = { xp: num(fm.xp, 0), per: fm.statxp && typeof fm.statxp === "object" ? fm.statxp : {} };
  }
  return h;
}
function baseStats() {
  const b = {}; STATS.forEach((s) => (b[s.name] = 0));
  for (const f of filesIn(P.areas)) { const fm = fmOf(f); if (fm.stat && fm.stat in b) b[fm.stat] += num(fm.xp, 0); }
  return b;
}
let st = readToday();
const hist = loadHistory();
const base = baseStats();

async function persist() {
  const f = getFile(todayPath);
  if (!f) return;
  const c = calc(st);
  await A.fileManager.processFrontMatter(f, (fm) => {
    fm.hp = st.hp; fm.mood = st.mood; fm.concentration = st.concentration; fm.motivation = st.motivation;
    fm.quests_done = st.done; fm.xp = c.total; fm.statxp = c.per; fm.bonus = st.bonus; fm.rolls = st.rolls; fm.loot = st.loot;
  });
}
const shuffle = (window.__rpgShuffle = window.__rpgShuffle || { dayKey: todayKey, rule: 0, dop: 0 });
if (shuffle.dayKey !== todayKey) { shuffle.dayKey = todayKey; shuffle.rule = 0; shuffle.dop = 0; }

// ---------- derived ----------
function derived() {
  const c = calc(st);
  const totals = {}; STATS.forEach((s) => (totals[s.name] = base[s.name] || 0));
  for (const h of Object.values(hist)) for (const [k, v] of Object.entries(h.per)) if (k in totals) totals[k] += num(v);
  for (const [k, v] of Object.entries(c.per)) if (k in totals) totals[k] += v;
  const total = Object.values(totals).reduce((a, b) => a + b, 0);
  const level = Math.floor(total / PER) + 1;
  const into = total % PER;
  const rank = level >= 60 ? "S" : level >= 45 ? "A" : level >= 30 ? "B" : level >= 20 ? "C" : level >= 10 ? "D" : "E";
  // streak
  const xpOn = (d) => (ymd(d) === todayKey ? c.total : (hist[ymd(d)] || {}).xp || 0);
  let streak = 0; const cur = new Date(now);
  if (xpOn(cur) <= 0) cur.setDate(cur.getDate() - 1);
  while (xpOn(cur) > 0) { streak++; cur.setDate(cur.getDate() - 1); }
  let best = 0, run = 0;
  const keys = Object.keys(hist).concat(c.total > 0 ? [todayKey] : []).sort();
  let prev = null;
  for (const k of keys) {
    if (((k === todayKey ? c.total : hist[k].xp) || 0) <= 0) { run = 0; prev = null; continue; }
    const d = new Date(k + "T00:00:00");
    run = prev && Math.round((d - prev) / 86400000) === 1 ? run + 1 : 1;
    prev = d; best = Math.max(best, run);
  }
  return { c, totals, total, level, into, rank, streak, best: Math.max(best, streak) };
}

// ---------- svg widgets ----------
function radarSvg(totals) {
  const n = STATS.length, cx = 160, cy = 150, R = 100;
  const vals = STATS.map((s) => totals[s.name] || 0);
  const max = Math.max(100, Math.ceil(Math.max(...vals) / 100) * 100);
  const pt = (i, r) => { const a = -Math.PI / 2 + (2 * Math.PI * i) / n; return [cx + r * Math.cos(a), cy + r * Math.sin(a)]; };
  let s = `<svg viewBox="0 0 320 300" class="rpg-radar">`;
  for (let k = 1; k <= 4; k++) s += `<polygon points="${STATS.map((_, i) => pt(i, (R * k) / 4).join(",")).join(" ")}" class="ring"/>`;
  STATS.forEach((_, i) => { const [x, y] = pt(i, R); s += `<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" class="axis"/>`; });
  s += `<polygon points="${vals.map((v, i) => pt(i, (R * v) / max).join(",")).join(" ")}" class="shape"/>`;
  vals.forEach((v, i) => { const [x, y] = pt(i, (R * v) / max); s += `<circle cx="${x}" cy="${y}" r="3.5" class="dot"/>`; });
  STATS.forEach((t, i) => {
    const [x, y] = pt(i, R + 26);
    s += `<text x="${x}" y="${y}" text-anchor="middle" dominant-baseline="middle" class="lbl">${esc(t.icon)} ${esc(t.name)}</text>`;
    s += `<text x="${x}" y="${y + 13}" text-anchor="middle" dominant-baseline="middle" class="val">${vals[i]}</text>`;
  });
  return s + `</svg>`;
}
function lineSvg(series) {
  const W = 560, H = 170, L = 28, B = 22, T = 10;
  const max = Math.max(TARGET, ...series.map((p) => p.v), 10);
  const x = (i) => L + ((W - L - 8) * i) / Math.max(1, series.length - 1);
  const y = (v) => T + (H - T - B) * (1 - v / max);
  const pts = series.map((p, i) => `${x(i)},${y(p.v)}`).join(" ");
  let s = `<svg viewBox="0 0 ${W} ${H}" class="rpg-line">`;
  [0, 0.5, 1].forEach((f) => { const yy = T + (H - T - B) * (1 - f); s += `<line x1="${L}" x2="${W - 8}" y1="${yy}" y2="${yy}" class="grid"/><text x="${L - 4}" y="${yy + 3}" text-anchor="end" class="tick">${Math.round(max * f)}</text>`; });
  s += `<line x1="${L}" x2="${W - 8}" y1="${y(TARGET)}" y2="${y(TARGET)}" class="target"/>`;
  s += `<polygon points="${x(0)},${y(0)} ${pts} ${x(series.length - 1)},${y(0)}" class="area"/><polyline points="${pts}" class="path"/>`;
  series.forEach((p, i) => { if (p.v > 0) s += `<circle cx="${x(i)}" cy="${y(p.v)}" r="2.6" class="dot"><title>${p.k}: ${p.v} XP</title></circle>`; if (i % 5 === 0 || i === series.length - 1) s += `<text x="${x(i)}" y="${H - 6}" text-anchor="middle" class="tick">${p.k.slice(8)}</text>`; });
  return s + `</svg>`;
}

// ---------- html ----------
function build(d) {
  const { c, totals, total, level, into, rank, streak, best } = d;
  const hello = now.getHours() < 12 ? "Good morning" : now.getHours() < 18 ? "Good afternoon" : "Good evening";
  const heroUrl = resUrl(P.hero);
  const avatarUrl = resUrl(`${P.banners}${DAYS[now.getDay()]}Banner.avif`) || heroUrl;
  const pct = clamp(Math.round((c.total / TARGET) * 100), 0, 100);
  const energy = [["hp", "❤️", "HP"], ["mood", "😊", "Mood"], ["concentration", "🎯", "Focus"], ["motivation", "🔥", "Motivation"]];
  const rules = arr(fmOf(getFile(P.rules)).rules);
  const menu = arr(fmOf(getFile(P.menu)).menu);
  const rule = rules.length ? rules[(dayOfYear + shuffle.rule) % rules.length] : "";
  const dop = menu.length ? menu[(dayOfYear * 7 + shuffle.dop) % menu.length] : null;
  const rewards = arr(fmOf(getFile(P.rew)).rewards);
  const rollsLeft = Math.max(0, Math.floor(c.total / ROLL_COST) - st.rolls);

  // heatmap: last 28 days
  let heat = "";
  for (let i = 27; i >= 0; i--) {
    const dd = new Date(now); dd.setDate(dd.getDate() - i);
    const v = ymd(dd) === todayKey ? c.total : (hist[ymd(dd)] || {}).xp || 0;
    const lv = v <= 0 ? 0 : v < TARGET * 0.4 ? 1 : v < TARGET * 0.8 ? 2 : v < TARGET ? 3 : 4;
    heat += `<span class="hm l${lv}" title="${ymd(dd)}: ${v} XP"></span>`;
  }
  // series: last 30 days
  const series = [];
  for (let i = 29; i >= 0; i--) {
    const dd = new Date(now); dd.setDate(dd.getDate() - i);
    series.push({ k: ymd(dd), v: ymd(dd) === todayKey ? c.total : (hist[ymd(dd)] || {}).xp || 0 });
  }
  // quests html
  const questHtml = SLOTS.map((slot) => {
    const qs = QUESTS.filter((q) => (q.slot || SLOTS[0]) === slot);
    if (!qs.length) return "";
    return `<div class="slot">${esc(slot)}</div>` + qs.map((q) => {
      const on = st.done.includes(q.id);
      return `<label class="quest ${on ? "done" : ""} ${st.exists ? "" : "off"}" data-act="quest" data-id="${esc(q.id)}"><span class="box">${on ? "✔" : ""}</span><span class="qname">${esc(q.icon || "")} ${esc(q.name)}</span><span class="qxp" style="color:${statColor(q.stat)}">+${num(q.xp)} ${esc(q.stat)}</span></label>`;
    }).join("");
  }).join("");
  // pursuits
  const pursuits = filesIn(P.pursuits).sort((a, b) => a.basename.localeCompare(b.basename)).map((f) => {
    const fm = fmOf(f), xp = num(fm.xp), goal = Math.max(1, num(fm.xp_goal, 100)), p = clamp(Math.round((xp / goal) * 100), 0, 100);
    return `<div class="pcard"><div class="phead"><span class="picon" data-act="open" data-path="${esc(f.path)}">${esc(fm.icon || "🎯")}</span><span class="pstatus">${esc(fm.status || "Active")}</span></div>
      <div class="ptitle" data-act="open" data-path="${esc(f.path)}">${esc(fm.title || f.basename)}</div><div class="pdesc">${esc(fm.description || "")}</div>
      <div class="bar"><i style="width:${p}%"></i></div><div class="pfoot"><span>${xp} / ${goal} XP · ${p}%</span><button class="mini" data-act="pursuit" data-path="${esc(f.path)}">+10 XP</button></div></div>`;
  }).join("");
  // vault pulse
  const all = A.vault.getMarkdownFiles();
  const skip = /^(06 Templates|99 - Meta|07 - Archives|01 - Journal|00 - Dashboard)/;
  const recent = all.filter((f) => !skip.test(f.path)).sort((a, b) => b.stat.mtime - a.stat.mtime).slice(0, 6);
  const inbound = new Set();
  const rl = A.metadataCache.resolvedLinks || {};
  for (const [src, tg] of Object.entries(rl)) for (const t of Object.keys(tg)) if (t !== src) inbound.add(t);
  const orphans = all.filter((f) => !skip.test(f.path) && !inbound.has(f.path) && !Object.keys(rl[f.path] || {}).length).length;
  const loot = st.loot.map((l) => `<li>${esc(l)}</li>`).join("");
  const tierColor = { Common: "#94a3b8", Rare: "#3b82f6", Epic: "#a855f7", Legendary: "#f59e0b" };

  return `
<div class="rpg-hero" style="background-image:url('${heroUrl}')"><div class="rpg-hero-in"><div class="h-title">🎮 Life Gamification</div><div class="h-sub">${esc(hello)}, ${esc(char.char_name || "Hunter")} · ${DAYS[now.getDay()]}, ${MONTHS[now.getMonth()]} ${now.getDate()} · 🔥 ${streak}-day streak</div></div></div>
<div class="rpg-grid">
 <div class="col">
  <div class="card lvl"><span>⏫ LEVEL ${level}</span><span class="rank r-${rank}">${rank}-Rank</span></div>
  <div class="avatar" style="background-image:url('${avatarUrl}')"><div class="cap">${esc(char.char_name || "Hunter")}<small>${esc(char.class || "")} · ${esc(char.title || "")}</small></div></div>
  <div class="card"><div class="ctitle">💗 Daily Energy <small>(click a bar to set)</small></div>
   ${energy.map(([k, ic, nm]) => `<div class="erow"><span>${ic} ${nm}</span><b>${st[k]}%</b></div><div class="segs">${Array.from({ length: 10 }, (_, i) => `<span class="seg ${st[k] >= (i + 1) * 10 ? "on" : ""} e-${k}" data-act="energy" data-key="${k}" data-val="${(i + 1) * 10}"></span>`).join("")}</div>`).join("")}
  </div>
  <div class="card"><div class="ctitle">📊 Stats</div>
   ${STATS.map((s) => `<div class="srow" data-act="open" data-path="${P.areas}${esc(s.name)}.md"><span>${esc(s.icon)} ${esc(s.name)}</span><b style="color:${s.color}">${totals[s.name]}</b><div class="bar sm"><i style="width:${clamp(((totals[s.name] || 0) % PER) / PER * 100, 0, 100)}%;background:${s.color}"></i></div></div>`).join("")}
   <div class="sum">SUM <b>${total}</b></div></div>
 </div>
 <div class="col mid">
  <div class="card"><div class="ctitle">🕸️ Attribute Radar</div>${radarSvg(totals)}</div>
  <div class="card"><div class="ctitle">📈 XP — last 30 days <small>(dashed = daily target)</small></div>${lineSvg(series)}<div class="heat">${heat}</div><div class="hnote">last 28 days · best streak ${best} days</div></div>
  <div class="ctitle big">« Choose Your Pursuits »</div>
  <div class="pgrid">${pursuits || "<i>No pursuits yet - add notes to 02 - Quests/Pursuits</i>"}</div>
 </div>
 <div class="col">
  <div class="card xp"><div class="xpt">⚗️ XP: ${total}</div><div class="xps">To reach Level ${level + 1} attain ${PER - into} XP</div><div class="bar"><i style="width:${Math.round((into / PER) * 100)}%"></i></div></div>
  <div class="card daily"><div class="dxp"><b>${c.total}/${TARGET}</b><span>Daily XP</span></div><div class="bar big"><i style="width:${pct}%"></i></div>
   <div class="quick">${STATS.map((s) => `<button class="mini" style="border-color:${s.color}" data-act="bonus" data-stat="${esc(s.name)}" title="Quick win: +${QUICK} ${esc(s.name)}">${esc(s.icon)}+${QUICK}</button>`).join("")}<button class="mini ghost" data-act="bonus-reset" title="Clear bonus XP">↺</button></div></div>
  <div class="card"><div class="ctitle">📜 Hero's Mission <small>${todayKey}</small></div>
   ${st.exists ? "" : `<div class="warn">Today's journal isn't created yet. <button class="mini" data-act="journal">Create it</button></div>`}${questHtml}</div>
  <div class="card gacha"><div class="ctitle">🎰 Gacha Rolls <small>1 roll per ${ROLL_COST} XP</small></div>
   <button class="roll" data-act="roll" ${rollsLeft > 0 && st.exists && rewards.length ? "" : "disabled"}>${rollsLeft > 0 ? `Roll reward (${rollsLeft} left)` : `Earn ${ROLL_COST} XP to unlock`}</button>
   ${loot ? `<ul class="loot">${loot}</ul>` : ""}
   <div class="tiers">${Object.entries(tierColor).map(([k, v]) => `<span style="color:${v}">● ${k}</span>`).join(" ")}</div></div>
  <div class="card"><div class="ctitle">🧭 Rule of the day <button class="mini ghost" data-act="shuffle" data-what="rule">🔄</button></div><div class="rule">${esc(rule) || "<i>Add rules in Rules for Life</i>"}</div></div>
  <div class="card"><div class="ctitle">🍬 Dopamine menu <button class="mini ghost" data-act="shuffle" data-what="dop">🔄</button></div><div class="rule">${dop ? `<small>${esc(dop.cat || "")}</small><br>${esc(dop.item || dop)}` : "<i>Add items in Dopamine Menu</i>"}</div></div>
  <div class="card"><div class="ctitle">⚡ Quick actions</div><div class="qa">
   <button class="mini" data-act="journal">📓 Today's journal</button>
   <button class="mini" data-act="open" data-path="00 - Dashboard/MOC.md">🗺️ MOC</button>
   <button class="mini" data-act="open" data-path="02 - Quests/Quest Board.md">⚔️ Quest board</button>
   <button class="mini" data-act="open" data-path="05 - Second Brain & Knowledge/Second Brain.md">🧠 Second brain</button>
   <button class="mini" data-act="open" data-path="04 - Academics & CS/Academics & CS.md">🎓 Academics</button></div></div>
  <div class="card"><div class="ctitle">🌱 Second brain pulse</div><div class="pulse">${all.length} notes · ${orphans} unlinked</div>
   <ul class="recent">${recent.map((f) => `<li data-act="open" data-path="${esc(f.path)}">${esc(f.basename)}</li>`).join("")}</ul></div>
 </div>
</div>`;
}

// ---------- render + events ----------
async function act(el) {
  const a = el.dataset.act;
  if (a === "open") return A.workspace.openLinkText(el.dataset.path.replace(/\.md$/, ""), "", false);
  if (a === "journal") return A.commands.executeCommandById("journals::open-daily-note");
  if (a === "shuffle") { shuffle[el.dataset.what] += 1; return render(); }
  if (a === "pursuit") {
    const f = getFile(el.dataset.path);
    if (f) await A.fileManager.processFrontMatter(f, (fm) => { fm.xp = num(fm.xp) + 10; });
    return;
  }
  if (!st.exists) return;
  if (a === "quest") { const i = st.done.indexOf(el.dataset.id); if (i >= 0) st.done.splice(i, 1); else st.done.push(el.dataset.id); }
  else if (a === "energy") st[el.dataset.key] = num(el.dataset.val);
  else if (a === "bonus") st.bonus[el.dataset.stat] = num(st.bonus[el.dataset.stat]) + QUICK;
  else if (a === "bonus-reset") st.bonus = {};
  else if (a === "roll") {
    const rewards = arr(fmOf(getFile(P.rew)).rewards);
    const left = Math.floor(calc(st).total / ROLL_COST) - st.rolls;
    if (left <= 0 || !rewards.length) return;
    let r = Math.random() * rewards.reduce((s, x) => s + num(x.weight, 1), 0), pick = rewards[0];
    for (const x of rewards) { if (r < num(x.weight, 1)) { pick = x; break; } r -= num(x.weight, 1); }
    st.rolls += 1; st.loot.push(`${pick.tier || ""} - ${pick.name}`);
  }
  render();
  await persist();
}
function render() {
  const wrap = document.createElement("div");
  wrap.className = "rpg-home";
  wrap.innerHTML = build(derived());
  wrap.querySelectorAll("[data-act]").forEach((el) => el.addEventListener("click", (e) => { e.preventDefault(); act(el); }));
  root.empty();
  root.appendChild(wrap);
}
render();
```

---
<small>🗺️ [[MOC]] · 📘 [[Vault Guide]] · ⚔️ [[Quest Board]] · ⚙️ [[Quest Config]] · 📓 [[Journal]] - this page opens automatically every time you launch Obsidian (Homepage plugin).</small>
