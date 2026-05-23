# MEC-203 — Quantitative Methods

**IGNOU | MA Economics (MAEC) | 8 Credits**

> [!info] About this file Covers PYQ analysis (Dec 2024, Jun 2024, Dec 2025, Jun 2025) + detailed notes + solved practice questions strictly as per syllabus.

---

## Table of Contents

- [[#Syllabus at a Glance]]
- [[#PYQ Frequency Analysis]]
- [[#Most Repeated Questions]]
- [[#Block 2 — Linear Algebra]]
- [[#Block 3 — Calculus]]
- [[#Block 4 — Real Analysis]]
- [[#Block 5 — Extreme Values and Optimisation]]
- [[#Block 6 — Economic Dynamics]]
- [[#Block 7 — Dynamic Optimisation]]
- [[#Block 8 — Probability and Probability Distributions]]
- [[#Block 9 — Inferential Statistics]]
- [[#Quick Revision Formulas]]
- [[#Exam Strategy]]

---

## Syllabus at a Glance

|Block|Title|Units|
|---|---|---|
|1|Review of Basic Mathematics|1–4|
|2|Linear Algebra|5–8|
|3|Calculus|9–12|
|4|Real Analysis|13–15|
|5|Extreme Values and Optimisation|16–19|
|6|Economic Dynamics|20–21|
|7|Dynamic Optimisation|22–24|
|8|Probability and Probability Distributions|25–27|
|9|Inferential Statistics|28–31|

---

## PYQ Frequency Analysis

### Topic-wise frequency across 4 papers

|Topic|Dec 2024|Jun 2024|Dec 2025|Jun 2025|**Total**|Priority|
|---|---|---|---|---|---|---|
|Linear Algebra (Cramer, eigenvalues)|✅|✅|✅|✅|**4/4**|🔴 Must Do|
|Taylor / Maclaurin Series|✅|✅|✅|✅|**4/4**|🔴 Must Do|
|Optimisation (Lagrange, max/min)|✅|✅|✅|✅|**4/4**|🔴 Must Do|
|Hypothesis Testing|✅|✅|✅|✅|**4/4**|🔴 Must Do|
|Sampling Methods & Bias|✅|✅|✅|✅|**4/4**|🔴 Must Do|
|Improper Integrals|✅|✅|—|✅|**3/4**|🟠 High|
|Limits & Continuity|✅|✅|✅|✅|**4/4**|🟠 High|
|Differential / Difference Equations|—|✅|✅|—|**2/4**|🟡 Medium|
|Probability Distributions|—|✅|✅|—|**2/4**|🟡 Medium|
|Vectors (norm, inner product)|✅|✅|—|—|**2/4**|🟡 Medium|
|Bolzano–Weierstrass / Topology|—|—|✅|—|**1/4**|🟢 Low|
|Cramer–Rao Inequality|—|—|✅|—|**1/4**|🟢 Low|

### Marks distribution (approx per paper)

|Section|Structure|Marks|
|---|---|---|
|Section A|Attempt any **2** out of 4 questions|2 × 20 = **40**|
|Section B|Attempt any **5** out of 7–8 questions|5 × 12 = **60**|
|**Total**||**100**|

---

## Most Repeated Questions

> [!warning] Verbatim repeats — guaranteed to come These exact questions have appeared in multiple papers. Memorise solutions.

1. **Taylor series for f(x,y,z) = xyz around (1,1,1)** — Dec 2024 Q2(b) AND Dec 2025 Q8
2. **Linear dependence of X₁=(1,2,3), X₂=(3,2,−1), X₃=(1,6,5)** — Dec 2024 Q1(a) AND Jun 2025 Q2(a)
3. **Consistency of system: x+2y=5, −2x+3z=−11, y−2z=8, 2x+y−z=12** — Dec 2024 Q1(b) AND Jun 2025 Q2(b)
4. **Eigenvalues of A = [[2,1],[1,2]]** — Dec 2024 Q1(c), Jun 2025 Q2(c), Jun 2024 Q1(c)
5. **Max/min of V = f(x,y,z) = −x³+3xz+2y−y²−3z²** — Dec 2024 Q10(a) AND Jun 2025 Q9(a)
6. **Taylor/Maclaurin for f(x) = cos x** — Dec 2024 Q6(b)
7. **Type I and Type II errors** — Dec 2024 Q3(b), Jun 2024 Q9(b)

---

## Block 2 — Linear Algebra

> [!abstract] Syllabus Units Unit 5: Matrix Algebra | Unit 6: Vector Analysis | Unit 7: Vectors and Matrices | Unit 8: Linear Equations

### 2.1 Cramer's Rule

For a system $Ax = b$, the solution is: $$x_i = \frac{\det(A_i)}{\det(A)}$$ where $A_i$ is matrix $A$ with the $i$-th column replaced by $b$.

**Steps:**

1. Write coefficient matrix $A$ and constant vector $b$
2. Compute $\det(A)$. If $\det(A) = 0$, Cramer's rule does not apply.
3. Form $A_1, A_2, A_3$ by replacing respective columns
4. Compute each determinant and divide

#### ✏️ Solved Question (Dec 2025 Q2 — 20 Marks)

**Q.** Solve using Cramer's rule: $$5x_1 - 2x_2 + 3x_3 = 16$$ $$2x_1 + 3x_2 - 5x_3 = 2$$ $$4x_1 - 5x_2 + 6x_3 = 7$$

**Solution:**

$$A = \begin{bmatrix} 5 & -2 & 3 \ \\
 2 & 3 & -5 \ \\
  4 & -5 & 6 \end{bmatrix}, \quad b = \begin{bmatrix} 16 \ 2 \ 7 \end{bmatrix}$$

**Step 1 — det(A):** $$\det(A) = 5(3 \cdot 6 - (-5)(-5)) - (-2)(2 \cdot 6 - (-5)(4)) + 3(2(-5) - 3(4))$$ $$= 5(18 - 25) + 2(12 + 20) + 3(-10 - 12)$$ $$= 5(-7) + 2(32) + 3(-22) = -35 + 64 - 66 = \mathbf{-37}$$

**Step 2 — det(A₁)** (replace col 1 with b): $$\det(A_1) = 16(18-25) - (-2)(12+35) + 3(-10-21) = -112 + 94 - 93 = -111$$

**Step 3 — det(A₂)** (replace col 2 with b): $$\det(A_2) = 5(12+35) - 16(12+20) + 3(14-12) = 235 - 512 + 6 = -271$$

**Step 4 — det(A₃)** (replace col 3 with b): $$\det(A_3) = 5(6+35) + 2(12-28) + 16(-10-12) = 205 - 32 - 352 = -179$$

**Answers:** $$x_1 = \frac{-111}{-37} = 3, \quad x_2 = \frac{-271}{-37} \approx 7.32, \quad x_3 = \frac{-179}{-37} \approx 4.84$$

---

### 2.2 Eigenvalues and Eigenvectors

**Characteristic equation:** $\det(A - \lambda I) = 0$

**Eigenvector:** Solve $(A - \lambda_i I)\mathbf{v} = \mathbf{0}$ for each eigenvalue $\lambda_i$.

#### ✏️ Solved Question (Repeated in 3 papers — 4 Marks each)

**Q.** Find eigenvalues of $A = \begin{bmatrix} 2 & 1 \ \\   1 & 2 \end{bmatrix}$

**Solution:** $$\det(A - \lambda I) = (2-\lambda)(2-\lambda) - (1)(1) = 0$$ $$\lambda^2 - 4\lambda + 4 - 1 = 0 \implies \lambda^2 - 4\lambda + 3 = 0$$ $$(\lambda - 1)(\lambda - 3) = 0 \implies \boxed{\lambda_1 = 1, \quad \lambda_2 = 3}$$

**Eigenvectors:**

- For $\lambda_1 = 1$: $(A - I)\mathbf{v} = 0 \implies \begin{bmatrix}1&1\1&1\end{bmatrix}\mathbf{v}=0 \implies v_1 = \begin{bmatrix}1\-1\end{bmatrix}$
- For $\lambda_2 = 3$: $(A - 3I)\mathbf{v} = 0 \implies \begin{bmatrix}-1&1\1&-1\end{bmatrix}\mathbf{v}=0 \implies v_2 = \begin{bmatrix}1\1\end{bmatrix}$

#### ✏️ Practice Question (Dec 2025 Q5 — 12 Marks)

**Q.** Find characteristic roots and vectors of $A = \begin{bmatrix} 6 & 6 \  \\  6 & -3 \end{bmatrix}$

**Solution:** $$\det(A - \lambda I) = (6-\lambda)(-3-\lambda) - 36 = 0$$ $$-18 - 6\lambda + 3\lambda + \lambda^2 - 36 = 0 \implies \lambda^2 - 3\lambda - 54 = 0$$ $$(\lambda - 9)(\lambda + 6) = 0 \implies \boxed{\lambda_1 = 9, \quad \lambda_2 = -6}$$

**Eigenvectors:**

- For $\lambda_1 = 9$: $\begin{bmatrix}-3&6\6&-12\end{bmatrix}\mathbf{v}=0 \implies -3v_1+6v_2=0 \implies v_1 = \begin{bmatrix}2\1\end{bmatrix}$
- For $\lambda_2 = -6$: $\begin{bmatrix}12&6\6&3\end{bmatrix}\mathbf{v}=0 \implies 2v_1+v_2=0 \implies v_2 = \begin{bmatrix}1\-2\end{bmatrix}$

---

### 2.3 Augmented Matrix and Linear Dependence

**Method:** Form the matrix with vectors as rows. Row-reduce to echelon form.

- If $\text{rank} < n$ (number of vectors) → **Linearly Dependent**
- If $\text{rank} = n$ → **Linearly Independent**

#### ✏️ Solved Question (Dec 2024 & Jun 2025 REPEATED — 8 Marks)

**Q.** Test linear dependency of $X_1=(1,2,3)$, $X_2=(3,2,-1)$, $X_3=(1,6,5)$

**Solution:** $$\begin{bmatrix} 1 & 2 & 3 \ \\
 3 & 2 & -1 \  \\
 1 & 6 & 5 \end{bmatrix}$$

$R_2 \leftarrow R_2 - 3R_1$: $\begin{bmatrix} 1&2&3 \ 0&-4&-10 \ 1&6&5 \end{bmatrix}$

$R_3 \leftarrow R_3 - R_1$: $\begin{bmatrix} 1&2&3 \ 0&-4&-10 \ 0&4&2 \end{bmatrix}$

$R_3 \leftarrow R_3 + R_2$: $\begin{bmatrix} 1&2&3 \ 0&-4&-10 \ 0&0&-8 \end{bmatrix}$

Rank = 3 = number of vectors → **Linearly Independent**. No linear relationship exists.

---

### 2.4 Consistency of System of Equations

**Rouché–Capelli Theorem:**

- System is **consistent** if $\text{rank}(A) = \text{rank}([A|b])$
- **Inconsistent** if $\text{rank}(A) < \text{rank}([A|b])$

#### ✏️ Solved Question (Dec 2024 & Jun 2025 REPEATED — 8 Marks)

**Q.** Is the following system consistent? $x + 2y = 5$, $-2x + 3z = -11$, $y - 2z = 8$, $2x + y - z = 12$

**Solution:** Augmented matrix $[A|b]$: $$\begin{bmatrix} 1&2&0&5 \ -2&0&3&-11 \ 0&1&-2&8 \ 2&1&-1&12 \end{bmatrix}$$

$R_2 \leftarrow R_2 + 2R_1$: row becomes $[0, 4, 3, -1]$

$R_4 \leftarrow R_4 - 2R_1$: row becomes $[0, -3, -1, 2]$

Continuing row reduction... After full reduction, $\text{rank}(A) = \text{rank}([A|b]) = 3$.

**The system is consistent.** (Solution exists.)

---

### 2.5 Vectors — Norm, Inner Product, Euclidean Distance

$$|x| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2} \quad \text{(Norm)}$$

$$d(x,y) = |x - y| = \sqrt{\sum_{i=1}^n (x_i - y_i)^2} \quad \text{(Euclidean distance)}$$

$$\langle x, y \rangle = \sum_{i=1}^n x_i y_i \quad \text{(Inner/Scalar product)}$$

#### ✏️ Solved Question (Dec 2024 Q9 — 9 Marks)

**Q.** For $x=(2,-1,-3,4,-2)$ and $y=(3,-1,-3,2,-3)$, find norm, distance, and scalar product.

**Norm of x:** $|x| = \sqrt{4+1+9+16+4} = \sqrt{34} \approx 5.83$

**Norm of y:** $|y| = \sqrt{9+1+9+4+9} = \sqrt{32} \approx 5.66$

**Euclidean distance:** $$d(x,y) = \sqrt{(2-3)^2+(-1+1)^2+(-3+3)^2+(4-2)^2+(-2+3)^2} = \sqrt{1+0+0+4+1} = \sqrt{6} \approx 2.45$$

**Scalar product:** $$\langle x,y \rangle = (2)(3)+(-1)(-1)+(-3)(-3)+(4)(2)+(-2)(-3) = 6+1+9+8+6 = \mathbf{30}$$

---

## Block 3 — Calculus

> [!abstract] Syllabus Units Unit 9: Limit and Continuity | Unit 10: Differential Calculus (one variable) | Unit 11: Differential Calculus (several variables) | Unit 12: Integration

### 3.1 Taylor's Theorem and Series

**Taylor series** for $f(x)$ around point $a$: $$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$$

**Maclaurin series** is Taylor series around $a=0$: $$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots$$

**Key Maclaurin series to memorise:**

|Function|Series|
|---|---|
|$e^x$|$1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$|
|$\sin x$|$x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$|
|$\cos x$|$1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$|
|$\ln(1+x)$|$x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ (valid for $|

---

#### ✏️ Solved Question (Dec 2024 Q2 & Dec 2025 Q8 — REPEATED — 12 Marks)

**Q.** Find Taylor series expansion for $f(x,y,z) = xyz$ around $(1,1,1)$

**Solution:**

Let $h = x-1$, $k = y-1$, $l = z-1$.

**Step 1 — Value at (1,1,1):** $$f(1,1,1) = 1 \cdot 1 \cdot 1 = 1$$

**Step 2 — First partial derivatives at (1,1,1):** $$f_x = yz = 1, \quad f_y = xz = 1, \quad f_z = xy = 1$$

**Step 3 — Second partial derivatives at (1,1,1):** $$f_{xx} = 0, \quad f_{yy} = 0, \quad f_{zz} = 0$$ $$f_{xy} = z = 1, \quad f_{xz} = y = 1, \quad f_{yz} = x = 1$$

**Step 4 — Third partial derivatives at (1,1,1):** $$f_{xyz} = 1 \quad \text{(all other third partials = 0)}$$

**Taylor expansion:** $$\boxed{f(x,y,z) = 1 + h + k + l + hk + hl + kl + hkl}$$

Substituting back: $$= 1 + (x-1) + (y-1) + (z-1) + (x-1)(y-1) + (x-1)(z-1) + (y-1)(z-1) + (x-1)(y-1)(z-1)$$

---

#### ✏️ Solved Question (Jun 2025 Q3 & Dec 2024 Q6 — 12 Marks)

**Q.** For $f(x) = \sin(x)$, find (i) linear and quadratic approximations, (ii) Maclaurin series.

**Solution:**

Compute derivatives at $x = 0$:

|$n$|$f^{(n)}(x)$|$f^{(n)}(0)$|
|---|---|---|
|0|$\sin x$|0|
|1|$\cos x$|1|
|2|$-\sin x$|0|
|3|$-\cos x$|-1|
|4|$\sin x$|0|

**(i) Linear approximation:** $P_1(x) = 0 + 1 \cdot x = \mathbf{x}$

**(ii) Quadratic approximation:** $P_2(x) = 0 + x + \frac{0}{2!}x^2 = \mathbf{x}$ (same as linear)

**(iii) Maclaurin series:** $$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}$$

---

#### ✏️ Practice: Maclaurin series for $\cos x$ (Dec 2024 Q6)

$f(0)=1$, $f'(0)=0$, $f''(0)=-1$, $f'''(0)=0$, $f^{(4)}(0)=1$

**Linear approx:** $P_1(x) = 1$

**Quadratic approx:** $P_2(x) = 1 - \frac{x^2}{2}$

**Maclaurin series:** $$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$$

---

### 3.2 Limits and L'Hôpital's Rule

**L'Hôpital's Rule:** If $\lim \frac{f}{g}$ gives $\frac{0}{0}$ or $\frac{\infty}{\infty}$: $$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

#### ✏️ Solved Questions (Jun 2025 Q5 — 8 Marks)

**(i)** $\displaystyle\lim_{x \to 1} \frac{x^3 - 2x^2 + 1}{x^3 - 1}$

At $x=1$: $\frac{0}{0}$ → L'Hôpital: $$= \lim_{x \to 1} \frac{3x^2 - 4x}{3x^2} = \frac{3-4}{3} = \mathbf{-\frac{1}{3}}$$

**(ii)** $\displaystyle\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$

At $x=0$: $\frac{0}{0}$ → L'Hôpital: $$= \lim_{x \to 0} \frac{e^x - 1}{2x} \xrightarrow{0/0} \lim_{x \to 0} \frac{e^x}{2} = \frac{1}{2} = \mathbf{\frac{1}{2}}$$

#### ✏️ Solved Questions (Jun 2024 Q7 — 8 Marks)

**(i)** $\displaystyle\lim_{x \to -2} \frac{x^3 + 8}{x^2 - 4}$

Factor: $\frac{(x+2)(x^2-2x+4)}{(x+2)(x-2)}$. Cancel $(x+2)$: $$= \lim_{x \to -2} \frac{x^2-2x+4}{x-2} = \frac{4+4+4}{-4} = \mathbf{-3}$$

**(ii)** $\displaystyle\lim_{x \to 4} \frac{\sqrt{x+5} - 3}{x-4}$

Multiply by conjugate $\frac{\sqrt{x+5}+3}{\sqrt{x+5}+3}$: $$= \lim_{x \to 4} \frac{(x+5)-9}{(x-4)(\sqrt{x+5}+3)} = \lim_{x \to 4} \frac{x-4}{(x-4)(\sqrt{x+5}+3)} = \frac{1}{\sqrt{9}+3} = \mathbf{\frac{1}{6}}$$

---

### 3.3 Partial Derivatives and Chain Rule

**Total differential:** For $z = f(x,y)$: $$dz = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$

**Chain rule:** For $u = f(x,y)$ where $x = x(t)$, $y = y(t)$: $$\frac{du}{dt} = \frac{\partial u}{\partial x}\frac{dx}{dt} + \frac{\partial u}{\partial y}\frac{dy}{dt}$$

**MRTS using partial derivatives:** $$MRTS_{KL} = \frac{MP_L}{MP_K} = \frac{\partial Q/\partial L}{\partial Q/\partial K}$$

---

### 3.4 Homogeneous and Homothetic Functions

**Homogeneous function** of degree $n$: $f(tx, ty) = t^n f(x,y)$

**Euler's theorem:** If $f$ is homogeneous of degree $n$: $$x \cdot f_x + y \cdot f_y = n \cdot f(x,y)$$

**Homothetic function:** A monotonic transformation of a homogeneous function. Not necessarily homogeneous itself, but retains the same ordinal properties.

**Difference:**

|Property|Homogeneous|Homothetic|
|---|---|---|
|Definition|$f(tx,ty) = t^n f(x,y)$|$f = g(h(x,y))$ where $h$ is homogeneous|
|Euler's theorem|✅ Applies directly|❌ Does not directly apply|
|Returns to scale|Clear (= degree $n$)|Not necessarily constant|
|Economic use|CRS production functions|Demand functions, indirect utility|

---

## Block 4 — Real Analysis

> [!abstract] Syllabus Units Unit 13: Real Analysis | Unit 14: Metric Space & Point Set Topology | Unit 15: Calculus of Several Variables

### 4.1 Continuity of Functions

A function $f$ is **continuous at** $x = a$ if:

1. $f(a)$ is defined
2. $\lim_{x \to a} f(x)$ exists
3. $\lim_{x \to a} f(x) = f(a)$

**Properties of continuous functions:**

- Sum, difference, product of continuous functions is continuous
- Quotient $f/g$ is continuous where $g \neq 0$
- Composition of continuous functions is continuous
- **Intermediate Value Theorem (IVT):** If $f$ is continuous on $[a,b]$ and $k$ is between $f(a)$ and $f(b)$, then $\exists c \in (a,b)$ such that $f(c) = k$
- **Extreme Value Theorem:** A continuous function on a closed bounded interval attains its max and min

#### ✏️ Solved Question (Dec 2024 Q6 — 5 Marks)

**Q.** Check if the following function is continuous: $$f(x) = \begin{cases} x+2 & x < 2 \ x^2-2 & 2 \le x < 3 \ 2x+5 & x \ge 3 \end{cases}$$

**At $x = 2$:**

- $\lim_{x \to 2^-} f(x) = 2+2 = 4$
- $\lim_{x \to 2^+} f(x) = 4-2 = 2$
- Left limit ≠ Right limit → **Discontinuous at $x=2$**

**At $x = 3$:**

- $\lim_{x \to 3^-} f(x) = 9-2 = 7$
- $\lim_{x \to 3^+} f(x) = 6+5 = 11$
- Left limit ≠ Right limit → **Discontinuous at $x=3$**

**Conclusion:** Function is **not continuous** at $x=2$ and $x=3$.

---

### 4.2 Improper Integrals

$$\int_a^{\infty} f(x)dx = \lim_{b \to \infty} \int_a^b f(x)dx$$

**Convergent** if the limit exists and is finite. **Divergent** if limit is $\pm\infty$ or does not exist.

**Standard results:** $$\int_1^{\infty} \frac{1}{x^p}dx \text{ converges if } p > 1, \text{ diverges if } p \le 1$$

#### ✏️ Solved Questions

**Q1 (Dec 2024 Q8 — 5 Marks):** Is $\displaystyle\int_1^{\infty} \frac{1}{x^2}dx$ convergent?

$$\int_1^b x^{-2}dx = \left[-\frac{1}{x}\right]_1^b = \left(-\frac{1}{b}\right) - (-1) = 1 - \frac{1}{b}$$

As $b \to \infty$: limit $= 1$. **Convergent, value = 1.**

**Q2 (Jun 2025 Q10 — 5 Marks):** Is $\displaystyle\int_{-\infty}^{0} \frac{1}{\sqrt{3-x}}dx$ convergent?

$$\int_{-b}^{0} (3-x)^{-1/2}dx = \left[-2\sqrt{3-x}\right]_{-b}^0 = (-2\sqrt{3}) - (-2\sqrt{3+b})$$

As $b \to \infty$: $2\sqrt{3+b} \to \infty$. **Divergent.**

---

### 4.3 Open Sets and Closed Sets

- **Open set:** Every point is an interior point (no boundary points included). Example: $(a,b)$
- **Closed set:** Contains all its boundary points / complement is open. Example: $[a,b]$

**Key theorem (PYQ Dec 2024 Q8):** The union of a finite number of closed sets is a closed set.

_Proof sketch:_ Let $F_1, F_2, \ldots, F_n$ be closed sets. Their complements $F_1^c, \ldots, F_n^c$ are open. By De Morgan's law: $(F_1 \cup \cdots \cup F_n)^c = F_1^c \cap \cdots \cap F_n^c$. Finite intersection of open sets is open. Therefore $F_1 \cup \cdots \cup F_n$ is closed. $\square$

---

## Block 5 — Extreme Values and Optimisation

> [!abstract] Syllabus Units Unit 16: Optimisation Introduction | Unit 17: Unconstrained and Constrained Optimisation | Unit 18–19: Advanced Optimisation

### 5.1 Unconstrained Optimisation

**First-order conditions (FOC):** $f_x = 0$ and $f_y = 0$

**Second-order conditions (SOC) using Hessian:** $$H = \begin{vmatrix} f_{xx} & f_{xy} \ f_{yx} & f_{yy} \end{vmatrix} = f_{xx}f_{yy} - (f_{xy})^2$$

|Condition|Conclusion|
|---|---|
|$H > 0$ and $f_{xx} > 0$|**Local minimum**|
|$H > 0$ and $f_{xx} < 0$|**Local maximum**|
|$H < 0$|**Saddle point**|
|$H = 0$|Inconclusive|

#### ✏️ Solved Question (Dec 2025 Q10 — 12 Marks)

**Q.** Find stationary values of $z = 3x^2 + 6xy + 7y^2$ and determine if max or min.

**FOC:** $$f_x = 6x + 6y = 0 \implies x + y = 0 \implies x = -y$$ $$f_y = 6x + 14y = 0$$

Substituting $x = -y$: $-6y + 14y = 0 \implies 8y = 0 \implies y = 0, x = 0$

**Stationary point: $(0, 0)$, $z = 0$**

**SOC:** $$f_{xx} = 6, \quad f_{yy} = 14, \quad f_{xy} = 6$$ $$H = (6)(14) - (6)^2 = 84 - 36 = 48 > 0, \quad f_{xx} = 6 > 0$$

**$\implies$ Local minimum at $(0,0)$ with $z = 0$.**

#### ✏️ Solved Question (Dec 2024 Q10 & Jun 2025 Q9 — REPEATED — 8 Marks)

**Q.** Indicate whether $V = f(x,y,z) = -x^3 + 3xz + 2y - y^2 - 3z^2$ has maximum or minimum.

**First-order conditions:** $$V_x = -3x^2 + 3z = 0 \implies z = x^2 \quad \cdots (1)$$ $$V_y = 2 - 2y = 0 \implies y = 1 \quad \cdots (2)$$ $$V_z = 3x - 6z = 0 \implies x = 2z \quad \cdots (3)$$

From (1) and (3): $z = x^2$ and $x = 2z = 2x^2 \implies x(2x-1) = 0$

So $x = 0$ or $x = \frac{1}{2}$.

**Point 1:** $x=0, z=0, y=1$ → $(0,1,0)$

**Point 2:** $x=\frac{1}{2}, z=\frac{1}{4}, y=1$ → $(\frac{1}{2}, 1, \frac{1}{4})$

**Hessian matrix at each point:** $$H = \begin{bmatrix} V_{xx} & V_{xy} & V_{xz} \ V_{yx} & V_{yy} & V_{yz} \ V_{zx} & V_{zy} & V_{zz} \end{bmatrix} = \begin{bmatrix} -6x & 0 & 3 \ 0 & -2 & 0 \ 3 & 0 & -6 \end{bmatrix}$$

At $(0,1,0)$: $H = \begin{bmatrix}0&0&3\0&-2&0\3&0&-6\end{bmatrix}$. $|H| = 0(-12-0) - 0 + 3(0+6) = 18 > 0$ but $H_{11} = 0$. Inconclusive by this method; further analysis needed.

At $(\frac{1}{2},1,\frac{1}{4})$: $H_{11} = -3$. $H_1 = -3 < 0$. $H_2 = (-3)(-2) - 0 = 6 > 0$. $H_3 = |H| < 0$. Signs alternate $(-,+,-)$ → **neither maximum nor minimum (saddle point)**.

---

### 5.2 Lagrange Multiplier Method

**Problem:** Maximise $f(x,y)$ subject to $g(x,y) = c$

**Lagrangian:** $\mathcal{L} = f(x,y) - \lambda[g(x,y) - c]$

**FOC:** $$\mathcal{L}_x = f_x - \lambda g_x = 0$$ $$\mathcal{L}_y = f_y - \lambda g_y = 0$$ $$\mathcal{L}_\lambda = g(x,y) - c = 0$$

The **Lagrange multiplier $\lambda$** measures the rate of change of the optimal value with respect to the constraint parameter $c$: $\lambda = \frac{df^*}{dc}$

#### ✏️ Solved Question (Jun 2025 Q1 — 12 Marks)

**Q.** Maximise $u_3 = 4u_1^2 + 3u_1u_2 + 6u_2^2$ subject to $u_1 + u_2 = 56$

**Lagrangian:** $\mathcal{L} = 4u_1^2 + 3u_1u_2 + 6u_2^2 - \lambda(u_1 + u_2 - 56)$

**FOC:** $$\mathcal{L}_{u_1} = 8u_1 + 3u_2 - \lambda = 0 \quad \cdots (i)$$ $$\mathcal{L}_{u_2} = 3u_1 + 12u_2 - \lambda = 0 \quad \cdots (ii)$$ $$u_1 + u_2 = 56 \quad \cdots (iii)$$

$(i) - (ii)$: $5u_1 - 9u_2 = 0 \implies u_1 = \frac{9u_2}{5}$

Substituting in (iii): $\frac{9u_2}{5} + u_2 = 56 \implies \frac{14u_2}{5} = 56 \implies \mathbf{u_2 = 20}$

$\implies \mathbf{u_1 = 36}$

**Maximum value:** $u_3 = 4(1296) + 3(36)(20) + 6(400) = 5184 + 2160 + 2400 = \mathbf{9744}$

---

### 5.3 Envelope Theorem

If $f^_(a)$ is the optimal value as parameter $a$ varies: $$\frac{df^_}{da} = \frac{\partial \mathcal{L}^*}{\partial a}\bigg|_{\text{at optimum}}$$

**Meaning:** The rate of change of the maximum value equals the partial derivative of the Lagrangian w.r.t. the parameter, evaluated at the optimum — without re-solving the problem.

---

### 5.4 Kuhn–Tucker Conditions

For **maximisation** of $f(\mathbf{x})$ subject to $g_i(\mathbf{x}) \le b_i$, $x_j \ge 0$:

**KT conditions:** $$\frac{\partial \mathcal{L}}{\partial x_j} \le 0, \quad x_j \ge 0, \quad x_j \cdot \frac{\partial \mathcal{L}}{\partial x_j} = 0 \quad \forall j$$ $$\lambda_i \ge 0, \quad g_i(\mathbf{x}) \le b_i, \quad \lambda_i[g_i(\mathbf{x}) - b_i] = 0 \quad \forall i$$

The last conditions are called **complementary slackness conditions**.

**Sufficiency:** For concave $f$ and convex $g_i$, KT conditions are both necessary and sufficient.

### 5.5 Concave and Convex Functions

- **Convex function:** $f(\lambda x + (1-\lambda)y) \le \lambda f(x) + (1-\lambda)f(y)$ for $\lambda \in [0,1]$. Second derivative $f'' \ge 0$.
- **Concave function:** Inequality reversed. $f'' \le 0$.
- **Quasi-concave:** Upper contour sets are convex. Weaker than concavity — a function can be quasi-concave without being concave.
- **Inflection point:** Where $f''(x) = 0$ and $f''$ changes sign.

---

### 5.6 Mean Value Theorem

If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then $\exists c \in (a,b)$ such that: $$f'(c) = \frac{f(b) - f(a)}{b - a}$$

#### ✏️ Solved Question (Dec 2024 Q4 — 8 Marks)

**Q.** Verify MVT for $f(x) = (x-1)(x-2)$ on $\left[0, \frac{1}{2}\right]$

**Step 1:** $f(0) = (-1)(-2) = 2$; $f(\frac{1}{2}) = (-\frac{1}{2})(-\frac{3}{2}) = \frac{3}{4}$

**Step 2:** RHS $= \frac{f(b)-f(a)}{b-a} = \frac{3/4 - 2}{1/2} = \frac{-5/4}{1/2} = -\frac{5}{2}$

**Step 3:** $f'(x) = (x-2) + (x-1) = 2x - 3$

**Step 4:** $f'(c) = 2c - 3 = -\frac{5}{2} \implies 2c = 3 - \frac{5}{2} = \frac{1}{2} \implies c = \frac{1}{4}$

Since $c = \frac{1}{4} \in \left(0, \frac{1}{2}\right)$, **MVT is verified.** $\square$

---

## Block 6 — Economic Dynamics

> [!abstract] Syllabus Units Unit 20: Difference Equations — Theory and Economic Applications | Unit 21: Differential Equations

### 6.1 First-Order Differential Equations

**General form:** $\frac{dy}{dt} + P(t)y = Q(t)$

**Integrating factor:** $\mu(t) = e^{\int P(t)dt}$

**General solution:** $$y(t) = e^{-\int P,dt}\left[\int Q \cdot e^{\int P,dt},dt + C\right]$$

**For constant coefficients** ($\frac{dy}{dt} + ay = b$): $$y(t) = \left(y_0 - \frac{b}{a}\right)e^{-at} + \frac{b}{a}$$

- Equilibrium (particular solution): $\bar{y} = \frac{b}{a}$
- Complementary function: $Ce^{-at}$
- **Stable** if $a > 0$ (solution converges to $\bar{y}$)

#### ✏️ Solved Question (Dec 2025 Q3a — 10 Marks)

**Q.** How is the Harrod–Domar model solved using differential equations?

**Model setup:**

- Savings function: $S = sY$ (where $s$ = marginal propensity to save)
- Investment: $I = v\frac{dY}{dt}$ (where $v$ = capital-output ratio)
- Equilibrium condition: $S = I$

**Derivation:** $$sY = v\frac{dY}{dt} \implies \frac{dY}{dt} - \frac{s}{v}Y = 0$$

This is a first-order linear DE with $P = -s/v$, $Q = 0$.

**Solution:** $$Y(t) = Y_0 \cdot e^{(s/v)t}$$

**Interpretation:**

- The economy grows at rate $g_w = s/v$ (warranted rate of growth)
- Growth is exponential
- Since $s/v > 0$, output diverges from any given level — **knife-edge instability**: if actual growth $\neq$ warranted growth, the economy moves further away from equilibrium.

---

### 6.2 First-Order Difference Equations

**General form:** $y_t = a \cdot y_{t-1} + b$

**Equilibrium:** $\bar{y} = \frac{b}{1-a}$ (if $a \ne 1$)

**General solution:** $$y_t = (y_0 - \bar{y}) \cdot a^t + \bar{y}$$

**Stability analysis:**

|Condition|Behaviour|
|---|---|
|$\|a\| < 1$|Convergent (stable) towards $\bar{y}$|
|$\|a\| > 1$|Divergent (unstable) away from $\bar{y}$|
|$a > 0$|Non-oscillatory (monotone)|
|$a < 0$|Oscillatory (alternating signs)|
|$a = 1$|No unique equilibrium|
|$a = -1$|Persistent oscillations|

#### ✏️ Solved Question (Jun 2024 Q4 — 20 Marks)

**Q.** Find time path of price when $D_t = 86 - 0.8P_t$ and $S_t = -10 + 0.8P_{t-1}$

**Setting $D_t = S_t$:** $$86 - 0.8P_t = -10 + 0.8P_{t-1}$$ $$0.8P_t = 96 - 0.8P_{t-1}$$ $$P_t = 120 - P_{t-1} \quad \text{i.e., } P_t = (-1)P_{t-1} + 120$$

**Here $a = -1$, $b = 120$.**

**Equilibrium price:** $$\bar{P} = \frac{120}{1 - (-1)} = \frac{120}{2} = \mathbf{60}$$

**General solution:** $$P_t = (P_0 - 60)(-1)^t + 60$$

**Behaviour:** Since $a = -1$, $|a| = 1$ → price **oscillates indefinitely** with constant amplitude between $(P_0 - 60)$ above and below 60. This is the **cobweb model** — the market exhibits **dynamic instability** (neither convergent nor divergent, but perpetually oscillating).

---

## Block 7 — Dynamic Optimisation

> [!abstract] Syllabus Units Unit 22–23: Intertemporal Optimisation | Unit 24: Economic Applications of Dynamic Optimisation

### 7.1 Price Elasticity of Demand

$$\varepsilon = \frac{dq}{dp} \cdot \frac{p}{q}$$

#### ✏️ Solved Question (Dec 2025 Q1a — 10 Marks)

**Q.** For $q = Ap^\varepsilon$ ($\varepsilon < 0$), obtain price elasticity of demand.

$$\frac{dq}{dp} = A \cdot \varepsilon \cdot p^{\varepsilon - 1}$$

$$\text{Elasticity} = \frac{dq}{dp} \cdot \frac{p}{q} = A\varepsilon p^{\varepsilon-1} \cdot \frac{p}{Ap^\varepsilon} = \frac{A\varepsilon p^\varepsilon}{Ap^\varepsilon} = \boxed{\varepsilon}$$

The price elasticity is the constant $\varepsilon$ (the exponent itself). Since $\varepsilon < 0$, demand is elastic or inelastic depending on its magnitude.

---

## Block 8 — Probability and Probability Distributions

> [!abstract] Syllabus Units Unit 25: Probability Theory | Unit 26: Probability Distribution–I | Unit 27: Probability Distribution–II

### 8.1 Binomial Distribution

$$P(X = r) = \binom{n}{r} p^r (1-p)^{n-r}, \quad r = 0,1,2,\ldots,n$$

$$\text{Mean} = np, \quad \text{Variance} = np(1-p)$$

**Derivation of mean:** $$E(X) = \sum_{r=0}^{n} r \binom{n}{r} p^r q^{n-r} = np\sum_{r=1}^{n} \binom{n-1}{r-1} p^{r-1} q^{n-r} = np(p+q)^{n-1} = np$$

---

### 8.2 Poisson Distribution

$$P(X = r) = \frac{e^{-\lambda}\lambda^r}{r!}, \quad r = 0,1,2,\ldots$$

$$\text{Mean} = \lambda, \quad \text{Variance} = \lambda$$

**Salient features:**

1. Discrete distribution for rare events
2. Mean = Variance = $\lambda$
3. Sum of independent Poisson variables is Poisson
4. As $\lambda$ increases, distribution becomes more symmetric (approaches normal)

### 8.3 Poisson as Limiting Case of Binomial (PYQ Jun 2024)

**Conditions:** $n \to \infty$, $p \to 0$, but $np = \lambda$ (constant).

**Proof sketch:** $$P(X=r) = \binom{n}{r}p^r(1-p)^{n-r} = \frac{n!}{r!(n-r)!}\left(\frac{\lambda}{n}\right)^r\left(1-\frac{\lambda}{n}\right)^{n-r}$$

As $n \to \infty$:

- $\frac{n!}{(n-r)! \cdot n^r} \to 1$
- $\left(1-\frac{\lambda}{n}\right)^n \to e^{-\lambda}$
- $\left(1-\frac{\lambda}{n}\right)^{-r} \to 1$

$$\therefore P(X=r) \to \frac{e^{-\lambda}\lambda^r}{r!} \quad \square$$

---

## Block 9 — Inferential Statistics

> [!abstract] Syllabus Units Unit 28: Sampling Theory | Unit 29: Sampling Distributions | Unit 30: Estimation | Unit 31: Hypothesis Testing

### 9.1 Sampling Theory

**Population vs Sample:**

|Term|Meaning|Symbol|
|---|---|---|
|Parameter|Numerical summary of **population**|$\mu$, $\sigma$, $\pi$|
|Statistic|Numerical summary of **sample**|$\bar{x}$, $s$, $p$|

**Sampling design:** The plan specifying how the sample will be selected.

**Advantages of sample survey:**

- Less time and cost
- More detailed information possible
- Useful when population is very large or infinite
- Suitable when destructive testing required

**Types of sampling:**

1. **Simple Random Sampling (SRS):** Every unit has equal probability of selection
2. **Stratified Sampling:** Population divided into strata; random sample from each
3. **Systematic Sampling:** Every $k$-th unit selected after a random start
4. **Cluster Sampling:** Population divided into clusters; entire clusters selected
5. **Multi-stage Sampling:** Combination of methods at multiple stages

**Sources of bias in sample surveys:**

1. Selection bias (non-random selection)
2. Non-response bias
3. Measurement/response bias
4. Interviewer bias
5. Sampling frame errors

---

### 9.2 Sampling Distribution

**Sampling distribution of $\bar{x}$:** $$E(\bar{x}) = \mu, \quad \text{Var}(\bar{x}) = \frac{\sigma^2}{n}$$

**Standard Error:** $SE(\bar{x}) = \frac{\sigma}{\sqrt{n}}$

- Standard error measures the variability of the sampling distribution
- Larger $n$ → smaller SE → more precise estimate
- By **Central Limit Theorem (CLT):** For large $n$, $\bar{x}$ is approximately normally distributed regardless of the population distribution

---

### 9.3 Hypothesis Testing

**Steps in hypothesis testing:**

1. State $H_0$ (null) and $H_1$ (alternative)
2. Choose significance level $\alpha$
3. Select test statistic
4. Determine critical region
5. Compute test statistic from data
6. Decision: Reject or fail to reject $H_0$

**Type I and Type II errors:**

|Decision|$H_0$ True|$H_0$ False|
|---|---|---|
|Reject $H_0$|**Type I error** ($\alpha$)|Correct (Power = $1-\beta$)|
|Fail to reject $H_0$|Correct|**Type II error** ($\beta$)|

- **Type I error:** Rejecting true $H_0$ (false positive). Probability = $\alpha$ = level of significance.
- **Type II error:** Not rejecting false $H_0$ (false negative). Probability = $\beta$.
- Trade-off: For fixed $n$, reducing $\alpha$ increases $\beta$.

---

### 9.4 One-Tail and Two-Tail Tests

**Two-tail test:**

- $H_0: \mu = \mu_0$ vs $H_1: \mu \ne \mu_0$
- Reject if $|Z| > Z_{\alpha/2}$
- Used when deviation in either direction matters

**One-tail (right) test:**

- $H_0: \mu \le \mu_0$ vs $H_1: \mu > \mu_0$
- Reject if $Z > Z_\alpha$

**One-tail (left) test:**

- $H_0: \mu \ge \mu_0$ vs $H_1: \mu < \mu_0$
- Reject if $Z < -Z_\alpha$

**Common critical values:**

|$\alpha$|Two-tail $Z_{\alpha/2}$|One-tail $Z_\alpha$|
|---|---|---|
|0.10|1.645|1.28|
|0.05|1.96|1.645|
|0.01|2.576|2.33|

---

### 9.5 P-value Method

The **p-value** is the probability of observing a test statistic as extreme as (or more extreme than) the computed value, assuming $H_0$ is true.

**Decision rule:** Reject $H_0$ if $p\text{-value} \le \alpha$

**Advantage:** Gives precise measure of evidence against $H_0$ rather than just accept/reject.

---

### 9.6 Critical Region

The **critical region** (rejection region) is the set of values of the test statistic for which $H_0$ is rejected. It is determined by:

- The significance level $\alpha$
- Whether the test is one-tailed or two-tailed
- The distribution of the test statistic

---

## Quick Revision Formulas

> [!tip] Key formulas to memorise

### Linear Algebra

$$\det(A - \lambda I) = 0 \quad \text{(Characteristic equation)}$$ $$x_i = \frac{\det(A_i)}{\det(A)} \quad \text{(Cramer's rule)}$$

### Calculus

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n \quad \text{(Taylor series)}$$ $$\lim \frac{f}{g} = \lim \frac{f'}{g'} \quad \text{(L'Hôpital, when 0/0 or ∞/∞)}$$ $$x \cdot f_x + y \cdot f_y = n \cdot f(x,y) \quad \text{(Euler's theorem)}$$

### Optimisation

$$\mathcal{L} = f - \lambda[g - c] \quad \text{(Lagrangian)}$$ $$D = f_{xx}f_{yy} - (f_{xy})^2 \quad \text{(Discriminant for max/min)}$$ $$\frac{df^*}{dc} = \lambda \quad \text{(Envelope theorem)}$$

### Dynamics

$$y_t = (y_0 - \bar{y})a^t + \bar{y} \quad \text{(Difference equation solution)}$$ $$y(t) = (y_0 - \bar{y})e^{-at} + \bar{y} \quad \text{(Differential equation solution)}$$ $$Y(t) = Y_0 e^{(s/v)t} \quad \text{(Harrod-Domar)}$$

### Statistics

$$SE(\bar{x}) = \frac{\sigma}{\sqrt{n}} \quad \text{(Standard error)}$$ $$Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} \quad \text{(Test statistic for mean)}$$ $$P(X=r) = \frac{e^{-\lambda}\lambda^r}{r!} \quad \text{(Poisson)}$$

---

## Exam Strategy

> [!success] Section A — Pick 2 from 4 (40 marks) **Safe picks:**
> 
> - **Linear Algebra question** (Cramer's rule / eigenvalues / augmented matrix) — appears in every paper, solutions are algorithmic
> - **Taylor/Maclaurin series question** — very predictable, same types repeat
> - **Optimisation question** (Lagrange multiplier) if you are comfortable with calculus

> [!success] Section B — Pick 5 from 7–8 (60 marks) **Recommended:**
> 
> - Standard error + sampling distribution (easy theory)
> - Type I/II errors + hypothesis testing (theory-based, scoring)
> - One limits question (direct computation)
> - Improper integrals (one formula, plugging in)
> - Vectors (norm, inner product — mechanical computation)
> 
> **Skip if unsure:**
> 
> - Topology proofs (Bolzano–Weierstrass, closed set proofs)
> - Cramer–Rao inequality

> [!warning] Topics NOT to skip
> 
> 1. Taylor series — **verbatim repeats** across papers
> 2. Cramer's rule — appeared in ALL 4 papers
> 3. Eigenvalues of [[2,1],[1,2]] — exact question repeated 3 times
> 4. Hypothesis testing vocabulary (Type I/II, critical region, p-value)
> 5. Harrod–Domar via differential equations

> [!note] Time management (3 hours)
> 
> - Section A: ~70 minutes (35 min per question)
> - Section B: ~110 minutes (22 min per question)
> - Buffer: 10 minutes for review

---

_Notes prepared from: Quantitative Methods Syllabus (IGNOU MAEC MEC-203) + PYQ papers: Dec 2024, Jun 2024, Dec 2025, Jun 2025_
