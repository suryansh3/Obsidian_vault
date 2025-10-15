Of course. This is a comprehensive list of topics in probability and statistics. I will explain each topic in detail, followed by a structured set of examples and questions ranging from Level 1 (easiest) to Level 10 (most difficult).

### **Part 1: Continuous Random Variables & Specific Distributions**

---

#### **1. Continuous Random Variable (CRV)**
A continuous random variable is a variable that can take on an infinite number of values within a given range. Unlike discrete random variables, the probability that a CRV equals any single, exact value is zero. We describe probabilities over intervals.

*   **Example:** The height of a randomly selected person, the time until a radioactive atom decays, the volume of water in a reservoir.

#### **2. Probability Density Function (PDF) - f(x)**
The PDF, denoted as \( f(x) \), describes the relative likelihood for a CRV to take on a given value. The probability is found by calculating the *area under the PDF curve* over an interval.

**Properties:**
1.  \( f(x) \geq 0 \) for all \( x \).
2.  The total area under the curve is 1: \( \int_{-\infty}^{\infty} f(x) \, dx = 1 \).
3.  \( P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx \).

#### **3. Cumulative Distribution Function (CDF) - F(x)**
The CDF, \( F(x) \), gives the probability that the random variable \( X \) is less than or equal to \( x \).
\[ F(x) = P(X \leq x) = \int_{-\infty}^{x} f(t) \, dt \]

**Properties:**
*   \( F(x) \) is a non-decreasing function.
*   \( \lim_{x \to -\infty} F(x) = 0 \)
*   \( \lim_{x \to \infty} F(x) = 1 \)
*   \( P(a < X \leq b) = F(b) - F(a) \)

#### **4. Moment Generating Function (MGF) - M_X(t)**
The MGF is a powerful alternative way to characterize a probability distribution. It "generates" the moments (mean, variance, etc.) of the distribution.
\[ M_X(t) = E[e^{tX}] \]
For a CRV: \( M_X(t) = \int_{-\infty}^{\infty} e^{tx} f(x) \, dx \)

**Why it's useful:**
*   \( E[X^n] = M_X^{(n)}(0) \) (the n-th derivative of the MGF evaluated at t=0 gives the n-th moment).
*   If two random variables have the same MGF, they have the same distribution.
*   It simplifies finding the distribution of sums of independent random variables.

---

#### **Uniform Distribution**
A distribution where all intervals of the same length have equal probability.

*   **Notation:** \( X \sim \text{Uniform}(a, b) \)
*   **PDF:** \( f(x) = \frac{1}{b-a} \) for \( a \leq x \leq b \), and 0 otherwise.
*   **CDF:** \( F(x) = \frac{x-a}{b-a} \) for \( a \leq x \leq b \).
*   **Mean:** \( E[X] = \frac{a+b}{2} \)
*   **Variance:** \( Var(X) = \frac{(b-a)^2}{12} \)

#### **Normal Distribution (Gaussian Distribution)**
The most important continuous distribution, characterized by its bell-shaped curve.

*   **Notation:** \( X \sim N(\mu, \sigma^2) \)
*   **PDF:** \( f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} \)
*   **Parameters:** \( \mu \) (mean, center of the curve), \( \sigma \) (standard deviation, spread of the curve).
*   **Standard Normal Distribution:** \( Z \sim N(0, 1) \) with \( \mu=0 \), \( \sigma=1 \). Its CDF is denoted by \( \Phi(z) \).

#### **Mean, Variance, Percentile, and Critical Value of Normal Distribution**
*   **Mean (\( \mu \)):** The center of the distribution.
*   **Variance (\( \sigma^2 \)):** The spread. About 68% of data lies within \( \mu \pm \sigma \), 95% within \( \mu \pm 2\sigma \), and 99.7% within \( \mu \pm 3\sigma \).
*   **Percentile:** The value below which a given percentage of observations fall. The \( p \)-th percentile \( x_p \) satisfies \( P(X \leq x_p) = p \). For the standard normal, \( z_p = \Phi^{-1}(p) \).
*   **Critical Value (\( z_{\alpha} \)):** The value on the standard normal curve such that the area to its right is \( \alpha \). So, \( P(Z > z_{\alpha}) = \alpha \). Commonly used in hypothesis testing (e.g., \( z_{0.05} = 1.645 \)).

