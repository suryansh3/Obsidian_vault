---
course: "Probability & Statistics"
semester: 3
tags:
  - course/probability-and-statistics
up: "[[Probability & Statistics]]"
---
Of course. Here is a detailed explanation of the requested concepts, complete with examples of increasing difficulty.

### 1. Definition of a Random Variable

A **random variable** is not a traditional variable but a function. It is a rule that assigns a numerical value to each outcome of a random experiment.

*   **Formally:** Let S be the sample space of an experiment. A random variable X is a function from the sample space S to the real numbers: `X: S → ℝ`.
*   **In simple terms:** It's a way to translate non-numerical outcomes (like "Heads" or "Tails") or complex numerical outcomes into a single number that we can perform calculations on.

**Types:**
*   **Discrete Random Variable:** Takes on a countable number of distinct values (e.g., number of students in a class, result of a die roll).
*   **Continuous Random Variable:** Takes on an uncountable number of values within an interval (e.g., height of a person, time until a component fails).

---

### 2. Interconversion Between PMF and CDF

For **discrete random variables**, we use the Probability Mass Function (PMF) and the Cumulative Distribution Function (CDF). Their relationship is fundamental.

*   **Probability Mass Function (PMF):** Denoted as `pₓ(x)` or `P(X=x)`. It gives the probability that a discrete random variable is *exactly equal* to some value.
*   **Cumulative Distribution Function (CDF):** Denoted as `Fₓ(x)` or `P(X ≤ x)`. It gives the probability that the random variable is *less than or equal to* some value.

**Interconversion Rules:**

1.  **From PMF to CDF (Summation):**
    The CDF is found by summing the PMF for all values less than or equal to `x`.
    `Fₓ(x) = P(X ≤ x) = Σ_{k ≤ x} P(X = k)`

2.  **From CDF to PMF (Difference):**
    The PMF is found by looking at the difference (or "jump") in the CDF at the point `x`. For any value `x` where the CDF changes,
    `P(X = x) = Fₓ(x) - Fₓ(x⁻)`
    where `Fₓ(x⁻)` is the limit of the CDF as it approaches `x` from the left. For simple discrete variables, this is simply the previous CDF value:
    `P(X = x) = Fₓ(x) - Fₓ(x - 1)` (if the values are consecutive integers).

---

### 3. Examples from Lowest to Highest Difficulty

Here are 10 examples demonstrating this interconversion.

#### **Example 1: The Coin Toss (Very Easy)**
A fair coin is tossed once. Let X be the random variable: X=0 for Heads, X=1 for Tails.

**a) Find the PMF.**
P(X=0) = 0.5, P(X=1) = 0.5

**b) Convert the PMF to a CDF.**
*   Fₓ(-1) = P(X ≤ -1) = 0
*   Fₓ(0) = P(X ≤ 0) = P(X=0) = 0.5
*   Fₓ(1) = P(X ≤ 1) = P(X=0) + P(X=1) = 0.5 + 0.5 = 1
*   Fₓ(2) = P(X ≤ 2) = 1

**c) Retrieve the PMF from the CDF.**
*   P(X=0) = Fₓ(0) - Fₓ(-1) = 0.5 - 0 = 0.5
*   P(X=1) = Fₓ(1) - Fₓ(0) = 1 - 0.5 = 0.5

---

#### **Example 2: A Single Die Roll (Easy)**
A fair die is rolled once. Let X be the number on the face.

**a) Find the PMF.**
P(X=x) = 1/6 for x = 1, 2, 3, 4, 5, 6.

**b) Find the CDF, Fₓ(3.5).**
Fₓ(3.5) = P(X ≤ 3.5) = P(X=1, 2, or 3) = 3/6 = 0.5

**c) Retrieve P(X=4) from the CDF.**
P(X=4) = Fₓ(4) - Fₓ(3) = (4/6) - (3/6) = 1/6

---

#### **Example 3: Two Coin Tosses (Basic)**
Two fair coins are tossed. Let X be the number of heads.

**a) Find the PMF.**
P(X=0) = P(TT) = 1/4
P(X=1) = P(HT, TH) = 1/2
P(X=2) = P(HH) = 1/4

**b) Convert the PMF to a CDF.**
*   Fₓ(0) = P(X ≤ 0) = 1/4
*   Fₓ(1) = P(X ≤ 1) = 1/4 + 1/2 = 3/4
*   Fₓ(2) = P(X ≤ 2) = 1

