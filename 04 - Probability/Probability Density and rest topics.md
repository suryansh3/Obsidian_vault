Of course. Here is the entire explanation and problem set in a structured Markdown format, optimized for readability in Obsidian, with proper LaTeX for equations.

---

## **Part 1: Continuous Random Variables & Specific Distributions**

### **Core Concepts**

#### **1. Continuous Random Variable (CRV)**
A variable that can take on an infinite number of values within a range. The probability it equals any single value is zero.
- **Example:** Height, time until decay, volume.

#### **2. Probability Density Function (PDF) - \( f(x) \)**
Describes the relative likelihood of a CRV.
- **Properties:**
  1. \( f(x) \geq 0 \)
  2. \( \int_{-\infty}^{\infty} f(x)  dx = 1 \)
  3. \( P(a \leq X \leq b) = \int_{a}^{b} f(x)  dx \)

#### **3. Cumulative Distribution Function (CDF) - \( F(x) \)**
Gives \( P(X \leq x) \).
- \( F(x) = P(X \leq x) = \int_{-\infty}^{x} f(t)  dt \)
- **Properties:** Non-decreasing, \( \lim_{x \to -\infty} F(x) = 0 \), \( \lim_{x \to \infty} F(x) = 1 \), \( P(a < X \leq b) = F(b) - F(a) \)

#### **4. Moment Generating Function (MGF) - \( M_X(t) \)**
- \( M_X(t) = E[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} f(x)  dx \) (for continuous)
- **Uses:**
  - \( E[X^n] = M_X^{(n)}(0) \)
  - Identifies distributions
  - Simplifies sums of independent variables

---

### **Key Distributions**

#### **Uniform Distribution**
- **Notation:** \( X \sim \text{Uniform}(a, b) \)
- **PDF:** \( f(x) = \frac{1}{b-a} \) for \( a \leq x \leq b \)
- **CDF:** \( F(x) = \frac{x-a}{b-a} \) for \( a \leq x \leq b \)
- **Mean:** \( E[X] = \frac{a+b}{2} \)
- **Variance:** \( \text{Var}(X) = \frac{(b-a)^2}{12} \)

#### **Normal Distribution**
- **Notation:** \( X \sim N(\mu, \sigma^2) \)
- **PDF:** \( f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} \)
- **Standard Normal:** \( Z \sim N(0, 1) \), CDF = \( \Phi(z) \)
- **68-95-99.7 Rule:**
  - \( P(\mu - \sigma < X < \mu + \sigma) \approx 0.68 \)
  - \( P(\mu - 2\sigma < X < \mu + 2\sigma) \approx 0.95 \)
  - \( P(\mu - 3\sigma < X < \mu + 3\sigma) \approx 0.997 \)

#### **Exponential Distribution**
- **Notation:** \( X \sim \text{Exp}(\lambda) \)
- **PDF:** \( f(x) = \lambda e^{-\lambda x} \) for \( x \geq 0 \)
- **CDF:** \( F(x) = 1 - e^{-\lambda x} \)
- **Mean:** \( E[X] = \frac{1}{\lambda} \)
- **Variance:** \( \text{Var}(X) = \frac{1}{\lambda^2} \)
- **Memoryless Property:** \( P(X > s + t  X > s) = P(X > t) \)

---

### **Normal Distribution Tools**

#### **Percentiles & Critical Values**
- **Percentile \( x_p \)**: \( P(X \leq x_p) = p \). For \( Z \), \( z_p = \Phi^{-1}(p) \)
- **Critical Value \( z_{\alpha} \)**: \( P(Z > z_{\alpha}) = \alpha \). Common: \( z_{0.05} = 1.645 \)

#### **Normal Approximation to Binomial**
For \( X \sim \text{Bin}(n, p) \), approximate with \( N(\mu, \sigma^2) \) where:
- \( \mu = np \)
- \( \sigma^2 = np(1-p) \)
- **Continuity Correction:** \( P(X \leq k) \approx P\left(Z \leq \frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right) \)

---

## **Questions: Continuous Random Variables & Distributions**

### **Level 1: Basic Definition & Application**
**Q1:** The time (in minutes) a customer spends in a shop has PDF \( f(x) = \frac{x}{8} \) for \( 0 \leq x \leq 4 \).
a) Is this a valid PDF?
b) Find \( P(X < 2) \).