#### **Normal Approximation of the Binomial Distribution**
When the number of trials \( n \) in a binomial distribution \( Bin(n, p) \) is large, and \( p \) is not too close to 0 or 1, it can be approximated by a normal distribution \( N(\mu, \sigma^2) \) where \( \mu = np \) and \( \sigma^2 = np(1-p) \).

A **continuity correction** is applied for better accuracy:
\[ P(X \leq k) \approx P\left(Z \leq \frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right) \]

#### **Exponential Distribution**
Models the time between events in a Poisson process (events occurring continuously and independently at a constant average rate).

*   **Notation:** \( X \sim \text{Exp}(\lambda) \)
*   **PDF:** \( f(x) = \lambda e^{-\lambda x} \) for \( x \geq 0 \)
*   **CDF:** \( F(x) = 1 - e^{-\lambda x} \) for \( x \geq 0 \)
*   **Mean:** \( E[X] = \frac{1}{\lambda} \)
*   **Variance:** \( Var(X) = \frac{1}{\lambda^2} \)
*   **Memoryless Property:** \( P(X > s + t | X > s) = P(X > t) \)

---

### **Questions: Continuous Random Variables & Distributions**

#### **Level 1: Basic Definition & Application**
**Q1:** The time (in minutes) a customer spends in a shop is modeled by a CRV X with PDF \( f(x) = \frac{x}{8} \) for \( 0 \leq x \leq 4 \). Is this a valid PDF? Find the probability a customer spends less than 2 minutes.

**Solution:**
1.  Check validity: \( \int_{0}^{4} \frac{x}{8} \, dx = \frac{1}{8} \cdot \frac{x^2}{2} \Big|_{0}^{4} = \frac{1}{16} (16 - 0) = 1 \). Yes, it's valid.
2.  \( P(X < 2) = \int_{0}^{2} \frac{x}{8} \, dx = \frac{1}{8} \cdot \frac{x^2}{2} \Big|_{0}^{2} = \frac{1}{16} (4) = 0.25 \).

#### **Level 2: Using the CDF**
**Q2:** For the same CRV in Q1, find its CDF, \( F(x) \). Use it to find \( P(1 < X < 3) \).

**Solution:**
1.  \( F(x) = \int_{0}^{x} \frac{t}{8} \, dt = \frac{t^2}{16} \Big|_{0}^{x} = \frac{x^2}{16} \) for \( 0 \leq x \leq 4 \).
2.  \( P(1 < X < 3) = F(3) - F(1) = \frac{9}{16} - \frac{1}{16} = \frac{8}{16} = 0.5 \).

#### **Level 3: Uniform Distribution**
**Q3:** A bus arrives every 15 minutes at a stop. What is the probability that a person arriving randomly at the stop will wait more than 10 minutes?

**Solution:**
Let \( X \sim \text{Uniform}(0, 15) \). We need \( P(X > 10) \).
Using PDF: \( P(X > 10) = \int_{10}^{15} \frac{1}{15} \, dx = \frac{5}{15} = \frac{1}{3} \).
Using CDF: \( P(X > 10) = 1 - F(10) = 1 - \frac{10}{15} = \frac{1}{3} \).

#### **Level 4: Exponential Distribution & Memoryless Property**
**Q4:** The lifetime of a lightbulb (in hours) follows an exponential distribution with a mean of 1000 hours. What is the probability it lasts more than 1500 hours? If it has already lasted 1000 hours, what is the probability it lasts another 500 hours?

**Solution:**
Mean \( E[X] = 1/\lambda = 1000 \), so \( \lambda = 0.001 \).
1.  \( P(X > 1500) = 1 - F(1500) = e^{-0.001 \times 1500} = e^{-1.5} \approx 0.223 \).
2.  By the memoryless property: \( P(X > 1500 | X > 1000) = P(X > 500) = e^{-0.001 \times 500} = e^{-0.5} \approx 0.606 \).

