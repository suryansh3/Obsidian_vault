---
course: "Probability & Statistics"
semester: 3
tags:
  - course/probability-and-statistics
up: "[[Probability & Statistics]]"
---
Of course. This is an excellent request that covers the core discrete probability distributions. Let's break it down systematically.

### 1. Differentiation of Probability Distributions

The key to differentiating these distributions lies in understanding the **random experiment** they model. Each distribution answers a different question about a process involving independent or dependent trials with two outcomes (success/failure).

| Distribution          | Random Variable (X) = ...                                            | Key Characteristics                                                                                                                                                                                                   | Parameters                                                                      | MGF (Mₓ(t))                                                    |
| :-------------------- | :------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ | :------------------------------------------------------------- |
| **Binomial**          | Number of successes in `n` trials.                                   | 1. Fixed number of trials (`n`). <br> 2. Constant probability of success (`p`). <br> 3. Trials are **independent**. <br> 4. Sampling is **with replacement** (or from an infinite population).                        | `n` (number of trials) <br> `p` (probability of success)                        | $(1 - p + pe^t)^n$                                             |
| **Geometric**         | Number of trials **until the first success**.                        | 1. Tracks number of trials **until first success**. <br> 2. "Memoryless" property. <br> 3. Constant probability of success (`p`). <br> 4. Trials are **independent**.                                                 | `p` (probability of success)                                                    | $\frac{pe^t}{1 - (1-p)e^t}$ for $t < -\ln(1-p)$                |
| **Negative Binomial** | Number of trials **until the k-th success**.                         | 1. Generalized Geometric distribution. <br> 2. Tracks number of trials **until k-th success**. <br> 3. Constant probability of success (`p`). <br> 4. Trials are **independent**.                                     | `k` (number of successes) <br> `p` (probability of success)                     | $\left(\frac{pe^t}{1 - (1-p)e^t}\right)^k$ for $t < -\ln(1-p)$ |
| **Hypergeometric**    | Number of successes in `n` trials **from a finite population**.      | 1. Fixed number of trials (`n`). <br> 2. Population size is **finite (`N`)**. <br> 3. A fixed number of successes in population (`K`). <br> 4. Trials are **dependent**. <br> 5. Sampling is **without replacement**. | `N` (population size) <br> `K` (successes in population) <br> `n` (sample size) | (Complex, not usually defined via a simple MGF)                |
| **Poisson**           | Number of events occurring in a **fixed interval** of time or space. | 1. Events occur **independently**. <br> 2. The **average rate ($\lambda$)** is constant. <br> 3. The probability of >1 event in a very short interval is negligible.                                                  | $\lambda$ (average rate)                                                        | $e^{\lambda(e^t - 1)}$                                         |

---

### 2. Derivation of Mean and Variance using MGFs

The Moment Generating Function (MGF) is defined as $M_X(t) = E(e^{tX})$. The mean and variance are found by:
*   $E(X) = M'_X(0)$
*   $E(X^2) = M''_X(0)$
*   $Var(X) = E(X^2) - [E(X)]^2$

#### A. Binomial Distribution
*   **MGF:** $M_X(t) = (1 - p + pe^t)^n$
*   **First Derivative:** $M'_X(t) = n(1 - p + pe^t)^{n-1} \cdot pe^t$
*   **Mean:** $E(X) = M'_X(0) = n(1 - p + p)^{n-1} \cdot p = n(1)^{n-1} \cdot p = np$
*   **Second Derivative:** $M''_X(t) = n(n-1)(1 - p + pe^t)^{n-2} \cdot (pe^t)^2 + n(1 - p + pe^t)^{n-1} \cdot pe^t$
*   **$E(X^2)$:** $M''_X(0) = n(n-1)p^2 + np$
*   **Variance:** $Var(X) = E(X^2) - [E(X)]^2 = n(n-1)p^2 + np - (np)^2 = np(1-p)$

#### B. Geometric Distribution
*   **MGF:** $M_X(t) = \frac{pe^t}{1 - (1-p)e^t}$
*   **First Derivative:** $M'_X(t) = \frac{pe^t(1 - (1-p)e^t) - pe^t(-(1-p)e^t)}{(1 - (1-p)e^t)^2} = \frac{pe^t}{(1 - (1-p)e^t)^2}$
*   **Mean:** $E(X) = M'_X(0) = \frac{p}{(1 - (1-p))^2} = \frac{p}{p^2} = \frac{1}{p}$
*   **Second Derivative:** $M''_X(t) = \frac{pe^t(1 - (1-p)e^t)^2 + pe^t \cdot 2(1 - (1-p)e^t)(1-p)e^t}{(1 - (1-p)e^t)^4}$ (Using quotient/product rule). Simplifies to $M''_X(t) = \frac{pe^t(1 + (1-p)e^t)}{(1 - (1-p)e^t)^3}$
*   **$E(X^2)$:** $M''_X(0) = \frac{p(1 + (1-p))}{(1 - (1-p))^3} = \frac{p(2-p)}{p^3} = \frac{2-p}{p^2}$
*   **Variance:** $Var(X) = E(X^2) - [E(X)]^2 = \frac{2-p}{p^2} - (\frac{1}{p})^2 = \frac{2-p - 1}{p^2} = \frac{1-p}{p^2}$

#### C. Negative Binomial Distribution
*   **MGF:** $M_X(t) = \left(\frac{pe^t}{1 - (1-p)e^t}\right)^k$ (This is the MGF for a Geometric distribution raised to the `k`-th power, as X is the sum of `k` i.i.d. Geometric trials).
*   **Mean:** Since it's the sum of `k` independent Geometric R.V.s, $E(X) = k \cdot E(X_{\text{geom}}) = k \cdot \frac{1}{p}$
*   **Variance:** Similarly, $Var(X) = k \cdot Var(X_{\text{geom}}) = k \cdot \frac{1-p}{p^2}$

