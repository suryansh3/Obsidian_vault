  ### File 3: `99 - Meta/Rewards.md`
    ```markdown
    ---
    rewards:
      - name: "Specialty Coffee / Boba Treat"
        tier: "Common"
        weight: 40
      - name: "1 Hour Gaming Session"
        tier: "Rare"
        weight: 30
      - name: "Movie Night / Favorite Show Binge"
        tier: "Rare"
        weight: 20
      - name: "Cheat Meal Feast"
        tier: "Epic"
        weight: 8
      - name: "Wishlist Item Purchase (< $50)"
        tier: "Legendary"
        weight: 2
    ---

    # 🎁 GACHA REWARD SYSTEM

    ```dataviewjs
    const btn = container.createEl("button", {
        text: "🎲 ROLL REWARD (GACHA SYSTEM)",
        cls: "rpg-gacha-btn"
    });

    const resultDiv = container.createEl("div", { cls: "rpg-gacha-result" });

    const rewardsList = [
        { name: "☕ Specialty Coffee / Boba Treat", tier: "Common", weight: 40, color: "#94a3b8" },
        { name: "🎮 1 Hour Gaming Session", tier: "Rare", weight: 30, color: "#3b82f6" },
        { name: "🎬 Movie Night / Favorite Show Binge", tier: "Rare", weight: 20, color: "#a855f7" },
        { name: "🍕 Cheat Meal Feast", tier: "Epic", weight: 8, color: "#f59e0b" },
        { name: "🎁 Wishlist Item Purchase (< $50)", tier: "Legendary", weight: 2, color: "#ef4444" }
    ];

    btn.onclick = () => {
        resultDiv.innerHTML = `<span class="rpg-rolling">Summoning Loot... 🔮</span>`;
        setTimeout(() => {
            const totalWeight = rewardsList.reduce((acc, r) => acc + r.weight, 0);
            let random = Math.random() * totalWeight;
            let selected = rewardsList[0];

            for (let r of rewardsList) {
                if (random < r.weight) {
                    selected = r;
                    break;
                }
                random -= r.weight;
            }

            resultDiv.innerHTML = `
            <div class="rpg-loot-box" style="border-color: ${selected.color}">
              <div class="rpg-loot-header" style="background: ${selected.color}22; color: ${selected.color}">
                ★ ${selected.tier.toUpperCase()} ITEM UNLOCKED! ★
              </div>
              <div class="rpg-loot-body">
                <h3>${selected.name}</h3>
                <p>Claim your reward for completing milestone achievements!</p>
              </div>
            </div>`;
        }, 600);
    };


    ---