#### **Level 5: Normal Distribution - Basic Calculation**
**Q5:** Test scores are normally distributed with a mean of 75 and a standard deviation of 10. What percentage of students scored above 90?

**Solution:**
\( X \sim N(75, 10^2) \). \( P(X > 90) = P\left(Z > \frac{90-75}{10}\right) = P(Z > 1.5) = 1 - \Phi(1.5) \approx 1 - 0.9332 = 0.0668 \) or 6.68%.

#### **Level 6: Normal Distribution - Percentiles**
**Q6:** For the test scores in Q5, what score is the 95th percentile? (i.e., the score that 95% of students scored below).

**Solution:**
We need \( x \) such that \( P(X < x) = 0.95 \).
First, find the z-score for the 95th percentile: \( z = \Phi^{-1}(0.95) \approx 1.645 \).
Now, convert back to X: \( x = \mu + z\sigma = 75 + 1.645 \times 10 = 91.45 \). So, a score of about 91.45.

#### **Level 7: Normal Approximation to Binomial**
**Q7:** A fair coin is tossed 400 times. Use the normal approximation to estimate the probability of getting between 185 and 210 heads (inclusive).

**Solution:**
\( n=400, p=0.5 \). \( \mu = np = 200 \), \( \sigma = \sqrt{np(1-p)} = \sqrt{100} = 10 \).
We want \( P(185 \leq X \leq 210) \). Using continuity correction: \( P(184.5 \leq X \leq 210.5) \).
Convert to Z: \( Z_{lower} = \frac{184.5 - 200}{10} = -1.55 \), \( Z_{upper} = \frac{210.5 - 200}{10} = 1.05 \).
\( P(-1.55 \leq Z \leq 1.05) = \Phi(1.05) - \Phi(-1.55) = \Phi(1.05) - (1 - \Phi(1.55)) \).
\( \approx 0.8531 - (1 - 0.9394) = 0.8531 - 0.0606 = 0.7925 \).

#### **Level 8: Moment Generating Function**
**Q8:** Find the MGF for \( X \sim \text{Exp}(\lambda) \). Use it to find the mean and variance of X.

**Solution:**
\( M_X(t) = E[e^{tX}] = \int_{0}^{\infty} e^{tx} \lambda e^{-\lambda x} dx = \lambda \int_{0}^{\infty} e^{-(\lambda - t)x} dx \).
This integral converges only if \( t < \lambda \). It evaluates to \( \frac{\lambda}{\lambda - t} \).
So, \( M_X(t) = \frac{\lambda}{\lambda - t} \) for \( t < \lambda \).
*   **Mean:** \( M'_X(t) = \frac{\lambda}{(\lambda - t)^2} \). \( E[X] = M'_X(0) = \frac{\lambda}{\lambda^2} = \frac{1}{\lambda} \).
*   **Variance:** \( E[X^2] = M''_X(t) = \frac{2\lambda}{(\lambda - t)^3} \). \( M''_X(0) = \frac{2\lambda}{\lambda^3} = \frac{2}{\lambda^2} \).
    \( Var(X) = E[X^2] - (E[X])^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2} \).

#### **Level 9: Combining Concepts (CDF, PDF, MGF)**
**Q9:** A CRV X has CDF \( F(x) = 1 - e^{-x^2/2} \) for \( x \geq 0 \). (This is a Rayleigh distribution).
a) Find its PDF, \( f(x) \).
b) Find \( P(1 < X < 2) \).
c) Find the MGF of \( Y = X^2 \). (Hint: What is the distribution of Y?)

**Solution:**
a) \( f(x) = \frac{d}{dx}F(x) = \frac{d}{dx}(1 - e^{-x^2/2}) = x e^{-x^2/2} \) for \( x \geq 0 \).
b) \( P(1 < X < 2) = F(2) - F(1) = (1 - e^{-2}) - (1 - e^{-0.5}) = e^{-0.5} - e^{-2} \approx 0.6065 - 0.1353 = 0.4712 \).
c) Let \( Y = X^2 \). Let's find the CDF of Y.
    \( F_Y(y) = P(Y \leq y) = P(X^2 \leq y) = P(X \leq \sqrt{y}) = F_X(\sqrt{y}) = 1 - e^{-y/2} \) for \( y \geq 0 \).
    This is the CDF of an Exponential distribution with \( \lambda = 1/2 \). So, \( Y \sim \text{Exp}(1/2) \).
    From Q8, the MGF for \( Exp(\lambda) \) is \( \frac{\lambda}{\lambda - t} \). Thus, \( M_Y(t) = \frac{1/2}{1/2 - t} = \frac{1}{1 - 2t} \) for \( t < 1/2 \).