#### D. Poisson Distribution
*   **MGF:** $M_X(t) = e^{\lambda(e^t - 1)}$
*   **First Derivative:** $M'_X(t) = e^{\lambda(e^t - 1)} \cdot \lambda e^t$
*   **Mean:** $E(X) = M'_X(0) = e^{\lambda(1 - 1)} \cdot \lambda \cdot 1 = e^0 \cdot \lambda = \lambda$
*   **Second Derivative:** $M''_X(t) = \lambda e^t \cdot e^{\lambda(e^t - 1)} \cdot \lambda e^t + e^{\lambda(e^t - 1)} \cdot \lambda e^t = e^{\lambda(e^t - 1)} \lambda e^t (\lambda e^t + 1)$
*   **$E(X^2)$:** $M''_X(0) = e^0 \cdot \lambda \cdot 1 \cdot (\lambda \cdot 1 + 1) = \lambda(\lambda + 1)$
*   **Variance:** $Var(X) = E(X^2) - [E(X)]^2 = \lambda(\lambda + 1) - \lambda^2 = \lambda$

#### E. Hypergeometric Distribution
The Hypergeometric distribution does not have a simple, closed-form MGF that is practical for finding moments. The mean and variance are derived using combinatorial expectations
*   **Mean:** $E(X) = n \cdot \frac{K}{N}$ (Intuitive: sample size × probability of success in the population)
*   **Variance:** $Var(X) = n \frac{K}{N} \frac{N-K}{N} \frac{N-n}{N-1}$. Notice the extra factor $\frac{N-n}{N-1}$ compared to the Binomial variance. This is the **finite population correction factor**.

---

### 3. How to Analyze a Question and Choose the Distribution

Ask yourself these questions about the problem:

1.  **Is there a fixed number of trials (`n`)?**
    *   **No, we are waiting for success(es):** → Geometric or Negative Binomial.
        *   Waiting for the *first* success? → **Geometric**
        *   Waiting for the *k-th* success? → **Negative Binomial**
    *   **Yes, there is a fixed `n`:** → Binomial, Hypergeometric, or sometimes Poisson.

2.  **Are the trials independent and is the probability constant?**
    *   **Yes, `p` is constant and trials are independent:** → **Binomial** (or Geometric/NegBin if waiting).
    *   **No, because we are sampling without replacement from a small, finite population:** → **Hypergeometric**.

3.  **Is the problem about an event happening in time/space?**
    *   **Yes, and we are given an average rate ($\lambda$):** → **Poisson**.

**Decision Flowchart:**
```
Start -> Fixed number of trials (n)?
│
├─> No -> Waiting for k-th success? -> Yes -> Negative Binomial (k, p)
│                           │
│                           └─> No (just first) -> Geometric (p)
│
└─> Yes -> Sampling from a finite population without replacement? -> Yes -> Hypergeometric (N, K, n)
                           │
                           └─> No -> Is n large and p small? -> Sometimes approximated by Poisson (λ = np)
                                   │
                                   └─> No -> Binomial (n, p)
```

**Examples of Analyzing Questions:**
*   **"A coin is flipped 10 times. What's the probability of 4 heads?"**
    *   Fixed `n` (10), constant `p` (0.5), independent trials. → **Binomial**
*   **"A coin is flipped until the first head appears. What's the probability it takes 3 flips?"**
    *   No fixed `n`, waiting for first success. → **Geometric**
*   **"From a deck of 52 cards, 5 are drawn. What's the probability of 2 aces?"**
    *   Fixed `n` (5), but probability changes (no replacement), finite population (52). → **Hypergeometric**
*   **"A customer service center gets 5 calls per hour on average. What's the probability they get 2 calls in the next hour?"**
    *   Events in a fixed interval, average rate given. → **Poisson**
*   **"What is the probability it takes 15 rolls of a die to get 4 'sixes'?"**
    *   No fixed `n`, waiting for the *k-th* (4th) success. → **Negative Binomial**

---

### 4. Problems and Solutions (10 per Distribution)

#### Binomial Distribution (B(n, p))

1.  **(Difficulty: 2)** A fair coin is tossed 5 times. Find the probability of getting exactly 3 heads.
    *   **Solution:** $X \sim Bin(n=5, p=0.5)$. $P(X=3) = \binom{5}{3}(0.5)^3(0.5)^2 = 10 \cdot 0.125 \cdot 0.25 = 0.3125$

2.  **(Difficulty: 3)** A multiple-choice quiz has 10 questions, each with 4 choices. A student guesses randomly. What is the probability they get at least 7 correct?
    *   **Solution:** $X \sim Bin(n=10, p=0.25)$. $P(X \geq 7) = P(X=7)+P(X=8)+P(X=9)+P(X=10)$
        $= \binom{10}{7}(.25)^7(.75)^3 + \binom{10}{8}(.25)^8(.75)^2 + \binom{10}{9}(.25)^9(.75)^1 + \binom{10}{10}(.25)^{10} \approx 0.0035$

3.  **(Difficulty: 4)** In a certain town, 60% of adults have a driver's license. If 8 adults are randomly selected, what is the probability that more than 5 have a license?
    *   **Solution:** $X \sim Bin(n=8, p=0.6)$. $P(X > 5) = P(X=6)+P(X=7)+P(X=8)$
        $= \binom{8}{6}(.6)^6(.4)^2 + \binom{8}{7}(.6)^7(.4)^1 + \binom{8}{8}(.6)^8 \approx 0.3154$

4.  **(Difficulty: 5)** A machine produces items with a 5% defect rate. In a batch of 20 items, find the mean and standard deviation of the number of defective items.
    *   **Solution:** $X \sim Bin(n=20, p=0.05)$.
        Mean: $\mu = np = 20 \cdot 0.05 = 1$
        Variance: $\sigma^2 = np(1-p) = 20 \cdot 0.05 \cdot 0.95 = 0.95$
        Std Dev: $\sigma = \sqrt{0.95} \approx 0.975$

5.  **(Difficulty: 6)** The probability of a seed germinating is 0.8. If 10 seeds are planted, what is the probability that the number germinating is within one standard deviation of the mean?
    *   **Solution:** $X \sim Bin(n=10, p=0.8)$.
        Mean: $\mu = 10 \cdot 0.8 = 8$
        Std Dev: $\sigma = \sqrt{10 \cdot 0.8 \cdot 0.2} = \sqrt{1.6} \approx 1.265$
        Interval: $(8 - 1.265, 8 + 1.265) \approx (6.735, 9.265)$. So we need $P(7 \leq X \leq 9)$.
        $P(7 \leq X \leq 9) = P(X=7)+P(X=8)+P(X=9)$
        $= \binom{10}{7}(.8)^7(.2)^3 + \binom{10}{8}(.8)^8(.2)^2 + \binom{10}{9}(.8)^9(.2)^1 \approx 0.2013 + 0.3020 + 0.2684 = 0.7717$

