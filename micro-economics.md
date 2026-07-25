# Microeconomic Analysis (MEC-101) - Complete Study Guide

## Course Code: MEC-101 | Credits: 6 | MA Economics (MEC/MAEC)

---

# Part 1: Syllabus & Topic Analysis

## 📚 Course Structure (8 Blocks)

| Block | Topic | Units |
|-------|-------|-------|
| Block 1 | Consumer Behaviour | Units 1-3 |
| Block 2 | Producer Behaviour | Units 4-6 |
| Block 3 | Price and Output Determination | Units 7-10 |
| Block 4 | General Equilibrium | Units 11-12 |
| Block 5 | Welfare Economics | Units 13-16 |
| Block 6 | Economics of Uncertainty | Units 17-19 |
| Block 7 | Non-Cooperative Game Theory-I | Units 20-22 |
| Block 8 | Non-Cooperative Game Theory-II | Units 23-26 |

---

## 🎯 Topic-wise Weightage Analysis (Based on PYQs 2023-2025)

### HIGH Priority Topics (Appear in 3+ exams)

| Topic | Frequency | Marks Range |
|-------|-----------|-------------|
| **Slutsky Equation & Duality** | 4 times | 10-15 marks |
| **Cobb-Douglas Production/Utility** | 4 times | 10-20 marks |
| **Nash Equilibrium & Game Theory** | 4 times | 15-20 marks |
| **Efficiency Wage** | 3 times | 12 marks |
| **Cobweb Model (Dynamic Stability)** | 3 times | 20 marks |
| **Cournot/Bertrand Oligopoly** | 3 times | 12-20 marks |
| **Welfare Theorems** | 3 times | 10-15 marks |

### MEDIUM Priority Topics

| Topic | Frequency | Marks Range |
|-------|-----------|-------------|
| Price Discrimination | 2 times | 10 marks |
| Perfect Competition (LR Equilibrium) | 2 times | 12 marks |
| Risk & Uncertainty (VNM) | 2 times | 10-12 marks |
| Compensated vs Ordinary Demand | 2 times | 12 marks |
| Quasi-concavity of Utility | 2 times | 12 marks |
| Pooling/Separating Equilibrium | 2 times | 15 marks |

### LOW Priority Topics (Appear once)

- Walrasian Dynamic Stability
- Edgeworth Box
- Inter-temporal Consumption
- Shepard's Lemma
- Hotelling's Lemma
- St. Petersburg Paradox
- Bertrand Paradox
- Rawls' Theory of Justice

---

## 📊 Most Repeated Questions (2019-2025)

### 🔥 Top 10 Repeated Questions

1. **Slutsky Equation derivation and decomposition** - Asked in Dec 2024, Dec 2025, June 2025
2. **Cobb-Douglas utility/production maximization** - Asked in June 2024, Dec 2023, Dec 2024
3. **Nash Equilibrium in Prisoner's Dilemma** - Asked in Dec 2024, June 2024, June 2025
4. **Efficiency wage explanation** - Asked in Dec 2024, Dec 2025, June 2025
5. **Cobweb model stability conditions** - Asked in June 2024, Dec 2025, June 2025
6. **Cournot-Nash equilibrium derivation** - Asked in Dec 2023, June 2025
7. **First and Second Welfare Theorems** - Asked in Dec 2024, Dec 2025
8. **Price discrimination (3rd degree)** - Asked in Dec 2024, Dec 2023
9. **Risk aversion with VNM utility** - Asked in Dec 2025, June 2025
10. **Perfect competition long-run equilibrium** - Asked in Dec 2024, June 2024

---

# Part 2: Detailed Notes by Topic

## 1. CONSUMER THEORY & DUALITY

### 1.1 Indirect Utility Function

**Definition:** The indirect utility function $v(p, m)$ gives the maximum utility a consumer can achieve given prices $p$ and income $m$.

$$v(p, m) = \max_{x} \{u(x) : p \cdot x \leq m\}$$

**Properties:**
1. Non-increasing in $p$ (higher prices reduce utility)
2. Non-decreasing in $m$ (more income increases utility)
3. Homogeneous of degree zero in $(p, m)$
4. Quasi-convex in $p$
5. Roy's identity: $x_i(p, m) = -\frac{\partial v/\partial p_i}{\partial v/\partial m}$

### 1.2 Expenditure Function

**Definition:** The expenditure function $e(p, u)$ gives the minimum expenditure needed to achieve utility level $u$ at prices $p$.

$$e(p, u) = \min_{x} \{p \cdot x : u(x) \geq u\}$$

**Properties:**
1. Non-decreasing in $p$
2. Homogeneous of degree 1 in $p$
3. Concave in $p$
4. Continuous in $p$ and $u$
5. Shephard's Lemma: $\frac{\partial e(p, u)}{\partial p_i} = h_i(p, u)$ (Hicksian demand)

### 1.3 Duality Relations

```
┌─────────────────┐                    ┌─────────────────┐
│  Utility        │  ◄─── Dual ───►    │  Expenditure    │
│  Maximization   │                    │  Minimization   │
└────────┬────────┘                    └────────┬────────┘
         │                                        │
         ▼                                        ▼
┌─────────────────┐                    ┌─────────────────┐
│  Marshallian    │    ◄─── Identity ─►│  Hicksian       │
│  Demand         │                    │  Demand         │
│  x(p, m)        │                    │  h(p, u)        │
└─────────────────┘                    └─────────────────┘
```