#### **Level 10: Proof using MGF**
**Q10:** Prove that if \( X \sim N(\mu_X, \sigma_X^2) \) and \( Y \sim N(\mu_Y, \sigma_Y^2) \) are independent, then \( Z = aX + bY \) is also normally distributed, and find its mean and variance. (Use the MGF uniqueness property).

**Solution:**
The MGF of a normal \( X \) is \( M_X(t) = \exp(\mu_X t + \frac{1}{2}\sigma_X^2 t^2) \).
Since X and Y are independent, \( M_{aX+bY}(t) = M_X(at) \cdot M_Y(bt) \).
\( M_X(at) = \exp(\mu_X (at) + \frac{1}{2}\sigma_X^2 (at)^2) = \exp(a\mu_X t + \frac{1}{2}a^2\sigma_X^2 t^2) \).
\( M_Y(bt) = \exp(b\mu_Y t + \frac{1}{2}b^2\sigma_Y^2 t^2) \).
Therefore, \( M_Z(t) = \exp(a\mu_X t + b\mu_Y t + \frac{1}{2}(a^2\sigma_X^2 + b^2\sigma_Y^2) t^2) \).
This is of the form \( \exp(\mu t + \frac{1}{2}\sigma^2 t^2) \), which is the MGF of a \( N(\mu, \sigma^2) \) random variable.
By the uniqueness property of MGFs, \( Z \sim N(\mu, \sigma^2) \) where:
*   \( \mu = a\mu_X + b\mu_Y \)
*   \( \sigma^2 = a^2\sigma_X^2 + b^2\sigma_Y^2 \)

---

### **Part 2: Joint Probability and Distributions**

---

#### **1. Joint Probability Mass Function (Joint PMF)**
For two discrete random variables X and Y, the joint PMF gives the probability that X takes a specific value x and Y takes a specific value y simultaneously.
\[ p_{X,Y}(x, y) = P(X = x, Y = y) \]

#### **2. Marginal Probability Mass Function**
The individual PMF of X or Y, found by summing the joint PMF over all possible values of the other variable.
\[ p_X(x) = \sum_{\text{all } y} p_{X,Y}(x, y) \]
\[ p_Y(y) = \sum_{\text{all } x} p_{X,Y}(x, y) \]

#### **3. Joint Probability Density Function (Joint PDF)**
For two continuous random variables X and Y, the joint PDF \( f_{X,Y}(x, y) \) is a function such that the probability that (X, Y) lies in a region R is the double integral over R.
\[ P((X, Y) \in R) = \iint_R f_{X,Y}(x, y) \, dx \, dy \]

**Properties:**
1.  \( f_{X,Y}(x, y) \geq 0 \)
2.  \( \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx \, dy = 1 \)

#### **4. Marginal Probability Density Function**
The individual PDF of X or Y, found by integrating the joint PDF over all possible values of the other variable.
\[ f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy \]
\[ f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx \]

#### **5. Independent Random Variables**
X and Y are independent if knowing the value of one provides no information about the other.
*   **Discrete:** \( P(X=x, Y=y) = P(X=x)P(Y=y) \) for all x, y. (Joint PMF = product of marginals).
*   **Continuous:** \( f_{X,Y}(x, y) = f_X(x) f_Y(y) \) for all x, y. (Joint PDF = product of marginals).

#### **6. Conditional Probability Mass/ Density Function**
The distribution of one variable given the value of the other.
*   **Discrete (Conditional PMF):** \( p_{X|Y}(x|y) = \frac{p_{X,Y}(x, y)}{p_Y(y)} \), provided \( p_Y(y) > 0 \).
*   **Continuous (Conditional PDF):** \( f_{X|Y}(x|y) = \frac{f_{X,Y}(x, y)}{f_Y(y)} \), provided \( f_Y(y) > 0 \).