6.  **(Difficulty: 7)** In a game, a player wins if they get at least 4 heads in 6 tosses of a fair coin. What is the probability of winning exactly 3 times in 5 games?
    *   **Solution:** First, find probability of winning *one* game ($p_{win}$).
        Let $Y \sim Bin(n=6, p=0.5)$. $p_{win} = P(Y \geq 4) = P(Y=4)+P(Y=5)+P(Y=6)$
        $= \binom{6}{4}(.5)^6 + \binom{6}{5}(.5)^6 + \binom{6}{6}(.5)^6 = (15+6+1)/64 = 22/64 = 11/32$
        Now, let $X$ be wins in 5 games. $X \sim Bin(n=5, p=11/32)$.
        $P(X=3) = \binom{5}{3}(\frac{11}{32})^3(\frac{21}{32})^2 \approx 0.1347$

7.  **(Difficulty: 8)** It is known that 2% of a company's widgets are defective. Using the binomial distribution and the Poisson approximation, find the probability that a box of 100 widgets contains more than 3 defectives. Compare the results.
    *   **Solution:**
        **Binomial:** $X \sim Bin(n=100, p=0.02)$. $P(X > 3) = 1 - P(X \leq 3)$.
        $P(X \leq 3) = \sum_{x=0}^{3} \binom{100}{x}(0.02)^x(0.98)^{100-x}$. This is tedious by hand.
        **Poisson Approximation:** $\lambda = np = 100 \cdot 0.02 = 2$.
        $Y \sim Poisson(\lambda=2)$. $P(Y > 3) = 1 - P(Y \leq 3) = 1 - [e^{-2}\frac{2^0}{0!} + e^{-2}\frac{2^1}{1!} + e^{-2}\frac{2^2}{2!} + e^{-2}\frac{2^3}{3!}]$
        $= 1 - e^{-2}[1 + 2 + 2 + 1.3333] \approx 1 - e^{-2}(6.3333) \approx 1 - (0.1353 \cdot 6.3333) \approx 1 - 0.857 = 0.143$
        The Binomial calculation (done via software) gives $P(X > 3) \approx 0.141$, showing the approximation is good.

8.  **(Difficulty: 9)** If $X_1 \sim Bin(n_1, p)$ and $X_2 \sim Bin(n_2, p)$ are independent, use MGFs to show that $Y = X_1 + X_2 \sim Bin(n_1 + n_2, p)$.
    *   **Solution:** $M_{X_1}(t) = (1-p+pe^t)^{n_1}$, $M_{X_2}(t) = (1-p+pe^t)^{n_2}$.
        $M_Y(t) = M_{X_1}(t) \cdot M_{X_2}(t) = (1-p+pe^t)^{n_1} \cdot (1-p+pe^t)^{n_2} = (1-p+pe^t)^{n_1+n_2}$
        This is the MGF of a $Bin(n_1+n_2, p)$ distribution. By uniqueness of MGFs, $Y \sim Bin(n_1+n_2, p)$.

9.  **(Difficulty: 9)** If $X \sim Bin(n, p)$, find $E\left(\frac{X}{n}\right)$ and $Var\left(\frac{X}{n}\right)$. ($\frac{X}{n}$ is the sample proportion).
    *   **Solution:** $E\left(\frac{X}{n}\right) = \frac{1}{n}E(X) = \frac{1}{n}(np) = p$
        $Var\left(\frac{X}{n}\right) = \frac{1}{n^2}Var(X) = \frac{1}{n^2}(np(1-p)) = \frac{p(1-p)}{n}$

10. **(Difficulty: 10)** Derive the recurrence relation $P(X = k+1) = \frac{p}{1-p} \cdot \frac{n-k}{k+1} \cdot P(X = k)$ for the Binomial distribution.
    *   **Solution:**
        $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$
        $P(X=k+1) = \binom{n}{k+1}p^{k+1}(1-p)^{n-k-1} = \frac{n!}{(k+1)!(n-k-1)!} p^{k+1}(1-p)^{n-k-1}$
        Now, $\frac{P(X=k+1)}{P(X=k)} = \frac{\frac{n!}{(k+1)!(n-k-1)!} p^{k+1}(1-p)^{n-k-1}}{\frac{n!}{k!(n-k)!} p^k(1-p)^{n-k}}$
        $= \frac{k!(n-k)!}{(k+1)!(n-k-1)!} \cdot \frac{p}{1-p}$
        $= \frac{(n-k)}{(k+1)} \cdot \frac{p}{1-p}$
        Therefore, $P(X=k+1) = \frac{p}{1-p} \cdot \frac{n-k}{k+1} \cdot P(X=k)$.

---

#### Geometric Distribution (Geom(p))

1.  **(Difficulty: 2)** The probability of a light bulb being defective is 0.1. What is the probability that the first defective bulb is the 5th one tested?
    *   **Solution:** $X \sim Geom(p=0.1)$. $P(X=5) = (1-p)^{5-1}p = (0.9)^4 \cdot (0.1) = 0.06561$

2.  **(Difficulty: 3)** A person rolls a fair die. What is the probability that the first '6' appears on the 3rd roll?
    *   **Solution:** $X \sim Geom(p=1/6)$. $P(X=3) = (5/6)^{2} \cdot (1/6) = (25/36) \cdot (1/6) = 25/216 \approx 0.1157$

3.  **(Difficulty: 4)** In a game, the chance of winning a prize is 0.05. What is the probability that you win your first prize on your 10th try?
    *   **Solution:** $X \sim Geom(p=0.05)$. $P(X=10) = (0.95)^9 \cdot (0.05) \approx 0.0315$

4.  **(Difficulty: 5)** What is the probability that it takes more than 7 trials to get the first success for an event with probability `p=0.2`?
    *   **Solution:** $P(X > 7) = (1-p)^7 = (0.8)^7 \approx 0.2097$

5.  **(Difficulty: 6)** Find the mean and variance of the number of rolls of a fair die needed to get the first '3'.
    *   **Solution:** $X \sim Geom(p=1/6)$.
        Mean: $E(X) = 1/p = 6$
        Variance: $Var(X) = (1-p)/p^2 = (5/6) / (1/36) = (5/6) \cdot 36 = 30$