**Solution:**
a) Check: \( \int_{0}^{4} \frac{x}{8}  dx = \frac{1}{8} \cdot \frac{x^2}{2} \Big|_{0}^{4} = \frac{1}{16}(16) = 1 \). ✅ Valid.
b) \( P(X < 2) = \int_{0}^{2} \frac{x}{8}  dx = \frac{1}{8} \cdot \frac{x^2}{2} \Big|_{0}^{2} = \frac{4}{16} = 0.25 \)

---

### **Level 2: Using the CDF**
**Q2:** For the CRV in Q1, find:
a) The CDF \( F(x) \)
b) \( P(1 < X < 3) \) using the CDF

**Solution:**
a) \( F(x) = \int_{0}^{x} \frac{t}{8}  dt = \frac{t^2}{16} \Big|_{0}^{x} = \frac{x^2}{16} \) for \( 0 \leq x \leq 4 \)
b) \( P(1 < X < 3) = F(3) - F(1) = \frac{9}{16} - \frac{1}{16} = \frac{8}{16} = 0.5 \)

---

### **Level 3: Uniform Distribution**
**Q3:** A bus arrives every 15 minutes. Find the probability a randomly arriving person waits >10 minutes.

**Solution:**
Let \( X \sim \text{Uniform}(0, 15) \)
- \( P(X > 10) = 1 - F(10) = 1 - \frac{10}{15} = \frac{1}{3} \)

---

### **Level 4: Exponential Distribution & Memoryless Property**
**Q4:** Lightbulb lifetime \( X \sim \text{Exp}(\lambda) \) with mean 1000 hours.
a) Find \( P(X > 1500) \)
b) If it has lasted 1000 hours, find \( P(X > 1500) \)

**Solution:**
- \( E[X] = \frac{1}{\lambda} = 1000 \Rightarrow \lambda = 0.001 \)
a) \( P(X > 1500) = 1 - F(1500) = e^{-0.001 \times 1500} = e^{-1.5} \approx 0.223 \)
b) Memoryless: \( P(X > 1500  X > 1000) = P(X > 500) = e^{-0.001 \times 500} = e^{-0.5} \approx 0.606 \)

---

### **Level 5: Normal Distribution - Basic Calculation**
**Q5:** Test scores \( X \sim N(75, 10^2) \). Find percentage scoring above 90.

**Solution:**
- \( P(X > 90) = P\left(Z > \frac{90-75}{10}\right) = P(Z > 1.5) = 1 - \Phi(1.5) \approx 1 - 0.9332 = 0.0668 \) (6.68%)

---

### **Level 6: Normal Distribution - Percentiles**
**Q6:** For scores in Q5, find the 95th percentile score.

**Solution:**
- Find \( z \) such that \( \Phi(z) = 0.95 \Rightarrow z \approx 1.645 \)
- \( x = \mu + z\sigma = 75 + 1.645 \times 10 = 91.45 \)

---

### **Level 7: Normal Approximation to Binomial**
**Q7:** A fair coin is tossed 400 times. Estimate \( P(185 \leq \text{Heads} \leq 210) \).

**Solution:**
- \( n = 400, p = 0.5 \Rightarrow \mu = 200, \sigma = \sqrt{100} = 10 \)
- With continuity correction: \( P(184.5 \leq X \leq 210.5) \)
- \( Z_{\text{lower}} = \frac{184.5 - 200}{10} = -1.55 \), \( Z_{\text{upper}} = \frac{210.5 - 200}{10} = 1.05 \)
- \( P(-1.55 \leq Z \leq 1.05) = \Phi(1.05) - \Phi(-1.55) = \Phi(1.05) - (1 - \Phi(1.55)) \approx 0.8531 - (1 - 0.9394) = 0.7925 \)

---

### **Level 8: Moment Generating Function**
**Q8:** For \( X \sim \text{Exp}(\lambda) \):
a) Find \( M_X(t) \)
b) Use it to find \( E[X] \) and \( \text{Var}(X) \)

**Solution:**
a) \( M_X(t) = \int_{0}^{\infty} e^{tx} \lambda e^{-\lambda x}  dx = \lambda \int_{0}^{\infty} e^{-(\lambda - t)x}  dx = \frac{\lambda}{\lambda - t} \) for \( t < \lambda \)
b) 
- \( M_X'(t) = \frac{\lambda}{(\lambda - t)^2} \Rightarrow E[X] = M_X'(0) = \frac{\lambda}{\lambda^2} = \frac{1}{\lambda} \)
- \( M_X''(t) = \frac{2\lambda}{(\lambda - t)^3} \Rightarrow E[X^2] = M_X''(0) = \frac{2\lambda}{\lambda^3} = \frac{2}{\lambda^2} \)
- \( \text{Var}(X) = E[X^2] - (E[X])^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2} \)