#### **7. Expected Value, Covariance, and Correlation**
*   **Expected Value:** For a function \( g(X, Y) \), \( E[g(X, Y)] = \sum_x \sum_y g(x, y) p_{X,Y}(x, y) \) (discrete) or \( \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) f_{X,Y}(x, y) \, dx \, dy \) (continuous).
*   **Covariance:** Measures the direction of the linear relationship between two variables.
    \( Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y] \).
*   **Correlation (\( \rho \)):** A standardized measure of the linear relationship.
    \( \rho_{X,Y} = \frac{Cov(X, Y)}{\sqrt{Var(X)Var(Y)}} \). \( -1 \leq \rho \leq 1 \).

**Note:** If X and Y are independent, then \( Cov(X, Y) = 0 \) and \( \rho = 0 \). However, the converse is not always true.

#### **8. Sum of Two Independent Random Variables**
If \( Z = X + Y \) and X and Y are independent, then:
*   **PMF/PDF:** The distribution of Z is the convolution of the distributions of X and Y.
*   **MGF:** \( M_Z(t) = M_X(t) \cdot M_Y(t) \). This is often the easiest method.
*   **Mean and Variance:** \( E[Z] = E[X] + E[Y] \), \( Var(Z) = Var(X) + Var(Y) \).

#### **9. Weak Law of Large Numbers (WLLN)**
Let \( X_1, X_2, ..., X_n \) be a sequence of independent and identically distributed (i.i.d.) random variables with finite mean \( \mu \). The sample mean is \( \bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i \).
The WLLN states that as \( n \) becomes very large, the sample mean converges in probability to the population mean. Formally:
For any \( \epsilon > 0 \), \( \lim_{n \to \infty} P(|\bar{X}_n - \mu| < \epsilon) = 1 \).
In simpler terms: As the sample size increases, the average of the observed values gets closer to the expected value.

---

### **Questions: Joint Distributions**

#### **Level 1: Joint PMF & Marginal PMF**
**Q1:** The joint PMF of random variables X and Y is given by:
|   | Y=1 | Y=2 |
|---|---|---|
| X=1 | 0.2 | 0.3 |
| X=2 | 0.1 | 0.4 |
a) Find the marginal PMF of X and Y.
b) Are X and Y independent?

**Solution:**
a) \( P(X=1) = 0.2 + 0.3 = 0.5 \), \( P(X=2) = 0.1 + 0.4 = 0.5 \).
    \( P(Y=1) = 0.2 + 0.1 = 0.3 \), \( P(Y=2) = 0.3 + 0.4 = 0.7 \).
b) Check for (X=1, Y=1): \( P(X=1, Y=1) = 0.2 \). \( P(X=1)P(Y=1) = 0.5 \times 0.3 = 0.15 \).
    Since \( 0.2 \neq 0.15 \), X and Y are **not** independent.

#### **Level 2: Joint PDF & Marginal PDF**
**Q2:** Let the joint PDF of X and Y be \( f_{X,Y}(x, y) = cxy \) for \( 0 < x < 2, 0 < y < 1 \).
a) Find the constant c.
b) Find the marginal PDF of X.

**Solution:**
a) \( \int_{0}^{1} \int_{0}^{2} cxy \, dx \, dy = 1 \).
    \( \int_{0}^{1} \left[ c \frac{x^2}{2} y \right]_{0}^{2} dy = \int_{0}^{1} \left[ c \cdot 2 y \right] dy = 2c \int_{0}^{1} y \, dy = 2c \cdot \frac{1}{2} = c \).
    So, \( c = 1 \).
b) \( f_X(x) = \int_{0}^{1} 1 \cdot x y \, dy = x \int_{0}^{1} y \, dy = x \cdot \frac{1}{2} = \frac{x}{2} \) for \( 0 < x < 2 \).

#### **Level 3: Independence Check**
**Q3:** Are the random variables X and Y from Q2 independent? Justify.