6.  **(Difficulty: 7)** If the probability of a successful rocket launch is 0.9, what is the probability that the first failure occurs on the 4th launch or later?
    *   **Solution:** We want $P(X \geq 4)$ where $X$ is the trial of first failure. Here `p` (failure) = 0.1.
        $P(X \geq 4) = 1 - P(X \leq 3) = 1 - [P(X=1)+P(X=2)+P(X=3)]$
        $= 1 - [0.1 + (0.9)(0.1) + (0.9)^2(0.1)] = 1 - [0.1 + 0.09 + 0.081] = 1 - 0.271 = 0.729$
        Alternatively: $P(X \geq 4) = (1-p)^{3} = (0.9)^3 = 0.729$

7.  **(Difficulty: 8)** Prove the memoryless property: $P(X > s+t | X > s) = P(X > t)$ for a Geometric random variable.
    *   **Solution:**
        $P(X > s) = (1-p)^s$
        $P(X > s+t | X > s) = \frac{P(X > s+t \cap X > s)}{P(X > s)} = \frac{P(X > s+t)}{P(X > s)} = \frac{(1-p)^{s+t}}{(1-p)^s} = (1-p)^t = P(X > t)$

8.  **(Difficulty: 9)** The probability of a customer making a purchase is 0.3. What is the probability that the 5th customer is the first one to make a purchase today?
    *   **Solution:** This is a direct application. $X \sim Geom(p=0.3)$.
        $P(X=5) = (0.7)^4 \cdot (0.3) = 0.2401 \cdot 0.3 = 0.07203$

9.  **(Difficulty: 9)** If $X \sim Geom(p)$, find $E(2^X)$.
    *   **Solution:** This is $E(e^{X \ln 2}) = M_X(\ln 2)$.
        $M_X(t) = \frac{pe^t}{1-(1-p)e^t}$ for $t < -\ln(1-p)$.
        So $E(2^X) = M_X(\ln 2) = \frac{p \cdot 2}{1 - (1-p) \cdot 2} = \frac{2p}{1 - 2 + 2p} = \frac{2p}{2p - 1}$, provided $2p > 1$ ($p > 0.5$) for the denominator to be positive and the condition $t < -\ln(1-p)$ to hold.

10. **(Difficulty: 10)** You have two independent Geometric random variables, $X_1 \sim Geom(p)$ and $X_2 \sim Geom(p)$. Find $P(X_1 = X_2)$.
    *   **Solution:**
        $P(X_1 = X_2) = \sum_{k=1}^{\infty} P(X_1 = k, X_2 = k) = \sum_{k=1}^{\infty} [P(X=k)]^2$ (by independence)
        $= \sum_{k=1}^{\infty} [(1-p)^{k-1}p]^2 = p^2 \sum_{k=1}^{\infty} ((1-p)^2)^{k-1}$
        This is a geometric series with first term $a = 1$ and common ratio $r = (1-p)^2$.
        $= p^2 \cdot \frac{1}{1 - (1-p)^2} = p^2 \cdot \frac{1}{1 - (1 - 2p + p^2)} = p^2 \cdot \frac{1}{2p - p^2} = \frac{p^2}{p(2-p)} = \frac{p}{2-p}$

---

#### Hypergeometric Distribution (H(N, K, n))

1.  **(Difficulty: 2)** A class has 10 boys and 5 girls. If 3 students are selected at random without replacement, what is the probability that exactly 2 are boys?
    *   **Solution:** $X \sim H(N=15, K=10, n=3)$.
        $P(X=2) = \frac{\binom{10}{2}\binom{5}{1}}{\binom{15}{3}} = \frac{45 \cdot 5}{455} = \frac{225}{455} \approx 0.4945$

2.  **(Difficulty: 3)** A bag contains 8 red marbles and 4 blue marbles. 5 marbles are drawn without replacement. Find the probability of getting 3 red marbles.
    *   **Solution:** $X \sim H(N=12, K=8, n=5)$.
        $P(X=3) = \frac{\binom{8}{3}\binom{4}{2}}{\binom{12}{5}} = \frac{56 \cdot 6}{792} = \frac{336}{792} \approx 0.4242$

3.  **(Difficulty: 4)** From a standard deck of 52 cards, 7 cards are dealt. What is the probability of getting exactly 3 hearts?
    *   **Solution:** $X \sim H(N=52, K=13, n=7)$.
        $P(X=3) = \frac{\binom{13}{3}\binom{39}{4}}{\binom{52}{7}} \approx 0.301$

4.  **(Difficulty: 5)** A box of 20 items contains 6 defectives. A sample of 5 items is inspected. What is the mean and variance of the number of defectives in the sample?
    *   **Solution:** $X \sim H(N=20, K=6, n=5)$.
        Mean: $E(X) = n \cdot \frac{K}{N} = 5 \cdot \frac{6}{20} = 1.5$
        Variance: $Var(X) = n \frac{K}{N} \frac{N-K}{N} \frac{N-n}{N-1} = 5 \cdot \frac{6}{20} \cdot \frac{14}{20} \cdot \frac{15}{19} = 5 \cdot 0.3 \cdot 0.7 \cdot 0.7895 \approx 0.8289$

5.  **(Difficulty: 6)** A committee of 4 is to be chosen from 7 men and 5 women. What is the probability that the committee consists of at most 2 men?
    *   **Solution:** $X \sim H(N=12, K=7, n=4)$.
        $P(X \leq 2) = P(X=0) + P(X=1) + P(X=2)$
        $= \frac{\binom{7}{0}\binom{5}{4}}{\binom{12}{4}} + \frac{\binom{7}{1}\binom{5}{3}}{\binom{12}{4}} + \frac{\binom{7}{2}\binom{5}{2}}{\binom{12}{4}}$
        $= \frac{1 \cdot 5}{495} + \frac{7 \cdot 10}{495} + \frac{21 \cdot 10}{495} = \frac{5}{495} + \frac{70}{495} + \frac{210}{495} = \frac{285}{495} \approx 0.576$

6.  **(Difficulty: 7)** A batch of 100 chips contains 10 defective chips. If 10 chips are selected without replacement, approximate the probability of finding at most 1 defective chip using the Binomial approximation. Compare it to the exact Hypergeometric probability.
    *   **Solution:**
        **Hypergeometric (Exact):** $X \sim H(N=100, K=10, n=10)$.
        $P(X \leq 1) = P(X=0) + P(X=1) = \frac{\binom{10}{0}\binom{90}{10}}{\binom{100}{10}} + \frac{\binom{10}{1}\binom{90}{9}}{\binom{100}{10}} \approx 0.330 + 0.408 = 0.738$
        **Binomial Approximation:** $Y \sim Bin(n=10, p=K/N=0.1)$.
        $P(Y \leq 1) = P(Y=0) + P(Y=1) = (0.9)^{10} + \binom{10}{1}(0.1)^1(0.9)^9 \approx 0.3487 + 0.3874 = 0.7361$
        The approximation is very good because $n=10$ is small relative to $N=100$.