---

### **Level 9: Combining Concepts (CDF, PDF, MGF)**
**Q9:** A CRV has CDF \( F(x) = 1 - e^{-x^2/2} \) for \( x \geq 0 \) (Rayleigh).
a) Find PDF \( f(x) \)
b) Find \( P(1 < X < 2) \)
c) Find MGF of \( Y = X^2 \)

**Solution:**
a) \( f(x) = \frac{d}{dx}F(x) = x e^{-x^2/2} \) for \( x \geq 0 \)
b) \( P(1 < X < 2) = F(2) - F(1) = (1 - e^{-2}) - (1 - e^{-0.5}) = e^{-0.5} - e^{-2} \approx 0.4712 \)
c) Find distribution of \( Y \):
- \( F_Y(y) = P(Y \leq y) = P(X^2 \leq y) = P(X \leq \sqrt{y}) = F_X(\sqrt{y}) = 1 - e^{-y/2} \)
- This is CDF of \( \text{Exp}(\lambda = 1/2) \)
- So \( Y \sim \text{Exp}(1/2) \Rightarrow M_Y(t) = \frac{1/2}{1/2 - t} = \frac{1}{1 - 2t} \) for \( t < 1/2 \)

---

### **Level 10: Proof using MGF**
**Q10:** Prove: If \( X \sim N(\mu_X, \sigma_X^2) \), \( Y \sim N(\mu_Y, \sigma_Y^2) \) are independent, then \( Z = aX + bY \sim N(\mu, \sigma^2) \). Find \( \mu, \sigma^2 \).

**Solution:**
- \( M_X(t) = \exp(\mu_X t + \frac{1}{2}\sigma_X^2 t^2) \), \( M_Y(t) = \exp(\mu_Y t + \frac{1}{2}\sigma_Y^2 t^2) \)
- Independence \( \Rightarrow M_Z(t) = M_X(at) \cdot M_Y(bt) \)
- \( M_Z(t) = \exp(a\mu_X t + \frac{1}{2}a^2\sigma_X^2 t^2) \cdot \exp(b\mu_Y t + \frac{1}{2}b^2\sigma_Y^2 t^2) = \exp[(a\mu_X + b\mu_Y)t + \frac{1}{2}(a^2\sigma_X^2 + b^2\sigma_Y^2)t^2] \)
- This is MGF of \( N(\mu, \sigma^2) \) where:
  - \( \mu = a\mu_X + b\mu_Y \)
  - \( \sigma^2 = a^2\sigma_X^2 + b^2\sigma_Y^2 \)

---

## **Part 2: Joint Probability and Distributions**

### **Core Concepts**

#### **1. Joint Probability Mass Function (Joint PMF)**
- \( p_{X,Y}(x, y) = P(X = x, Y = y) \)

#### **2. Marginal PMF**
- \( p_X(x) = \sum_{\text{all } y} p_{X,Y}(x, y) \)
- \( p_Y(y) = \sum_{\text{all } x} p_{X,Y}(x, y) \)

#### **3. Joint Probability Density Function (Joint PDF)**
- \( P((X, Y) \in R) = \iint_R f_{X,Y}(x, y)  dx  dy \)
- **Properties:**
  1. \( f_{X,Y}(x, y) \geq 0 \)
  2. \( \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y)  dx  dy = 1 \)

#### **4. Marginal PDF**
- \( f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y)  dy \)
- \( f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y)  dx \)

#### **5. Independent Random Variables**
- **Discrete:** \( p_{X,Y}(x, y) = p_X(x)p_Y(y) \)
- **Continuous:** \( f_{X,Y}(x, y) = f_X(x)f_Y(y) \)

#### **6. Conditional Distributions**
- **Discrete:** \( p_{X Y}(x y) = \frac{p_{X,Y}(x, y)}{p_Y(y)} \)
- **Continuous:** \( f_{X Y}(x y) = \frac{f_{X,Y}(x, y)}{f_Y(y)} \)