**Solution:**
From Q2: \( f_X(x) = x/2 \), \( f_Y(y) = \int_{0}^{2} 1 \cdot x y \, dx = y \int_{0}^{2} x \, dx = y \cdot 2 = 2y \).
Now, \( f_X(x)f_Y(y) = (x/2)(2y) = xy \).
This is exactly the joint PDF \( f_{X,Y}(x, y) \). Therefore, **yes, X and Y are independent**.

#### **Level 4: Conditional PDF**
**Q4:** For the joint PDF in Q2, find the conditional PDF \( f_{Y|X}(y|x) \).

**Solution:**
\( f_{Y|X}(y|x) = \frac{f_{X,Y}(x, y)}{f_X(x)} = \frac{xy}{x/2} = 2y \) for \( 0 < y < 1 \).
Notice that this does not depend on x, which is consistent with the independence we found in Q3.

#### **Level 5: Covariance and Correlation (Discrete)**
**Q5:** For the joint PMF in Q1, calculate \( Cov(X, Y) \) and \( \rho_{X,Y} \).

**Solution:**
First, find \( E[X] = 1*0.5 + 2*0.5 = 1.5 \). \( E[Y] = 1*0.3 + 2*0.7 = 1.7 \).
Now, find \( E[XY] = \sum_x \sum_y xy \cdot p(x, y) \).
= (1)(1)(0.2) + (1)(2)(0.3) + (2)(1)(0.1) + (2)(2)(0.4) = 0.2 + 0.6 + 0.2 + 1.6 = 2.6.
So, \( Cov(X, Y) = E[XY] - E[X]E[Y] = 2.6 - (1.5)(1.7) = 2.6 - 2.55 = 0.05 \).
Now, find variances: \( E[X^2] = 1^2*0.5 + 2^2*0.5 = 0.5 + 2 = 2.5 \). \( Var(X) = 2.5 - (1.5)^2 = 0.25 \).
\( E[Y^2] = 1^2*0.3 + 2^2*0.7 = 0.3 + 2.8 = 3.1 \). \( Var(Y) = 3.1 - (1.7)^2 = 3.1 - 2.89 = 0.21 \).
Thus, \( \rho_{X,Y} = \frac{0.05}{\sqrt{0.25 \cdot 0.21}} = \frac{0.05}{\sqrt{0.0525}} \approx \frac{0.05}{0.229} \approx 0.218 \).

#### **Level 6: Covariance and Correlation (Continuous)**
**Q6:** Let X and Y have joint PDF \( f_{X,Y}(x, y) = x + y \) for \( 0 < x < 1, 0 < y < 1 \).
a) Find \( Cov(X, Y) \).
b) Are X and Y independent?

**Solution:**
a) First, find marginals.
    \( f_X(x) = \int_{0}^{1} (x+y) dy = [xy + y^2/2]_{0}^{1} = x + 1/2 \).
    Similarly, \( f_Y(y) = y + 1/2 \).
    \( E[X] = \int_{0}^{1} x f_X(x) dx = \int_{0}^{1} x(x + 1/2) dx = \int_{0}^{1} (x^2 + x/2) dx = [x^3/3 + x^2/4]_{0}^{1} = 1/3 + 1/4 = 7/12 \). Similarly \( E[Y] = 7/12 \).
    \( E[XY] = \int_{0}^{1} \int_{0}^{1} xy(x+y) dx dy = \int_{0}^{1} \int_{0}^{1} (x^2y + xy^2) dx dy \).
    = \( \int_{0}^{1} [\frac{x^3}{3}y + \frac{x^2}{2}y^2]_{0}^{1} dy = \int_{0}^{1} (\frac{y}{3} + \frac{y^2}{2}) dy = [\frac{y^2}{6} + \frac{y^3}{6}]_{0}^{1} = 1/6 + 1/6 = 1/3 \).
    So, \( Cov(X, Y) = E[XY] - E[X]E[Y] = 1/3 - (7/12)(7/12) = 1/3 - 49/144 = 48/144 - 49/144 = -1/144 \).
b) Check independence: \( f_X(x)f_Y(y) = (x + 1/2)(y + 1/2) \). This is NOT equal to the joint PDF \( x + y \). Therefore, they are **not independent**.