**c) Retrieve P(X=1) from the CDF.**
P(X=1) = Fₓ(1) - Fₓ(0) = 3/4 - 1/4 = 1/2

---

#### **Example 4: A Simple Non-Uniform Distribution (Intermediate)**
The PMF of a random variable Y is given by: P(Y=y) = k*y for y = 1, 2, 3.

**a) Find the constant k.**
The probabilities must sum to 1: k(1) + k(2) + k(3) = 6k = 1 => **k = 1/6**
So the PMF is: P(Y=1)=1/6, P(Y=2)=2/6, P(Y=3)=3/6.

**b) Find the CDF.**
*   Fᵧ(1) = 1/6
*   Fᵧ(2) = 1/6 + 2/6 = 3/6
*   Fᵧ(3) = 1/6 + 2/6 + 3/6 = 1

**c) Find P(Y > 1) using the CDF.**
P(Y > 1) = 1 - P(Y ≤ 1) = 1 - Fᵧ(1) = 1 - 1/6 = 5/6

---

#### **Example 5: CDF Given Directly (Intermediate)**
The CDF of a discrete random variable X is:
Fₓ(x) = { 0 for x < 1,
          0.2 for 1 ≤ x < 3,
          0.7 for 3 ≤ x < 5,
          1 for x ≥ 5 }

**a) What is P(X ≤ 3)?**
P(X ≤ 3) = Fₓ(3) = 0.7

**b) What is P(X < 3)?**
P(X < 3) = Fₓ(3⁻) = 0.2 (the value of the CDF just before the jump at x=3)

**c) Find the PMF of X.**
The PMF exists only at the "jump" points: x=1, x=3, x=5.
*   P(X=1) = Fₓ(1) - Fₓ(1⁻) = 0.2 - 0 = 0.2
*   P(X=3) = Fₓ(3) - Fₓ(3⁻) = 0.7 - 0.2 = 0.5
*   P(X=5) = Fₓ(5) - Fₓ(5⁻) = 1 - 0.7 = 0.3

---

#### **Example 6: Partially Defined PMF (Advanced)**
A discrete random variable Z has CDF F_z(z). It is known that P(Z=1) = 0.1, P(Z=2) = 0.3, and P(Z=4) = 0.2. F_z(3) = 0.7.

**a) Find P(Z=3).**
We know F_z(3) = P(Z ≤ 3) = P(Z=1) + P(Z=2) + P(Z=3)
0.7 = 0.1 + 0.3 + P(Z=3)
**P(Z=3) = 0.3**

**b) Find the complete CDF.**
*   F_z(1) = P(Z ≤ 1) = 0.1
*   F_z(2) = P(Z ≤ 2) = 0.1 + 0.3 = 0.4
*   F_z(3) = 0.7 (given)
*   F_z(4) = P(Z ≤ 4) = 0.7 + 0.2 = 0.9
*   F_z(5) = 1 (assuming Z's maximum value is 4)

---

#### **Example 7: Word Problem - Defective Items (Applied)**
A batch of 10 items contains 3 defectives. 4 items are chosen at random. Let X be the number of defective items found.

**a) Find the PMF (using combinations).**
This is a hypergeometric distribution.
P(X = k) = [C(3, k) * C(7, 4-k)] / C(10, 4) for k = 0, 1, 2, 3.
*   P(X=0) = [C(3,0)*C(7,4)] / C(10,4) = (1*35)/210 ≈ 0.167
*   P(X=1) = [C(3,1)*C(7,3)] / C(10,4) = (3*35)/210 = 105/210 = 0.5
*   P(X=2) = [C(3,2)*C(7,2)] / C(10,4) = (3*21)/210 = 63/210 = 0.3
*   P(X=3) = [C(3,3)*C(7,1)] / C(10,4) = (1*7)/210 ≈ 0.033

**b) Find the probability that at most 2 are defective using the CDF.**
P(X ≤ 2) = Fₓ(2) = P(X=0) + P(X=1) + P(X=2) = 0.167 + 0.5 + 0.3 = 0.967

---

#### **Example 8: CDF with Non-Integer Values (Advanced)**
The CDF of a discrete variable W is defined as:
F_w(w) = { 0 for w < 0,
          w/4 for 0 ≤ w < 2,
          0.8 for 2 ≤ w < 4,
          1 for w ≥ 4 }