**Key Identities:**
- $h(p, u) = x(p, e(p, u))$ (Hicksian = Marshallian at expenditure-minimizing income)
- $e(p, v(p, m)) = m$ (Expenditure to achieve max utility = income)
- $v(p, e(p, u)) = u$ (Utility from min expenditure = target utility)

### 1.4 Slutsky Equation

**The Fundamental Equation:**
$$\frac{\partial x_i}{\partial p_j} = \frac{\partial h_i}{\partial p_j} - x_j \frac{\partial x_i}{\partial m}$$

**For Own Price Effect ($i = j$):**
$$\frac{\partial x_i}{\partial p_i} = \underbrace{\frac{\partial h_i}{\partial p_i}}_{\text{Substitution Effect (-)}} - \underbrace{x_i \frac{\partial x_i}{\partial m}}_{\text{Income Effect}}$$

**Slutsky Equation in Elasticity Form:**
$$e_{ii} = e_{ii}^* - s_i e_{im}$$

Where:
- $e_{ii}$ = Own price elasticity of Marshallian demand
- $e_{ii}^*$ = Own price elasticity of Hicksian demand (always negative)
- $s_i$ = Budget share of good $i$
- $e_{im}$ = Income elasticity

---

## 📝 Practice Question 1: Cobb-Douglas Utility Maximization

**Question:** A consumer has utility function $U = x^{3/4}y^{1/4}$. Prices are $P_x = 6$, $P_y = 3$, and income $I = 120$. Find optimal quantities using Lagrangian method.

### Solution:

**Step 1:** Set up Lagrangian
$$\mathcal{L} = x^{3/4}y^{1/4} + \lambda(120 - 6x - 3y)$$

**Step 2:** First-order conditions

$$\frac{\partial \mathcal{L}}{\partial x} = \frac{3}{4}x^{-1/4}y^{1/4} - 6\lambda = 0 \quad \Rightarrow \quad \frac{3}{4}\left(\frac{y}{x}\right)^{1/4} = 6\lambda \quad ...(1)$$

$$\frac{\partial \mathcal{L}}{\partial y} = \frac{1}{4}x^{3/4}y^{-3/4} - 3\lambda = 0 \quad \Rightarrow \quad \frac{1}{4}\left(\frac{x}{y}\right)^{3/4} = 3\lambda \quad ...(2)$$

$$\frac{\partial \mathcal{L}}{\partial \lambda} = 120 - 6x - 3y = 0 \quad ...(3)$$

**Step 3:** Divide (1) by (2)

$$\frac{\frac{3}{4}(y/x)^{1/4}}{\frac{1}{4}(x/y)^{3/4}} = \frac{6\lambda}{3\lambda} = 2$$

$$3 \cdot \frac{(y/x)^{1/4}}{(x/y)^{3/4}} = 3 \cdot \frac{y^{1/4}}{x^{1/4}} \cdot \frac{y^{3/4}}{x^{3/4}} = 3 \cdot \frac{y}{x} = 2$$

$$\frac{y}{x} = \frac{2}{3} \quad \Rightarrow \quad y = \frac{2}{3}x$$

**Step 4:** Substitute into budget constraint

$$6x + 3\left(\frac{2}{3}x\right) = 120$$
$$6x + 2x = 120$$
$$8x = 120 \quad \Rightarrow \quad x^* = 15$$

$$y^* = \frac{2}{3} \times 15 = 10$$

**Answer:** $x^* = 15$ units, $y^* = 10$ units

---

## 📝 Practice Question 2: Slutsky Equation

**Question:** For a consumer with utility $U = x_1x_2$ and $m = 100$, $p_1 = 2$, $p_2 = 5$. Calculate the total effect, substitution effect, and income effect when $p_1$ falls to 1.

### Solution:

**Step 1:** Find initial optimal bundle

MRS = $\frac{MU_1}{MU_2} = \frac{x_2}{x_1} = \frac{p_1}{p_2} = \frac{2}{5} \quad \Rightarrow \quad 5x_2 = 2x_1 \quad \Rightarrow \quad x_2 = \frac{2}{5}x_1$

Budget: $2x_1 + 5(\frac{2}{5}x_1) = 2x_1 + 2x_1 = 4x_1 = 100 \quad \Rightarrow \quad x_1^0 = 25$, $x_2^0 = 10$

Initial utility: $U^0 = 25 \times 10 = 250$