#### **Level 7: Sum of Independent Random Variables (MGF Method)**
**Q7:** Let \( X \sim \text{Exp}(\lambda=2) \) and \( Y \sim \text{Exp}(\lambda=3) \) be independent. Find the distribution of \( Z = X + Y \) using MGFs.

**Solution:**
From earlier, MGF of \( Exp(\lambda) \) is \( \frac{\lambda}{\lambda - t} \).
So, \( M_X(t) = \frac{2}{2 - t} \), \( M_Y(t) = \frac{3}{3 - t} \).
Since X and Y are independent, \( M_Z(t) = M_X(t) M_Y(t) = \frac{2}{2-t} \cdot \frac{3}{3-t} = \frac{6}{(2-t)(3-t)} \).
This is not the MGF of a common distribution like Exponential. We can find the PDF via convolution, but the MGF uniquely defines the distribution.

#### **Level 8: Conditional Expectation**
**Q8:** For the joint PDF in Q6, find \( E[X | Y = 0.5] \).

**Solution:**
First, find the conditional PDF \( f_{X|Y}(x|y) = \frac{f_{X,Y}(x, y)}{f_Y(y)} = \frac{x + y}{y + 1/2} \).
So, \( f_{X|Y}(x|0.5) = \frac{x + 0.5}{0.5 + 0.5} = \frac{x + 0.5}{1} = x + 0.5 \) for \( 0 < x < 1 \).
Now, \( E[X | Y=0.5] = \int_{0}^{1} x \cdot f_{X|Y}(x|0.5) dx = \int_{0}^{1} x (x + 0.5) dx = \int_{0}^{1} (x^2 + 0.5x) dx \).
= \( [x^3/3 + 0.5 \cdot x^2/2]_{0}^{1} = [1/3 + 1/4] = 7/12 \).

#### **Level 9: Application of WLLN**
**Q9:** A die is rolled 600 times. Use the WLLN to estimate the probability that the average of the rolls lies between 3.4 and 3.6.

**Solution:**
Let \( X_i \) be the outcome of the i-th roll. \( E[X_i] = \mu = (1+2+3+4+5+6)/6 = 3.5 \).
The sample mean is \( \bar{X}_{600} \). The WLLN says \( \bar{X}_n \) will be close to 3.5 for large n.
We want \( P(3.4 < \bar{X}_{600} < 3.6) \). While the WLLN is a limit law, for a large n=600, we can use the Central Limit Theorem (a stronger result) to approximate this.
\( Var(X_i) = E[X^2] - \mu^2 = (91/6) - (3.5)^2 = 15.1667 - 12.25 = 2.9167 \). \( \sigma \approx 1.707 \).
\( P(3.4 < \bar{X} < 3.6) = P\left( \frac{3.4-3.5}{1.707/\sqrt{600}} < Z < \frac{3.6-3.5}{1.707/\sqrt{600}} \right) = P\left( \frac{-0.1}{0.0697} < Z < \frac{0.1}{0.0697} \right) \approx P(-1.434 < Z < 1.434) \).
\( \approx \Phi(1.434) - \Phi(-1.434) \approx 0.924 - 0.076 = 0.848 \).
The WLLN assures us this probability is high.

#### **Level 10: Proof involving Covariance and Sums**
**Q10:** Prove that for any two random variables X and Y, \( Var(X+Y) = Var(X) + Var(Y) + 2Cov(X, Y) \). Hence, what is \( Var(X+Y) \) if X and Y are independent?

**Solution:**
Start with the definition: \( Var(X+Y) = E[((X+Y) - E[X+Y])^2] = E[( (X - \mu_X) + (Y - \mu_Y) )^2] \).
Expand the square: \( = E[(X - \mu_X)^2 + (Y - \mu_Y)^2 + 2(X - \mu_X)(Y - \mu_Y)] \).
By linearity of expectation: \( = E[(X - \mu_X)^2] + E[(Y - \mu_Y)^2] + 2E[(X - \mu_X)(Y - \mu_Y)] \).
This is equal to \( Var(X) + Var(Y) + 2Cov(X, Y) \). Q.E.D.

If X and Y are independent, then \( Cov(X, Y) = 0 \), and thus \( Var(X+Y) = Var(X) + Var(Y) \).