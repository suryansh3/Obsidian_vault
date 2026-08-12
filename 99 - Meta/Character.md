 ## 3. ⚔️ Component Breakdown & Implementation

  ### Feature 1: Character Sheet (Level, Rank, XP)

  • Location: Place in 99 - Meta/Character.md.
  • YAML Frontmatter:

    ---
    char_name: "Shadow Monarch"
    class: "Scholar / Engineer"
    title: "The System Awakened"
    level: 5
    rank: E
    total_xp: 450
    xp_to_next_level: 500
    ---

  • DataviewJS Code Block:

    const page = dv.page("99 - Meta/Character.md") || dv.current();
    const totalXp = page.total_xp || 0;

    // Dynamic XP Formula: XP required scales with level
    function getLevelInfo(xp) {
        let lvl = 1;
        let req = 500;
        while (xp >= req) {
            xp -= req;
            lvl++;
            req = Math.floor(500 * Math.pow(lvl, 1.3));
        }
        return { level: lvl, currentXp: xp, nextLevelReq: req };
    }

    const info = getLevelInfo(totalXp);
    const level = page.level || info.level;
    const reqXp = page.xp_to_next_level || info.nextLevelReq;
    const currentLevelXp = totalXp % reqXp;
    const percent = Math.min(Math.round((currentLevelXp / reqXp) * 100), 100);

    // Rank Tiering Logic
    function getRank(lvl) {
        if (lvl >= 75) return { name: "S-Rank", class: "rank-s" };
        if (lvl >= 50) return { name: "A-Rank", class: "rank-a" };
        if (lvl >= 30) return { name: "B-Rank", class: "rank-b" };
        if (lvl >= 15) return { name: "C-Rank", class: "rank-c" };
        if (lvl >= 6)  return { name: "D-Rank", class: "rank-d" };
        return { name: "E-Rank", class: "rank-e" };
    }

    const rankInfo = getRank(level);

    dv.el("div", `
    <div class="rpg-character-card">
      <div class="rpg-header">
        <div class="rpg-avatar-box">
          <span class="rpg-avatar-icon">👑</span>
        </div>
        <div class="rpg-char-details">
          <h2 class="rpg-name">${page.char_name || "PLAYER"}</h2>
          <div class="rpg-badges">
            <span class="rpg-badge rpg-level-badge">LVL ${level}</span>
            <span class="rpg-badge rpg-rank-badge ${rankInfo.class}">${rankInfo.name}</span>
            <span class="rpg-title-tag">${page.title || "Hunter"}</span>
          </div>
        </div>
      </div>
      <div class="rpg-xp-container">
        <div class="rpg-xp-labels">
          <span class="rpg-xp-title">EXP PROGRESS</span>
          <span class="rpg-xp-val">${currentLevelXp} / ${reqXp} XP (${percent}%)</span>
        </div>
        <div class="rpg-progress-track">
          <div class="rpg-progress-fill green" style="width: ${percent}%;"></div>
        </div>
      </div>
    </div>
    `, { raw: true });