7.  **(Difficulty: 8)** In a lottery, 6 numbers are chosen from 49. To win a prize, you must match at least 3 numbers. Find the probability of winning a prize.
    *   **Solution:** Let $X$ be the number of matches. $X \sim H(N=49, K=6, n=6)$. We want $P(X \geq 3)$.
        $P(X \geq 3) = 1 - P(X \leq 2) = 1 - [P(X=0) + P(X=1) + P(X=2)]$
        $P(X=0) = \frac{\binom{6}{0}\binom{43}{6}}{\binom{49}{6}}$, $P(X=1) = \frac{\binom{6}{1}\binom{43}{5}}{\binom{49}{6}}$, $P(X=2) = \frac{\binom{6}{2}\binom{43}{4}}{\binom{49}{6}}$
        Calculating these gives $P(X \geq 3) \approx 1 - [0.436 + 0.413 + 0.132] \approx 0.019$ (About 1.9%)

8.  **(Difficulty: 9)** Derive the mean of the Hypergeometric distribution, $E(X) = n\frac{K}{N}$, using the indicator method. (Let $X_i = 1$ if the i-th draw is a success).
    *   **Solution:** Define $X_i = 1$ if the i-th item in the sample is a success (from the K group), 0 otherwise.
        Then $X = \sum_{i=1}^{n} X_i$.
        $P(X_i = 1) = \frac{K}{N}$ for any `i`. (The probability the first draw is a success is K/N. The probability the *second* draw is a success is *also* K/N: it's $\frac{K-1}{N-1} \cdot \frac{K}{N} + \frac{K}{N-1} \cdot \frac{N-K}{N} = \frac{K}{N}$.
        Therefore, $E(X_i) = 1 \cdot P(X_i=1) = \frac{K}{N}$.
        By linearity of expectation: $E(X) = E(\sum X_i) = \sum E(X_i) = n \cdot \frac{K}{N}$.

9.  **(Difficulty: 9)** A jar has 100 coins, some fair (50/50), some double-headed. There are 10 double-headed coins. You pick 5 coins at random. What is the probability that you get exactly 1 double-headed coin? If you then flip each of your 5 coins once, what is the probability of getting 5 heads?
    *   **Solution:**
        **Part 1:** $X \sim H(N=100, K=10, n=5)$. $P(X=1) = \frac{\binom{10}{1}\binom{90}{4}}{\binom{100}{5}}$
        **Part 2:** To get 5 heads, the double-headed coin(s) will always show heads. The fair coins show heads with probability 1/2.
        Let $Y$ be the number of double-headed coins in the sample.
        Case $Y=0$: Probability of 5 heads is $(1/2)^5 = 1/32$.
        Case $Y=1$: The one DH coin gives H. The other 4 fair coins must all show H: prob $(1/2)^4 = 1/16$.
        Case $Y \geq 2$: Any sample with 2 or more DH coins will definitely have at least 2 heads, but we need *all 5* to be heads. If there are, say, 2 DH coins, the other 3 fair coins must all show H: prob $(1/2)^3 = 1/8$. We need the full probability.
        The total probability is a weighted sum over all possible values of Y (0 to 5, but K=10 so max is 5):
        $P(\text{5 heads}) = \sum_{y=0}^{5} P(Y=y) \cdot P(\text{5 heads} | Y=y)$
        $P(\text{5 heads} | Y=y) = 1^y \cdot (1/2)^{5-y}$ (The `y` DH coins are always heads, the `5-y` fair coins must all be heads).
        So $P(\text{5 heads}) = \sum_{y=0}^{5} \frac{\binom{10}{y}\binom{90}{5-y}}{\binom{100}{5}} \cdot (1/2)^{5-y}$

10. **(Difficulty: 10)** Show that the variance of the Hypergeometric distribution is $Var(X) = n \frac{K}{N} \frac{N-K}{N} \frac{N-n}{N-1}$. (Hint: Use indicator variables and find $Cov(X_i, X_j)$).
    *   **Solution:** $X = \sum_{i=1}^n X_i$, so $Var(X) = \sum_{i=1}^n Var(X_i) + 2\sum_{i<j} Cov(X_i, X_j)$.
        We know $Var(X_i) = E(X_i^2) - [E(X_i)]^2 = \frac{K}{N} - (\frac{K}{N})^2 = \frac{K}{N}(1-\frac{K}{N})$.
        Now, find $Cov(X_i, X_j) = E(X_i X_j) - E(X_i)E(X_j)$ for $i \ne j$.
        $E(X_i X_j) = P(X_i=1, X_j=1) = P(\text{1st is success}) \cdot P(\text{2nd is success} | \text{1st is success}) = \frac{K}{N} \cdot \frac{K-1}{N-1}$.
        Therefore, $Cov(X_i, X_j) = \frac{K(K-1)}{N(N-1)} - (\frac{K}{N})^2 = \frac{K}{N} \left( \frac{K-1}{N-1} - \frac{K}{N} \right)$
        $= \frac{K}{N} \left( \frac{N(K-1) - K(N-1)}{N(N-1)} \right) = \frac{K}{N} \left( \frac{NK - N - KN + K}{N(N-1)} \right) = \frac{K}{N} \left( \frac{K - N}{N(N-1)} \right) = -\frac{K(N-K)}{N^2(N-1)}$.
        Now, plug into the variance formula:
        $Var(X) = n \cdot \frac{K}{N}(1-\frac{K}{N}) + 2\binom{n}{2} \cdot \left( -\frac{K(N-K)}{N^2(N-1)} \right)$
        $= n \frac{K}{N} \frac{N-K}{N} - n(n-1) \frac{K(N-K)}{N^2(N-1)}$
        $= \frac{nK(N-K)}{N^2} \left( 1 - \frac{n-1}{N-1} \right)$
        $= \frac{nK(N-K)}{N^2} \left( \frac{N-1 - (n-1)}{N-1} \right)$
        $= \frac{nK(N-K)}{N^2} \cdot \frac{N-n}{N-1}$
        $= n \frac{K}{N} \frac{N-K}{N} \frac{N-n}{N-1}$

---

#### Negative Binomial Distribution (NB(k, p))

1.  **(Difficulty: 2)** A coin is flipped until the 3rd head appears. What is the probability that the 3rd head occurs on the 5th flip?
    *   **Solution:** $X \sim NB(k=3, p=0.5)$. We need exactly `k=3` successes in `x=5` trials, with the last trial being a success.
        $P(X=5) = \binom{5-1}{3-1}p^3(1-p)^{5-3} = \binom{4}{2}(0.5)^5 = 6 \cdot \frac{1}{32} = \frac{6}{32} = 0.1875$

2.  **(Difficulty: 3)** A basketball player makes a free throw with probability 0.7. What is the probability that her 4th successful throw occurs on her 6th attempt?
    *   **Solution:** $X \sim NB(k=4, p=0.7)$.
        $P(X=6) = \binom{6-1}{4-1}(0.7)^4(0.3)^{6-4} = \binom{5}{3}(0.7)^4(0.3)^2 = 10 \cdot 0.2401 \cdot 0.09 = 0.21609$

3.  **(Difficulty: 4)** In a board game, you need to roll a '6' on a fair die three times to win. What is the probability that you win on your 8th roll?
    *   **Solution:** $X \sim NB(k=3, p=1/6)$.
        $P(X=8) = \binom{7}{2}(1/6)^3(5/6)^5 = 21 \cdot (1/216) \cdot (3125/7776) \approx 21 \cdot 0.00463 \cdot 0.4019 \approx 0.0391$

4.  **(Difficulty: 5)** Find the mean and variance of the number of trials needed to get the 5th success for an event with `p=0.4`.
    *   **Solution:** $X \sim NB(k=5, p=0.4)$.
        Mean: $E(X) = k/p = 5 / 0.4 = 12.5$
        Variance: $Var(X) = k(1-p)/p^2 = 5 \cdot 0.6 / (0.16) = 3 / 0.16 = 18.75$

5.  **(Difficulty: 6)** A researcher is interviewing people until they find 5 left-handed individuals. If the probability of being left-handed is 0.1, what is the probability that they will need to interview more than 30 people?
    *   **Solution:** $X \sim NB(k=5, p=0.1)$. We want $P(X > 30)$.
        It's easier to find the complement: $P(X > 30) = 1 - P(X \leq 30)$.
        $P(X \leq 30) = \sum_{x=5}^{30} \binom{x-1}{5-1}(0.1)^5(0.9)^{x-5}$. This requires computation (e.g., using software or a calculator with summation功能).
        Alternatively, we can use the fact that $P(X > 30) = P(\text{Fewer than 5 successes in 30 trials})$.
        Let $Y$ be the number of successes in 30 trials. $Y \sim Bin(n=30, p=0.1)$.
        $P(X > 30) = P(Y < 5) = P(Y \leq 4)$.
        $P(Y \leq 4) = \sum_{y=0}^{4} \binom{30}{y}(0.1)^y(0.9)^{30-y} \approx 0.824$ (from Binomial tables/calculator).
        So $P(X > 30) \approx 0.824$.

6.  **(Difficulty: 7)** If $X_1 \sim NB(k_1, p)$ and $X_2 \sim NB(k_2, p)$ are independent, find the distribution of $Y = X_1 + X_2$ using MGFs.
    *   **Solution:** $M_{X_1}(t) = \left(\frac{pe^t}{1-(1-p)e^t}\right)^{k_1}$, $M_{X_2}(t) = \left(\frac{pe^t}{1-(1-p)e^t}\right)^{k_2}$.
        $M_Y(t) = M_{X_1}(t) \cdot M_{X_2}(t) = \left(\frac{pe^t}{1-(1-p)e^t}\right)^{k_1 + k_2}$.
        This is the MGF of a $NB(k_1+k_2, p)$ distribution. So $Y \sim NB(k_1+k_2, p)$.

7.  **(Difficulty: 8)** Derive the mean of the Negative Binomial distribution using the MGF.
    *   **Solution:** $M_X(t) = \left(\frac{pe^t}{1-(1-p)e^t}\right)^k$
        Let $u = pe^t$ and $v = 1-(1-p)e^t$. Then $M_X(t) = (u/v)^k$.
        $M'_X(t) = k(u/v)^{k-1} \cdot \frac{u'v - uv'}{v^2}$ (Quotient rule within chain rule).
        $u' = pe^t$, $v' = -(1-p)e^t$.
        At $t=0$: $u=p$, $v=1-(1-p)=p$, $u'=p$, $v' = -(1-p)$.
        $M'_X(0) = k(p/p)^{k-1} \cdot \frac{(p)(p) - (p)(-(1-p))}{p^2} = k \cdot 1 \cdot \frac{p^2 + p(1-p)}{p^2} = k \cdot \frac{p^2 + p - p^2}{p^2} = k \cdot \frac{p}{p^2} = \frac{k}{p}$.

8.  **(Difficulty: 9)** The probability of a car passing a certain emissions test is 0.8. Cars are tested until 3 pass. What is the probability that the 3rd pass occurs on a trial number that is even?
    *   **Solution:** $X \sim NB(k=3, p=0.8)$. We want $P(X \text{ is even}) = P(X=2) + P(X=4) + P(X=6) + ...$
        $P(X=2) = \binom{1}{2}(0.8)^3(0.2)^{-1}$ -> This is 0 because you can't have 3 successes in 2 trials. So the smallest possible `x` is 3 (odd).
        $P(X=4) = \binom{3}{2}(0.8)^3(0.2)^1 = 3 \cdot 0.512 \cdot 0.2 = 0.3072$
        $P(X=6) = \binom{5}{2}(0.8)^3(0.2)^3 = 10 \cdot 0.512 \cdot 0.008 = 0.04096$
        $P(X=8) = \binom{7}{2}(0.8)^3(0.2)^5 = 21 \cdot 0.512 \cdot 0.00032 = 0.00344064$
        This is an infinite series: $S = 0.3072 + 0.04096 + 0.00344 + ...$
        This is a convergent series. The sum can be found exactly using generating functions, but the numerical sum is approximately $0.3516$.

9.  **(Difficulty: 9)** Find $E\left(\frac{1}{X}\right)$ for a Negative Binomial distribution. (This is challenging and may not have a closed form).
    *   **Solution:** $E\left(\frac{1}{X}\right) = \sum_{x=k}^{\infty} \frac{1}{x} \binom{x-1}{k-1}p^k(1-p)^{x-k}$.
        There is no simple closed-form expression for this expectation. It can be expressed in terms of hypergeometric functions or approximated.

10. **(Difficulty: 10)** Show that the Negative Binomial distribution can be derived as a Gamma-Poisson mixture. (If $X | \lambda \sim Poisson(\lambda)$ and $\lambda \sim Gamma(r, \beta)$ with mean $r\beta$, then the marginal distribution of $X$ is Negative Binomial).
    *   **Solution:** We need to find the marginal PMF $P(X=x)$.
        $P(X=x | \lambda) = \frac{e^{-\lambda} \lambda^x}{x!}$
        The PDF of $\lambda$ is $f(\lambda) = \frac{\lambda^{r-1} e^{-\lambda / \beta}}{\beta^r \Gamma(r)}$ for $\lambda > 0$.
        $P(X=x) = \int_{0}^{\infty} P(X=x | \lambda) f(\lambda) d\lambda = \int_{0}^{\infty} \frac{e^{-\lambda} \lambda^x}{x!} \cdot \frac{\lambda^{r-1} e^{-\lambda / \beta}}{\beta^r \Gamma(r)} d\lambda$
        $= \frac{1}{x! \beta^r \Gamma(r)} \int_{0}^{\infty} \lambda^{x + r - 1} e^{-\lambda(1 + 1/\beta)} d\lambda$
        Notice the integral is the kernel of a Gamma distribution with shape $a = x+r$ and rate $b = (1+1/\beta)$ (or scale $1/b$). So:
        $\int_{0}^{\infty} \lambda^{x+r-1} e^{-\lambda(1+1/\beta)} d\lambda = \frac{\Gamma(x+r)}{(1+1/\beta)^{x+r}}$
        Therefore, $P(X=x) = \frac{1}{x! \beta^r \Gamma(r)} \cdot \frac{\Gamma(x+r)}{(1+1/\beta)^{x+r}} = \frac{\Gamma(x+r)}{x! \Gamma(r)} \cdot \frac{1}{\beta^r (1+1/\beta)^{x+r}}$
        $= \binom{x+r-1}{x} \left( \frac{1/\beta}{1+1/\beta} \right)^r \left( \frac{1}{1+1/\beta} \right)^x$ (Using $\Gamma(x+r)/\Gamma(r) = (r)(r+1)...(r+x-1)$)
        Let $p = \frac{1/\beta}{1+1/\beta} = \frac{1}{1+\beta}$. Then $1-p = \frac{\beta}{1+\beta} = \frac{1}{1+1/\beta}$.
        So $P(X=x) = \binom{x+r-1}{x} p^r (1-p)^x$ for $x=0,1,2,...$.
        This is the PMF of a Negative Binomial distribution where `x` is the number of failures before the `r`-th success (a common alternative parameterization).

---

#### Poisson Distribution (Poi(λ))

1.  **(Difficulty: 2)** A call center receives an average of 2 calls per minute. What is the probability of receiving exactly 3 calls in a minute?
    *   **Solution:** $X \sim Poi(\lambda=2)$. $P(X=3) = \frac{e^{-2} 2^3}{3!} = \frac{0.1353 \cdot 8}{6} \approx 0.1804$

2.  **(Difficulty: 3)** Suppose flaws occur in a carpet at an average rate of 0.5 flaws per square meter. What is the probability of no flaws in 2 square meters?
    *   **Solution:** For 2 sq m, the average rate is $\lambda = 0.5 \cdot 2 = 1$.
        $X \sim Poi(\lambda=1)$. $P(X=0) = \frac{e^{-1} 1^0}{0!} = e^{-1} \approx 0.3679$

3.  **(Difficulty: 4)** On average, 3 students are late to a class each day. What is the probability that on a given day, more than 2 students are late?
    *   **Solution:** $X \sim Poi(\lambda=3)$. $P(X > 2) = 1 - P(X \leq 2) = 1 - [P(X=0)+P(X=1)+P(X=2)]$
        $= 1 - [\frac{e^{-3}3^0}{0!} + \frac{e^{-3}3^1}{1!} + \frac{e^{-3}3^2}{2!}] = 1 - e^{-3}[1 + 3 + 9/2] = 1 - e^{-3}(1+3+4.5) = 1 - (0.0498)(8.5) \approx 1 - 0.4232 = 0.5768$

4.  **(Difficulty: 5)** The number of accidents at a factory follows a Poisson distribution with a mean of 2.5 per week. Find the probability of exactly 4 accidents in a two-week period.
    *   **Solution:** For two weeks, $\lambda = 2.5 \cdot 2 = 5$.
        $X \sim Poi(\lambda=5)$. $P(X=4) = \frac{e^{-5} 5^4}{4!} = \frac{0.006738 \cdot 625}{24} \approx 0.1755$

5.  **(Difficulty: 6)** If $X \sim Poi(\lambda)$, find $E(X(X-1))$, and hence verify that $Var(X) = \lambda$.
    *   **Solution:** $E(X(X-1)) = \sum_{x=0}^{\infty} x(x-1) \frac{e^{-\lambda} \lambda^x}{x!} = \sum_{x=2}^{\infty} x(x-1) \frac{e^{-\lambda} \lambda^x}{x!}$ (terms 0 and 1 are 0).
        $= e^{-\lambda} \lambda^2 \sum_{x=2}^{\infty} \frac{\lambda^{x-2}}{(x-2)!}$. Let $y = x-2$.
        $= e^{-\lambda} \lambda^2 \sum_{y=0}^{\infty} \frac{\lambda^y}{y!} = e^{-\lambda} \lambda^2 \cdot e^{\lambda} = \lambda^2$.
        Now, $E(X(X-1)) = E(X^2 - X) = E(X^2) - E(X) = \lambda^2$.
        So $E(X^2) = \lambda^2 + \lambda$.
        Therefore, $Var(X) = E(X^2) - [E(X)]^2 = (\lambda^2 + \lambda) - \lambda^2 = \lambda$.

6.  **(Difficulty: 7)** If $X$ and $Y$ are independent Poisson random variables with parameters $\lambda_1$ and $\lambda_2$, show that the conditional distribution of $X$ given $X+Y=n$ is Binomial.
    *   **Solution:** Let $Z = X+Y$. $Z \sim Poi(\lambda_1 + \lambda_2)$.
        $P(X=k | X+Y=n) = \frac{P(X=k, Y=n-k)}{P(Z=n)} = \frac{P(X=k)P(Y=n-k)}{P(Z=n)}$ (by independence)
        $= \frac{ \frac{e^{-\lambda_1} \lambda_1^k}{k!} \cdot \frac{e^{-\lambda_2} \lambda_2^{n-k}}{(n-k)!} }{ \frac{e^{-(\lambda_1+\lambda_2)} (\lambda_1+\lambda_2)^n}{n!} }$
        $= \frac{n!}{k!(n-k)!} \cdot \frac{\lambda_1^k \lambda_2^{n-k}}{(\lambda_1+\lambda_2)^n}$
        $= \binom{n}{k} \left( \frac{\lambda_1}{\lambda_1+\lambda_2} \right)^k \left( \frac{\lambda_2}{\lambda_1+\lambda_2} \right)^{n-k}$
        This is the Binomial PMF with parameters $n$ and $p = \frac{\lambda_1}{\lambda_1+\lambda_2}$.

7.  **(Difficulty: 8)** The number of typographical errors on a page follows a Poisson distribution with a mean of 0.4. What is the probability that the 5th page is the first page to have at least one error?
    *   **Solution:** First, find the probability that a single page has at least one error.
        $P(\text{at least 1 error}) = 1 - P(\text{0 errors}) = 1 - e^{-0.4} \approx 1 - 0.6703 = 0.3297$
        Now, we want the first "success" (page with ≥1 error) to be on the 5th trial. This is Geometric.
        Let $Y \sim Geom(p=0.3297)$.
        $P(Y=5) = (1-p)^4 \cdot p = (0.6703)^4 \cdot (0.3297) \approx 0.202 \cdot 0.3297 \approx 0.0666$

8.  **(Difficulty: 9)** If $X \sim Poi(\lambda)$, find $E(e^X)$ and $E(2^X)$.
    *   **Solution:** $E(e^X) = E(e^{tX})|_{t=1} = M_X(1) = e^{\lambda(e^1 - 1)} = e^{\lambda(e-1)}$
        Similarly, $E(2^X) = E(e^{X \ln 2}) = M_X(\ln 2) = e^{\lambda(e^{\ln 2} - 1)} = e^{\lambda(2 - 1)} = e^{\lambda}$

9.  **(Difficulty: 9)** Customers arrive at a service station according to a Poisson process with rate 10 per hour. The service station opens at 9:00 am. What is the probability that the 2nd customer arrives before 9:20 am?
    *   **Solution:** The time between arrivals in a Poisson process is Exponential with parameter $\lambda=10$/hr, so mean $1/10$ hr = 6 mins.
        The time until the 2nd arrival, $T$, follows a Gamma (or Erlang) distribution with shape parameter $k=2$ and rate $\lambda=10$, or equivalently, a Negative Binomial for time.
        $P(T < 20/60 \text{ hr}) = P(T < 1/3 \text{ hr})$.
        $P(T \leq t) = 1 - \sum_{i=0}^{k-1} \frac{(\lambda t)^i e^{-\lambda t}}{i!}$ for a Gamma(k, $\lambda$) distribution.
        So $P(T < 1/3) = 1 - \sum_{i=0}^{1} \frac{(10/3)^i e^{-10/3}}{i!} = 1 - \left[ \frac{(10/3)^0 e^{-10/3}}{0!} + \frac{(10/3)^1 e^{-10/3}}{1!} \right]$
        $= 1 - e^{-10/3} \left[ 1 + 10/3 \right] = 1 - e^{-3.333}(1 + 3.333) = 1 - (0.0357)(4.333) \approx 1 - 0.1547 = 0.8453$
        Alternatively, this is the probability of having at least 2 arrivals by time $t=1/3$ hr.
        Let $N \sim Poi(\lambda t = 10/3 \approx 3.333)$.
        $P(N \geq 2) = 1 - P(N \leq 1) = 1 - [P(N=0)+P(N=1)] = 1 - [e^{-10/3} + (10/3)e^{-10/3}]$, which is the same as above.

10. **(Difficulty: 10)** Derive the Poisson distribution as a limit of the Binomial distribution. (Let $n \to \infty$ and $p \to 0$ such that $np \to \lambda$).
    *   **Solution:** Let $X_n \sim Bin(n, p)$ where $p = \lambda / n$.
        $P(X_n = k) = \binom{n}{k} p^k (1-p)^{n-k} = \frac{n!}{k!(n-k)!} \left( \frac{\lambda}{n} \right)^k \left( 1 - \frac{\lambda}{n} \right)^{n-k}$
        $= \frac{\lambda^k}{k!} \cdot \frac{n!}{(n-k)! n^k} \cdot \left( 1 - \frac{\lambda}{n} \right)^{n} \cdot \left( 1 - \frac{\lambda}{n} \right)^{-k}$
        Now, take the limit as $n \to \infty$:
        $\lim_{n \to \infty} \frac{n!}{(n-k)! n^k} = \lim_{n \to \infty} \frac{n(n-1)...(n-k+1)}{n^k} = 1$
        $\lim_{n \to \infty} \left( 1 - \frac{\lambda}{n} \right)^{n} = e^{-\lambda}$
        $\lim_{n \to \infty} \left( 1 - \frac{\lambda}{n} \right)^{-k} = 1$
        Therefore, $\lim_{n \to \infty} P(X_n = k) = \frac{\lambda^k}{k!} \cdot 1 \cdot e^{-\lambda} \cdot 1 = \frac{e^{-\lambda} \lambda^k}{k!}$, which is the Poisson PMF.


Links : [[probabilty]] [[probability_and_statistics]] [[psmidsem]] [[midsem2025_autumn]]

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Probability & Statistics]] · **Semester:** [[Semester 3]] · **Map:** [[MOC]]
> **Prev:** - · **Next:** [[04 - Academics & CS/Semester 3/Probability & Statistics/PMF and CMF interconvertibility|PMF and CMF interconvertibility]]
> **Related:** [[IPA]] · [[AI & ML Roadmap]] · [[Discrete Mathematics]]
<!-- connections:end -->