**a) Why is W discrete? Identify its possible values.**
The CDF has flat sections and jumps, indicating a discrete variable. The jumps occur where the definition changes: at w=0, w=2, and w=4. These are the possible values.

**b) Find the PMF.**
Find the "jump" in the CDF at each point.
*   P(W=0) = F_w(0) - F_w(0⁻) = (0/4) - 0 = 0
*   Wait, this is a trick. The CDF is *defined* for a range. The jump happens at the start of the range. Let's evaluate just after the points:
    *   P(W=0) = F_w(0.0001) - F_w(-0.0001) ≈ (0.0001/4) - 0 ≈ 0. This value is not a discrete point; the discrete points are at the jumps at w=2 and w=4.
    *   **P(W=2) = F_w(2) - F_w(2⁻)**. F_w(2) = 0.8. Just before 2, the CDF is w/4, so F_w(2⁻) ≈ 2/4 = 0.5. So P(W=2) = 0.8 - 0.5 = 0.3.
    *   **P(W=4) = F_w(4) - F_w(4⁻)**. F_w(4)=1. F_w(4⁻)=0.8. So P(W=4)=1-0.8=0.2.
What about the probability for 0 ≤ w < 2? It's spread out, meaning W is actually a **mixed random variable** (partly continuous, partly discrete). This is a high-difficulty insight. The PMF only exists for the discrete parts: P(W=2)=0.3, P(W=4)=0.2. The rest (1 - 0.3 - 0.2 = 0.5) is distributed continuously between 0 and 2.

---

#### **Example 9: Using CDF to find Probabilities (High Application)**
The number of customers arriving at a store follows a distribution with CDF Fₓ(x). Given Fₓ(10) = 0.85 and Fₓ(11) = 0.92.

**a) What is the probability that exactly 11 customers arrive?**
P(X=11) = Fₓ(11) - Fₓ(10) = 0.92 - 0.85 = 0.07

**b) What is the probability that more than 10 customers arrive?**
P(X > 10) = 1 - P(X ≤ 10) = 1 - Fₓ(10) = 1 - 0.85 = 0.15

**c) What is P(10 < X ≤ 11)?**
P(10 < X ≤ 11) = Fₓ(11) - Fₓ(10) = 0.92 - 0.85 = 0.07
(This is the same as P(X=11) because X is discrete).

---

#### **Example 10: Multi-Part Problem (Highest Difficulty)**
A random variable X has a CDF defined as follows:
Fₓ(x) = {
    0,                          x < 0
    (1/4)(x + 1)²,      0 ≤ x < 1
    1/2 + (x - 1)/2,    1 ≤ x < 2
    1,                          x ≥ 2
}

**a) Is X discrete, continuous, or mixed? Explain.**
The CDF is piecewise and continuous (check at x=0: (1/4)(0+1)²=1/4 vs. 0, so it's not continuous at x=0). There is a jump at x=0. It is continuous on the intervals (0,1) and (1,2). Therefore, X is a **mixed random variable**.

**b) Find P(X = 0).**
P(X=0) = Fₓ(0) - Fₓ(0⁻) = [(1/4)(0+1)²] - [0] = 1/4 - 0 = **1/4**

**c) Find P(0.5 < X < 1.5).**
P(0.5 < X < 1.5) = Fₓ(1.5⁻) - Fₓ(0.5)
For 1 ≤ x < 2, the CDF is 1/2 + (x-1)/2. So Fₓ(1.5) = 1/2 + (1.5-1)/2 = 1/2 + 1/4 = 3/4.
For 0 ≤ x < 1, the CDF is (1/4)(x+1)². So Fₓ(0.5) = (1/4)(1.5)² = (1/4)(2.25) = 9/16 = 0.5625.
Therefore, P(0.5 < X < 1.5) = Fₓ(1.5) - Fₓ(0.5) = (3/4) - (9/16) = (12/16 - 9/16) = **3/16**

This final example combines understanding of CDF, PMF (for the discrete point), and the ability to work with a mixed distribution.

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Probability & Statistics]] · **Semester:** [[Semester 3]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 3/Probability & Statistics/Distribution Deepseek|Distribution Deepseek]] · **Next:** [[04 - Academics & CS/Semester 3/Probability & Statistics/Statistics|Statistics]]
> **Related:** [[IPA]] · [[AI & ML Roadmap]] · [[Discrete Mathematics]]
<!-- connections:end -->