#### **7. Expected Value, Covariance, Correlation**
- **Expected Value:** \( E[g(X, Y)] = \sum_x \sum_y g(x, y)p_{X,Y}(x, y) \) or \( \iint g(x, y)f_{X,Y}(x, y)  dx  dy \)
- **Covariance:** \( \text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y] \)
- **Correlation:** \( \rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}} \), \( -1 \leq \rho \leq 1 \)

#### **8. Sum of Independent Random Variables**
- **MGF:** \( M_{X+Y}(t) = M_X(t)M_Y(t) \)
- **Mean/Variance:** \( E[X+Y] = E[X] + E[Y] \), \( \text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) \)

#### **9. Weak Law of Large Numbers (WLLN)**
For i.i.d. \( X_1, X_2, \dots, X_n \) with mean \( \mu \):
- \( \bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \)
- For any \( \epsilon > 0 \), \( \lim_{n \to \infty} P( \bar{X}_n - \mu  < \epsilon) = 1 \)

---

## **Questions: Joint Distributions**

### **Level 1: Joint PMF & Marginal PMF**
**Q1:** Joint PMF:
|       | Y=1 | Y=2 |
|-------|-----|-----|
| **X=1** | 0.2 | 0.3 |
| **X=2** | 0.1 | 0.4 |

a) Find marginal PMFs of X and Y
b) Are X and Y independent?

**Solution:**
a) 
- \( P(X=1) = 0.2 + 0.3 = 0.5 \), \( P(X=2) = 0.1 + 0.4 = 0.5 \)
- \( P(Y=1) = 0.2 + 0.1 = 0.3 \), \( P(Y=2) = 0.3 + 0.4 = 0.7 \)
b) Check: \( P(X=1, Y=1) = 0.2 \), \( P(X=1)P(Y=1) = 0.5 \times 0.3 = 0.15 \)
- Since \( 0.2 \neq 0.15 \) ⇒ **Not independent**

---

### **Level 2: Joint PDF & Marginal PDF**
**Q2:** Let \( f_{X,Y}(x, y) = cxy \) for \( 0 < x < 2, 0 < y < 1 \)
a) Find \( c \)
b) Find marginal PDF of X

**Solution:**
a) \( \int_{0}^{1} \int_{0}^{2} cxy  dx  dy = c \int_{0}^{1} y  dy \int_{0}^{2} x  dx = c \cdot \frac{1}{2} \cdot 2 = c = 1 \Rightarrow c = 1 \)
b) \( f_X(x) = \int_{0}^{1} xy  dy = x \int_{0}^{1} y  dy = x \cdot \frac{1}{2} = \frac{x}{2} \) for \( 0 < x < 2 \)

---

### **Level 3: Independence Check**
**Q3:** Are X and Y from Q2 independent?

**Solution:**
- From Q2: \( f_X(x) = \frac{x}{2} \), \( f_Y(y) = \int_{0}^{2} xy  dx = y \int_{0}^{2} x  dx = y \cdot 2 = 2y \)
- \( f_X(x)f_Y(y) = \frac{x}{2} \cdot 2y = xy = f_{X,Y}(x, y) \) ⇒ **Yes, independent**

---

### **Level 4: Conditional PDF**
**Q4:** For Q2, find \( f_{Y X}(y x) \)

**Solution:**
- \( f_{Y X}(y x) = \frac{f_{X,Y}(x, y)}{f_X(x)} = \frac{xy}{x/2} = 2y \) for \( 0 < y < 1 \)

---

### **Level 5: Covariance and Correlation (Discrete)**
**Q5:** For Q1's joint PMF, find \( \text{Cov}(X, Y) \) and \( \rho_{X,Y} \)

**Solution:**
- \( E[X] = 1 \times 0.5 + 2 \times 0.5 = 1.5 \)
- \( E[Y] = 1 \times 0.3 + 2 \times 0.7 = 1.7 \)
- \( E[XY] = (1)(1)(0.2) + (1)(2)(0.3) + (2)(1)(0.1) + (2)(2)(0.4) = 2.6 \)
- \( \text{Cov}(X, Y) = E[XY] - E[X]E[Y] = 2.6 - (1.5)(1.7) = 0.05 \)
- \( E[X^2] = 1^2 \times 0.5 + 2^2 \times 0.5 = 2.5 \Rightarrow \text{Var}(X) = 2.5 - 1.5^2 = 0.25 \)
- \( E[Y^2] = 1^2 \times 0.3 + 2^2 \times 0.7 = 3.1 \Rightarrow \text{Var}(Y) = 3.1 - 1.7^2 = 0.21 \)
- \( \rho_{X,Y} = \frac{0.05}{\sqrt{0.25 \times 0.21}} \approx \frac{0.05}{0.229} \approx 0.218 \)