**Step 2:** Find new optimal bundle after price change ($p_1' = 1$)

MRS = $\frac{x_2}{x_1} = \frac{1}{5} \quad \Rightarrow \quad 5x_2 = x_1$

Budget: $1x_1 + 5x_2 = x_1 + 5x_2 = 100$

Substitute $x_1 = 5x_2$: $5x_2 + 5x_2 = 10x_2 = 100 \quad \Rightarrow \quad x_2^1 = 10$, $x_1^1 = 50$

**Total Effect:** $\Delta x_1 = 50 - 25 = 25$

**Step 3:** Find substitution effect (Hicksian)

Need income to keep utility at 250 at new prices:

$U = x_1x_2 = 250$, with MRS $= \frac{x_2}{x_1} = \frac{1}{5}$ (tangency condition)

From MRS: $x_1 = 5x_2$

Substitute: $(5x_2)(x_2) = 5x_2^2 = 250 \quad \Rightarrow \quad x_2^2 = 50 \quad \Rightarrow \quad x_2 = \sqrt{50} \approx 7.07$, $x_1 = 5\sqrt{50} \approx 35.35$

**Substitution Effect:** $35.35 - 25 = 10.35$

**Step 4:** Income effect = Total effect - Substitution effect

**Income Effect:** $50 - 35.35 = 14.65$

| Effect | Value |
|--------|-------|
| Total Effect | +25 |
| Substitution Effect | +10.35 |
| Income Effect | +14.65 |

---

## 2. PRODUCTION THEORY

### 2.1 Cobb-Douglas Production Function

$$Q = A L^{\alpha} K^{\beta}$$

**Properties:**

| Condition | Returns to Scale |
|-----------|------------------|
| $\alpha + \beta = 1$ | Constant Returns to Scale |
| $\alpha + \beta > 1$ | Increasing Returns to Scale |
| $\alpha + \beta < 1$ | Decreasing Returns to Scale |

**Marginal Products:**
- $MP_L = \alpha A L^{\alpha-1} K^{\beta}$
- $MP_K = \beta A L^{\alpha} K^{\beta-1}$

**Diminishing Returns:** $MP_L$ decreases as $L$ increases when $\alpha < 1$

### 2.2 Returns to Scale vs Diminishing Returns

> **Key Distinction:**
> - **Returns to Scale:** All inputs vary proportionally (long-run concept)
> - **Diminishing Returns:** One input varies, others fixed (short-run concept)

**Proof that CRS implies diminishing returns:**

For $Q = f(L, \bar{K})$ with CRS: $f(tL, t\bar{K}) = t f(L, \bar{K})$

Differentiate with respect to $t$: $f_L(tL, t\bar{K}) \cdot L + f_K(tL, t\bar{K}) \cdot \bar{K} = f(L, \bar{K})$

Set $t=1$: $f_L \cdot L + f_K \cdot \bar{K} = f$

Differentiate with respect to $L$: $f_{LL} \cdot L + f_L + f_{KL} \cdot \bar{K} = f_L$

Thus: $f_{LL} \cdot L + f_{KL} \cdot \bar{K} = 0$

Since $f_{KL} > 0$ typically, we get $f_{LL} < 0$ (diminishing returns)

---

## 📝 Practice Question 3: Production Function Analysis

**Question:** A firm has production function $Q = 5\sqrt{LK}$. 
(a) Find maximum output when $L=9$, $K=9$
(b) Find $MP_L$ at this point
(c) Determine returns to scale

### Solution:

**(a) Output at L=9, K=9**

$$Q = 5\sqrt{9 \times 9} = 5\sqrt{81} = 5 \times 9 = 45 \text{ units}$$

**(b) Marginal Product of Labour**

$$MP_L = \frac{\partial Q}{\partial L} = 5 \times \frac{1}{2}(LK)^{-1/2} \times K = \frac{5K}{2\sqrt{LK}}$$

At L=9, K=9: $MP_L = \frac{5 \times 9}{2\sqrt{81}} = \frac{45}{2 \times 9} = \frac{45}{18} = 2.5$

**(c) Returns to Scale**

Double inputs: $L' = 2L$, $K' = 2K$

$$Q' = 5\sqrt{(2L)(2K)} = 5\sqrt{4LK} = 5 \times 2\sqrt{LK} = 2 \times (5\sqrt{LK}) = 2Q$$

Since output doubles when inputs double → **Constant Returns to Scale**

---

## 3. MARKET STRUCTURES

### 3.1 Perfect Competition

**Long-Run Equilibrium Conditions:**
1. $P = MR = MC$ (Profit maximization)
2. $P = AC$ (Zero economic profit)
3. $MC = AC$ at minimum of AC curve

**Firm vs Industry:**
- **Firm:** Horizontal demand curve (price taker)
- **Industry:** Downward-sloping demand curve

### 3.2 Monopoly

**Profit Maximization:** $MR = MC$

**MR Formula:** $MR = P\left(1 - \frac{1}{|e_p|}\right)$

**Lerner Index:** $L = \frac{P - MC}{P} = \frac{1}{|e_p|}$

### 3.3 Price Discrimination

**3rd Degree Price Discrimination:**

For two markets with demands $P_1(Q_1)$ and $P_2(Q_2)$:

**Optimal condition:** $MR_1 = MR_2 = MC$

**Price ratio:** $\frac{P_1}{P_2} = \frac{1 - 1/|e_2|}{1 - 1/|e_1|}$

**Key insight:** Higher price in market with lower elasticity

---

## 📝 Practice Question 4: Price Discrimination

**Question:** A monopolist sells in two markets:
$$P_1 = 12 - Q_1,\quad P_2 = 20 - Q_2$$
$$TC = 3 + 2Q \text{ where } Q = Q_1 + Q_2$$
Find profit-maximizing prices and quantities in each market.

### Solution:

**Step 1:** Find revenue functions

$R_1 = P_1Q_1 = (12 - Q_1)Q_1 = 12Q_1 - Q_1^2$
$R_2 = P_2Q_2 = (20 - Q_2)Q_2 = 20Q_2 - Q_2^2$

**Step 2:** Marginal revenues

$MR_1 = 12 - 2Q_1$
$MR_2 = 20 - 2Q_2$

**Step 3:** Marginal cost

$MC = \frac{dTC}{dQ} = 2$

**Step 4:** Set $MR_1 = MR_2 = MC$

$12 - 2Q_1 = 2 \quad \Rightarrow \quad 2Q_1 = 10 \quad \Rightarrow \quad Q_1 = 5$

$20 - 2Q_2 = 2 \quad \Rightarrow \quad 2Q_2 = 18 \quad \Rightarrow \quad Q_2 = 9$

**Step 5:** Find prices

$P_1 = 12 - 5 = 7$
$P_2 = 20 - 9 = 11$

**Step 6:** Calculate profit

$Q = 5 + 9 = 14$
$TR = (7 \times 5) + (11 \times 9) = 35 + 99 = 134$
$TC = 3 + 2(14) = 3 + 28 = 31$
**Profit = 134 - 31 = 103**

| Market | Quantity | Price |
|--------|----------|-------|
| Market 1 | 5 | 7 |
| Market 2 | 9 | 11 |

---

## 4. OLIGOPOLY

### 4.1 Cournot Duopoly

**Setup:** Two firms, homogeneous product, choose quantities simultaneously

**Demand:** $P = a - Q$ where $Q = q_1 + q_2$

**Costs:** $C_i(q_i) = c q_i$ (constant MC)

**Firm 1's profit:** $\pi_1 = [a - (q_1 + q_2)]q_1 - c q_1$

**FOC:** $\frac{\partial \pi_1}{\partial q_1} = a - 2q_1 - q_2 - c = 0$

**Reaction function:** $q_1 = \frac{a - c - q_2}{2}$

By symmetry: $q_1^* = q_2^* = \frac{a - c}{3}$

**Equilibrium:** $Q^* = \frac{2(a-c)}{3}$, $P^* = \frac{a + 2c}{3}$

### 4.2 Bertrand Duopoly

**Setup:** Firms choose prices simultaneously

**Key insight:** With homogeneous products and constant MC, equilibrium occurs at $P = MC$ (like perfect competition)

**Bertrand Paradox:** Two firms are enough to achieve competitive outcome

### 4.3 Stackelberg Duopoly

**Setup:** Leader moves first, follower moves second

**Follower's reaction:** $q_2 = \frac{a - c - q_1}{2}$

**Leader maximizes:** $\pi_1 = [a - (q_1 + q_2)]q_1 - c q_1$

Substitute $q_2$: $\pi_1 = \left[a - q_1 - \frac{a - c - q_1}{2}\right]q_1 - c q_1$

Simplify: $\pi_1 = \left[\frac{a - c - q_1}{2}\right]q_1$

**FOC:** $\frac{a - c - 2q_1}{2} = 0 \quad \Rightarrow \quad q_1 = \frac{a - c}{2}$

Then: $q_2 = \frac{a - c - (a-c)/2}{2} = \frac{a - c}{4}$

**Result:** First-mover advantage ($q_1 > q_2$)

---

## 📝 Practice Question 5: Cournot Equilibrium

**Question:** Two firms face demand $P = 130 - Q$ with $MC = 10$. Find Cournot-Nash equilibrium.

### Solution:

**Step 1:** Firm 1's profit

$\pi_1 = (130 - q_1 - q_2)q_1 - 10q_1 = 130q_1 - q_1^2 - q_1q_2 - 10q_1 = 120q_1 - q_1^2 - q_1q_2$

**Step 2:** First-order condition

$\frac{\partial \pi_1}{\partial q_1} = 120 - 2q_1 - q_2 = 0$

**Step 3:** Reaction function for Firm 1

$q_1 = \frac{120 - q_2}{2}$ ...(1)

**Step 4:** By symmetry, Firm 2's reaction function

$q_2 = \frac{120 - q_1}{2}$ ...(2)

**Step 5:** Solve simultaneously

Substitute (2) into (1):

$q_1 = \frac{120 - \frac{120 - q_1}{2}}{2} = \frac{120 - 60 + \frac{q_1}{2}}{2} = \frac{60 + \frac{q_1}{2}}{2}$

$q_1 = 30 + \frac{q_1}{4} \quad \Rightarrow \quad \frac{3q_1}{4} = 30 \quad \Rightarrow \quad q_1 = 40$

By symmetry: $q_2 = 40$

**Step 6:** Industry output and price

$Q = 40 + 40 = 80$

$P = 130 - 80 = 50$

| Variable | Value |
|----------|-------|
| $q_1$ | 40 |
| $q_2$ | 40 |
| $Q$ | 80 |
| $P$ | 50 |

**Check:** Each firm's profit = $(50 - 10) \times 40 = 40 \times 40 = 1600$

---

## 5. GAME THEORY

### 5.1 Nash Equilibrium

**Definition:** A strategy profile $(s_1^*, s_2^*, ..., s_n^*)$ is a Nash equilibrium if for each player $i$:

$$u_i(s_i^*, s_{-i}^*) \geq u_i(s_i, s_{-i}^*) \quad \forall s_i \in S_i$$

No player can unilaterally deviate and improve their payoff.

### 5.2 Prisoner's Dilemma

| | Confess | Don't Confess |
|--|---------|---------------|
| **Confess** | (-5, -5) | (0, -10) |
| **Don't Confess** | (-10, 0) | (-1, -1) |

**Key insights:**
- Unique Nash equilibrium: (Confess, Confess)
- Pareto inferior to (Don't Confess, Don't Confess)
- Demonstrates conflict between individual and collective rationality

### 5.3 Mixed Strategy Nash Equilibrium

**Finding mixed strategy:** Make opponent indifferent between pure strategies

**Example:** For a 2×2 game with payoffs:

| | L | R |
|--|---|---|
| **U** | a, b | c, d |
| **D** | e, f | g, h |

**Player 1's mixed strategy:** Play U with probability $p$, D with $1-p$

**Player 2's indifference condition:**

$$b \cdot p + f \cdot (1-p) = d \cdot p + h \cdot (1-p)$$

Solve for $p$

---

## 📝 Practice Question 6: Nash Equilibrium

**Question:** Find Nash equilibrium in pure and mixed strategies for:

Player 2

| Player 1 | M | I |
|----------|---|---|
| **W** | (1, 1) | (1, 2) |
| **S** | (0, 2) | (2, 1) |

### Solution:

**(a) Pure Strategy Nash Equilibrium**

Check each cell:

- (W, M): Can Player 1 deviate? 1 → 0 (No). Player 2: 1 → 2 (YES, to I) → Not NE
- (W, I): Player 1: 1 → 2 (YES, to S) → Not NE
- (S, M): Player 1: 0 → 1 (YES, to W) → Not NE
- (S, I): Player 1: 2 → 1 (No). Player 2: 1 → 2 (YES, to M) → Not NE

**No pure strategy Nash equilibrium exists.**

**(b) Mixed Strategy Nash Equilibrium**

Let Player 1 play W with probability $p$, S with $1-p$
Let Player 2 play M with probability $q$, I with $1-q$

**Player 2's expected payoffs:**

$E_2(M) = 1 \cdot p + 2 \cdot (1-p) = p + 2 - 2p = 2 - p$
$E_2(I) = 2 \cdot p + 1 \cdot (1-p) = 2p + 1 - p = 1 + p$

Set equal: $2 - p = 1 + p \quad \Rightarrow \quad 1 = 2p \quad \Rightarrow \quad p = 0.5$

**Player 1's expected payoffs:**

$E_1(W) = 1 \cdot q + 1 \cdot (1-q) = 1$
$E_1(S) = 0 \cdot q + 2 \cdot (1-q) = 2 - 2q$

Set equal: $1 = 2 - 2q \quad \Rightarrow \quad 2q = 1 \quad \Rightarrow \quad q = 0.5$

**Mixed Strategy NE:** Player 1: (0.5 W, 0.5 S), Player 2: (0.5 M, 0.5 I)

---

## 6. WELFARE ECONOMICS

### 6.1 First Welfare Theorem

**Statement:** Every competitive equilibrium is Pareto efficient (under perfect competition, no externalities, perfect information).

**Implication:** Markets allocate resources efficiently.

**Limitation:** Does NOT guarantee fairness or equity.

### 6.2 Second Welfare Theorem

**Statement:** Any Pareto efficient allocation can be achieved as a competitive equilibrium with appropriate initial endowments (lump-sum transfers).

**Implication:** Efficiency and distribution can be separated.

### 6.3 Social Welfare Function

**General form:** $W = F(U_1, U_2, ..., U_n)$

**Types:**

| Type | Formula | Characteristics |
|------|---------|-----------------|
| Utilitarian (Bentham) | $W = \sum U_i$ | Maximizes sum of utilities |
| Rawlsian | $W = \min(U_1, ..., U_n)$ | Maximizes welfare of worst-off |
| Bergson-Samuelson | $W = F(U_1, ..., U_n)$ | General form with value judgments |

### 6.4 Compensation Principle (Kaldor-Hicks)

**Kaldor Criterion:** Change is desirable if gainers can potentially compensate losers (even if compensation not actually paid)

**Hicks Criterion:** Change is desirable if losers cannot profitably bribe gainers to forgo the change

**Difference:** Kaldor uses current prices, Hicks uses new prices (both face index number problem)

---

## 📝 Practice Question 7: Welfare Theorems

**Question:** Does the First Welfare Theorem guarantee fair or equitable market allocation? Explain.

### Solution:

**Answer:** NO, the First Welfare Theorem does NOT guarantee fairness or equity.

**Explanation:**

1. **What FWT guarantees:** 
   - Competitive equilibrium is Pareto efficient
   - No reallocation can make someone better off without making someone else worse off

2. **What FWT does NOT guarantee:**
   - **Equity:** The distribution of resources can be highly unequal
   - **Fairness:** Starting endowments determine final allocation

3. **Example:**
   - Initial endowments: Person A has everything, Person B has nothing
   - Competitive equilibrium: A consumes everything (efficient but not equitable)
   - Any redistribution would require departing from competitive equilibrium

4. **Role of Second Welfare Theorem:**
   - Any Pareto efficient allocation can be achieved with appropriate redistribution
   - Separates efficiency (market) from equity (government intervention)

**Conclusion:** Markets ensure efficiency, but equity requires redistribution through policy.

---

## 7. ECONOMICS OF UNCERTAINTY

### 7.1 Expected Utility Theory (VNM)

**Von Neumann-Morgenstern Utility:** $U(L) = \sum_{i=1}^n p_i u(w_i)$

Where $u(w)$ is a concave function for risk-averse individuals.

### 7.2 Risk Attitudes

| Attitude | Condition | Shape of u(w) | Example |
|----------|-----------|---------------|---------|
| Risk Averse | $E[u(w)] < u(E[w])$ | Concave | $u(w) = \sqrt{w}$ |
| Risk Neutral | $E[u(w)] = u(E[w])$ | Linear | $u(w) = w$ |
| Risk Loving | $E[u(w)] > u(E[w])$ | Convex | $u(w) = w^2$ |

### 7.3 Certainty Equivalent and Risk Premium

**Certainty Equivalent (CE):** $u(CE) = E[u(w)]$

**Risk Premium:** $RP = E[w] - CE$

### 7.4 Efficiency Wage

**Definition:** Wage above market-clearing level paid to increase productivity

**Why profitable when workers have better information:**

1. **Shirking model:** Higher wage increases cost of job loss → reduces shirking
2. **Adverse selection:** Higher wage attracts more productive workers
3. **Turnover costs:** Higher wage reduces costly turnover
4. **Morale/effort:** Workers exert more effort when paid above-market wages

**No-Shirking Condition (NSC):**
$$w \geq \bar{w} + \frac{e}{q}$$

Where:
- $\bar{w}$ = alternative wage
- $e$ = effort level
- $q$ = probability of detection

---

## 📝 Practice Question 8: Risk Aversion

**Question:** You have $u(w) = \sqrt{w}$, initial wealth = ₹100. Offered gamble: 50% chance of ₹156, 50% chance of -₹100 (lose ₹100). Should you accept?

### Solution:

**Step 1:** Calculate expected utility of gamble

Final wealth in each outcome:
- Win: $100 + 156 = 256$
- Lose: $100 - 100 = 0$

$E[u(w)] = 0.5 \times \sqrt{256} + 0.5 \times \sqrt{0} = 0.5 \times 16 + 0.5 \times 0 = 8$

**Step 2:** Compare with current utility

Current utility: $u(100) = \sqrt{100} = 10$

**Step 3:** Decision rule

Since $E[u(w)] = 8 < 10$ (current utility)

**Answer:** Do NOT accept the gamble. The expected utility is lower than certain utility.

**Step 4:** Find Certainty Equivalent

$\sqrt{CE} = 8 \quad \Rightarrow \quad CE = 64$

**Risk premium** = $E[w] - CE = (0.5 \times 256 + 0.5 \times 0) - 64 = 128 - 64 = 64$

You would pay up to ₹64 to avoid the gamble.

---

## 8. COBWEB MODEL (Dynamic Stability)

### 8.1 Model Setup

**Demand:** $Q_t^d = a - bP_t$ (period t price determines demand)

**Supply:** $Q_t^s = c + dP_{t-1}$ (previous period price determines supply)

**Equilibrium condition:** $Q_t^d = Q_t^s$

### 8.2 Difference Equation

$$a - bP_t = c + dP_{t-1}$$

$$P_t = \frac{a-c}{b} - \frac{d}{b}P_{t-1}$$

### 8.3 Stability Condition

**Stable equilibrium if:** $\left|\frac{d}{b}\right| < 1$ (Supply curve flatter than demand curve)

| Condition | Result |
|-----------|--------|
| $\left|\frac{d}{b}\right| < 1$ | Convergent (stable) |
| $\left|\frac{d}{b}\right| > 1$ | Divergent (unstable) |
| $\left|\frac{d}{b}\right| = 1$ | Constant amplitude oscillation |

### 8.4 Time Path Solution

$$P_t = P^* + (P_0 - P^*)\left(-\frac{d}{b}\right)^t$$

Where $P^* = \frac{a-c}{b+d}$ is the equilibrium price

---

## 📝 Practice Question 9: Cobweb Model

**Question:** In a cobweb model, demand is $Q_t^d = 20 - 2P_t$, supply is $Q_t^s = 4 + 3P_{t-1}$. Determine stability and find time path.

### Solution:

**Step 1:** Find equilibrium price

Set $Q_t^d = Q_t^s$: $20 - 2P_t = 4 + 3P_{t-1}$

At equilibrium: $P_t = P_{t-1} = P^*$

$20 - 2P^* = 4 + 3P^* \quad \Rightarrow \quad 16 = 5P^* \quad \Rightarrow \quad P^* = 3.2$

**Step 2:** Check stability

Demand slope: $b = 2$
Supply slope: $d = 3$

$\left|\frac{d}{b}\right| = \left|\frac{3}{2}\right| = 1.5 > 1$ → **Unstable (divergent)**

**Step 3:** Derive difference equation

$20 - 2P_t = 4 + 3P_{t-1} \quad \Rightarrow \quad 2P_t = 16 - 3P_{t-1} \quad \Rightarrow \quad P_t = 8 - 1.5P_{t-1}$

**Step 4:** Time path

$P_t = 3.2 + (P_0 - 3.2)(-1.5)^t$

If $P_0 = 4$, then:
$P_1 = 8 - 1.5(4) = 8 - 6 = 2$
$P_2 = 8 - 1.5(2) = 8 - 3 = 5$
$P_3 = 8 - 1.5(5) = 8 - 7.5 = 0.5$

Prices oscillate with increasing amplitude.

---

# Part 3: Conceptual Distinctions (Important for Exams)

## Table 1: Key Distinctions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| **Partial Equilibrium** | **General Equilibrium** | Single market vs all markets simultaneously |
| **Signalling** | **Screening** | Informed party moves first vs uninformed party moves first |
| **Cooperative Game** | **Non-cooperative Game** | Binding agreements possible vs not possible |
| **Pooling Equilibrium** | **Separating Equilibrium** | All types same action vs different actions by type |
| **Homogeneous Function** | **Homothetic Function** | $f(tx)=t^k f(x)$ vs $f$ is monotonic transform of homogeneous |
| **Adverse Selection** | **Moral Hazard** | Hidden information before contract vs hidden action after contract |
| **Compensated Demand** | **Ordinary Demand** | Utility constant (Hicksian) vs income constant (Marshallian) |
| **First Degree PD** | **Third Degree PD** | Perfect price discrimination vs group-based discrimination |

---

# Part 4: Formula Sheet for Quick Revision

## Consumer Theory

| Formula | Name |
|---------|------|
| $MRS = \frac{MU_x}{MU_y} = \frac{P_x}{P_y}$ | Utility maximization |
| $x_i(p,m) = -\frac{\partial v/\partial p_i}{\partial v/\partial m}$ | Roy's Identity |
| $\frac{\partial e(p,u)}{\partial p_i} = h_i(p,u)$ | Shephard's Lemma |
| $\frac{\partial x_i}{\partial p_j} = \frac{\partial h_i}{\partial p_j} - x_j \frac{\partial x_i}{\partial m}$ | Slutsky Equation |

## Production Theory

| Formula | Name |
|---------|------|
| $MRTS = \frac{MP_L}{MP_K} = \frac{w}{r}$ | Cost minimization |
| $\sigma = \frac{d(K/L)}{K/L} / \frac{d(MRTS)}{MRTS}$ | Elasticity of substitution |
| $\epsilon_Q = \alpha + \beta$ (for Cobb-Douglas) | Returns to scale parameter |

## Market Structures

| Formula | Application |
|---------|-------------|
| $MR = P(1 - 1/|e|)$ | Monopoly pricing |
| $q_i = (a-c)/3$ (each firm) | Cournot duopoly (symmetric) |
| $P = MC$ | Bertrand equilibrium |
| $q_L = (a-c)/2$, $q_F = (a-c)/4$ | Stackelberg (leader-follower) |

## Welfare

| Formula | Name |
|---------|------|
| $CS = \int_{P^*}^{P_{max}} Q(P) dP$ | Consumer surplus |
| $EV = e(p^0, u^1) - e(p^0, u^0)$ | Equivalent variation |
| $CV = e(p^1, u^0) - e(p^0, u^0)$ | Compensating variation |

## Uncertainty

| Formula | Name |
|---------|------|
| $E[u(w)] = \sum p_i u(w_i)$ | Expected utility |
| $RP = E[w] - CE$ | Risk premium |
| $ARA = -u''(w)/u'(w)$ | Absolute risk aversion |

---

# Part 5: Practice Problem Set

## Problem 1: Utility Maximization (Cobb-Douglas)

**Q:** Consumer has $U = x^{0.6}y^{0.4}$, $I=500$, $P_x=25$, $P_y=20$. Find optimal bundle and indirect utility.

<details>
<summary><b>Solution</b></summary>

Using property: For $U = x^\alpha y^{1-\alpha}$, expenditure shares are constant.

$x^* = \alpha \cdot \frac{I}{P_x} = 0.6 \times \frac{500}{25} = 0.6 \times 20 = 12$

$y^* = (1-\alpha) \cdot \frac{I}{P_y} = 0.4 \times \frac{500}{20} = 0.4 \times 25 = 10$

$U^* = 12^{0.6} \times 10^{0.4} \approx (12^{0.6} \approx 4.43) \times (10^{0.4} \approx 2.51) \approx 11.12$

$v(p,m) = I \cdot \alpha^\alpha (1-\alpha)^{1-\alpha} / P_x^\alpha P_y^{1-\alpha}$
</details>

---

## Problem 2: Cost Minimization

**Q:** Production function $Q = L^{0.7}K^{0.3}$, $w=1$, $r=2$, target $Q=100$. Find cost-minimizing L and K.

<details>
<summary><b>Solution</b></summary>

Cost minimization condition: $MP_L/MP_K = w/r$

$MP_L = 0.7 L^{-0.3} K^{0.3}$
$MP_K = 0.3 L^{0.7} K^{-0.7}$

$\frac{0.7 L^{-0.3} K^{0.3}}{0.3 L^{0.7} K^{-0.7}} = \frac{0.7}{0.3} \cdot \frac{K}{L} = \frac{1}{2}$

$\frac{7}{3} \cdot \frac{K}{L} = \frac{1}{2} \quad \Rightarrow \quad 14K = 3L \quad \Rightarrow \quad K = \frac{3}{14}L$

Plug into $L^{0.7}(\frac{3}{14}L)^{0.3} = 100$:

$(\frac{3}{14})^{0.3} \cdot L = 100 \quad \Rightarrow \quad L = 100 \times (\frac{14}{3})^{0.3} \approx 100 \times 1.7 \approx 170$

$K = (3/14) \times 170 \approx 36.4$

Minimum cost = $1(170) + 2(36.4) = 170 + 72.8 = 242.8$
</details>

---

## Problem 3: Slutsky Decomposition for Inferior Good

**Q:** For a good with $x(p,m) = 100 - 5p + 0.1m$ at $p=10$, $m=1000$, find SE and IE when price falls to 8.

<details>
<summary><b>Solution</b></summary>

Initial: $x(10,1000) = 100 - 50 + 100 = 150$

New: $x(8,1000) = 100 - 40 + 100 = 160$

Total effect = $160 - 150 = 10$

For substitution effect: $h(p,u) = x(p, e(p,u))$

Need $u$ from initial: $u = 150$ (assuming direct utility consistent with this demand)

$e(10, u) = m$ initially

$e(8, u) = ?$ Using expenditure function derived from demand

Alternatively use Slutsky: $SE = \frac{\partial h}{\partial p} \cdot \Delta p$

For inferior good, IE is negative (if $\partial x/\partial m < 0$)

Here $\partial x/\partial m = 0.1 > 0$ (normal good)

$SE = TE - IE = 10 - [-(150 \times 0.1 \times 2)]?$ Wait, need correct formula.

Actually: $IE = -x \cdot \frac{\partial x}{\partial m} \cdot \Delta p = -150 \times 0.1 \times (-2) = 30$

So $SE = TE - IE = 10 - 30 = -20$ (This would be negative but substitution effect should be negative. If SE > TE, good is Giffen. Let me recalc carefully.)

$TE = \Delta x = 10$

$IE = -x \cdot \frac{\partial x}{\partial m} \cdot \Delta p = -150 \times 0.1 \times (-2) = 30$

$SE = TE - IE = 10 - 30 = -20$

This implies SE is -20 and IE is +30, so good is Giffen? But $\partial x/\partial m > 0$ suggests normal. Check: With price decrease, IE should be positive for normal good. So TE = SE + IE => 10 = SE + 30 => SE = -20. Yes, SE is always negative. So good is normal (IE positive) but not Giffen.
</details>

---

# Part 6: Exam Strategy

## Section A (2×20=40 marks) - Choose 2 questions

**Recommended topics to focus:**
1. Slutsky equation with numerical example
2. Cobb-Douglas optimization (production or utility)
3. Game theory (Nash equilibrium, Prisoner's Dilemma)
4. Cobweb model stability analysis

## Section B (5×12=60 marks) - Choose 5 questions

**Recommended topics:**
1. Indirect utility/Expenditure function properties
2. Perfect competition long-run equilibrium
3. Price discrimination calculations
4. Risk and expected utility
5. Efficiency wage explanation
6. Welfare theorems
7. Cournot/Bertrand equilibrium derivation

## Time Management

| Section | Questions | Time Allocation |
|---------|-----------|-----------------|
| Section A | 2 questions | 15 min each (30 min total) |
| Section B | 5 questions | 10-12 min each (50-60 min total) |
| Review | - | 10 min |

---

# Part 7: Quick Revision Checklist

## ☐ Consumer Theory
- [ ] Indirect utility function (properties)
- [ ] Expenditure function (properties, Shephard's Lemma)
- [ ] Slutsky equation (derivation and decomposition)
- [ ] Roy's identity
- [ ] Compensated vs ordinary demand

## ☐ Producer Theory
- [ ] Cobb-Douglas production (RTS, diminishing returns)
- [ ] Cost minimization (Lagrangian)
- [ ] Returns to scale vs diminishing returns
- [ ] Shephard's Lemma for cost functions

## ☐ Market Structures
- [ ] Perfect competition (LR equilibrium)
- [ ] Monopoly (MR = MC, Lerner index)
- [ ] Price discrimination (3rd degree calculations)
- [ ] Cournot duopoly (reaction functions)
- [ ] Bertrand duopoly (price competition)
- [ ] Stackelberg (first-mover advantage)

## ☐ Game Theory
- [ ] Nash equilibrium (pure and mixed)
- [ ] Prisoner's Dilemma
- [ ] Best response functions
- [ ] Dominant strategies

## ☐ Welfare Economics
- [ ] First Welfare Theorem
- [ ] Second Welfare Theorem
- [ ] Social welfare functions (Utilitarian, Rawlsian)
- [ ] Kaldor-Hicks compensation principle

## ☐ Uncertainty
- [ ] Expected utility theory (VNM)
- [ ] Risk aversion (concave utility)
- [ ] Certainty equivalent and risk premium
- [ ] Efficiency wage (NSC)

## ☐ Dynamic Analysis
- [ ] Cobweb model (stability condition)
- [ ] Time path derivation

---

*This guide covers all major topics in MEC-101 syllabus based on analysis of past examination papers from 2023-2025.*