---

### **Level 6: Covariance and Correlation (Continuous)**
**Q6:** Let \( f_{X,Y}(x, y) = x + y \) for \( 0 < x < 1, 0 < y < 1 \)
a) Find \( \text{Cov}(X, Y) \)
b) Are X and Y independent?

**Solution:**
a) 
- \( f_X(x) = \int_{0}^{1} (x+y)  dy = x + \frac{1}{2} \)
- \( f_Y(y) = \int_{0}^{1} (x+y)  dx = y + \frac{1}{2} \)
- \( E[X] = \int_{0}^{1} x(x + \frac{1}{2})  dx = \frac{1}{3} + \frac{1}{4} = \frac{7}{12} \), similarly \( E[Y] = \frac{7}{12} \)
- \( E[XY] = \int_{0}^{1} \int_{0}^{1} xy(x+y)  dx  dy = \int_{0}^{1} \left( \frac{y}{3} + \frac{y^2}{2} \right) dy = \frac{1}{6} + \frac{1}{6} = \frac{1}{3} \)
- \( \text{Cov}(X, Y) = \frac{1}{3} - \left( \frac{7}{12} \right)^2 = -\frac{1}{144} \)
b) \( f_X(x)f_Y(y) = (x + \frac{1}{2})(y + \frac{1}{2}) \neq x + y = f_{X,Y}(x, y) \) ⇒ **Not independent**

---

### **Level 7: Sum of Independent Random Variables (MGF Method)**
**Q7:** Let \( X \sim \text{Exp}(2) \), \( Y \sim \text{Exp}(3) \) be independent. Find distribution of \( Z = X + Y \) using MGFs.

**Solution:**
- \( M_X(t) = \frac{2}{2 - t} \), \( M_Y(t) = \frac{3}{3 - t} \)
- \( M_Z(t) = M_X(t)M_Y(t) = \frac{6}{(2-t)(3-t)} \)
- This is the MGF of the distribution (not a standard exponential)

---

### **Level 8: Conditional Expectation**
**Q8:** For Q6's joint PDF, find \( E[X  Y = 0.5] \)

**Solution:**
- $$( f_{X Y}(x y) = \frac{x + y}{y + \frac{1}{2}} \Rightarrow f_{X Y}(x 0.5) = \frac{x + 0.5}{1} = x + 0.5 )$$
- \( E[X  Y=0.5] = \int_{0}^{1} x(x + 0.5)  dx = \int_{0}^{1} (x^2 + 0.5x)  dx = \frac{1}{3} + \frac{1}{4} = \frac{7}{12} \)

---

### **Level 9: Application of WLLN**
**Q9:** A die is rolled 600 times. Estimate \( P(3.4 < \bar{X} < 3.6) \)

**Solution:**
- \( E[X_i] = \mu = 3.5 \), \( \text{Var}(X_i) = \frac{35}{12} \approx 2.9167 \), \( \sigma \approx 1.707 \)
- WLLN suggests sample mean ≈ population mean for large n
- Using CLT: \( P(3.4 < \bar{X} < 3.6) = P\left( \frac{-0.1}{1.707/\sqrt{600}} < Z < \frac{0.1}{1.707/\sqrt{600}} \right) \approx P(-1.434 < Z < 1.434) \approx 0.848 \)

---

### **Level 10: Proof involving Covariance and Sums**
**Q10:** Prove: \( \text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y) \)

**Solution:**
- \( \text{Var}(X+Y) = E[((X+Y) - E[X+Y])^2] = E[((X - \mu_X) + (Y - \mu_Y))^2] \)
- \( = E[(X - \mu_X)^2 + (Y - \mu_Y)^2 + 2(X - \mu_X)(Y - \mu_Y)] \)
- \( = E[(X - \mu_X)^2] + E[(Y - \mu_Y)^2] + 2E[(X - \mu_X)(Y - \mu_Y)] \)
- \( = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y) \)
- If independent: \( \text{Cov}(X, Y) = 0 \Rightarrow \text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) \)