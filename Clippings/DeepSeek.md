---
title: DeepSeek
source: https://chat.deepseek.com/a/chat/s/0be013b8-25fb-4fb4-b816-6a78c482bf37
author:
published:
created: 2025-11-15
description: Chat with DeepSeek AI – your intelligent assistant for coding, content creation, file reading, and more. Upload documents, engage in long-context conversations, and get expert help in AI, natural language processing, and beyond. | 深度求索（DeepSeek）助力编程代码开发、创意写作、文件处理等任务，支持文件上传及长文本对话，随时为您提供高效的AI支持。
tags:
  - clippings
  - "#probabilty"
  - probability_and_statistics
---

**Note on Conventions:**

- **Geometric Distribution:** This table uses the definition "number of trials *until* the first success" (support: $x = 1, 2, 3, ...$ ). The "number of failures *before* the first success" (support: $x = 0, 1, 2, ...$ ) is an alternative parameterization with a different mean and PMF.
- **Normal CDF:** The CDF of the Normal distribution has no closed form and is expressed in terms of the standard normal CDF, $\Phi$ , which is widely tabulated and available in software.

### Summary of Common Probability Distributions

| Distribution                                        | PMF (for discrete) / PDF (for continuous)                                                                         | CDF (or CMF for discrete)                                                                  | Mean                | Variance                                   |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------- | ------------------------------------------ |
| **Binomial**   $X \sim \text{Bin}(n, p)$            | $P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}$   for $x = 0, 1, ..., n$                                                  | $F(x) = \sum_{k=0}^{\lfloor x \rfloor} \binom{n}{k} p^k (1-p)^{n-k}$                       | $np$                | $np(1-p)$                                  |
| **Geometric**   $X \sim \text{Geom}(p)$             | $P(X=x) = (1-p)^{x-1} p$   for $x = 1, 2, 3, ...$                                                                 | $F(x) = 1 - (1-p)^{\lfloor x \rfloor}$                                                     | $\frac{1}{p}$       | $\frac{1-p}{p^2}$                          |
| **Negative Binomial**   $X \sim \text{NB}(r, p)$    | $P(X=x) = \binom{x-1}{r-1} (1-p)^{x-r} p^r$   for $x = r, r+1, ...$                                               | $F(x) = \sum_{k=r}^{\lfloor x \rfloor} \binom{k-1}{r-1} (1-p)^{k-r} p^r$                   | $\frac{r}{p}$       | $\frac{r(1-p)}{p^2}$                       |
| **Hypergeometric**   $X \sim \text{HGeom}(N, K, n)$ | $P(X=x) = \frac{\binom{K}{x} \binom{N-K}{n-x}}{\binom{N}{n}}$   for $x = \max(0, n+K-N)$ to $\min(n, K)$          | $F(x) = \sum_{k=0}^{\lfloor x \rfloor} \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}$ | $n\frac{K}{N}$      | $n\frac{K}{N}\frac{N-K}{N}\frac{N-n}{N-1}$ |
| **Poisson**   $X \sim \text{Poi}(\lambda)$          | $P(X=x) = \frac{e^{-\lambda} \lambda^x}{x!}$   for $x = 0, 1, 2, ...$                                             | $F(x) = e^{-\lambda} \sum_{k=0}^{\lfloor x \rfloor} \frac{\lambda^k}{k!}$                  | $\lambda$           | $\lambda$                                  |
| **Uniform (Continuous)**   $X \sim U(a, b)$         | $f(x) = \frac{1}{b-a}$   for $a \le x \le b$                                                                      | $F(x) = \frac{x-a}{b-a}$   for $a \le x \le b$                                             | $\frac{a+b}{2}$     | $\frac{(b-a)^2}{12}$                       |
| **Exponential**   $X \sim \text{Exp}(\lambda)$      | $f(x) = \lambda e^{-\lambda x}$   for $x \ge 0, \lambda > 0$                                                      | $F(x) = 1 - e^{-\lambda x}$   for $x \ge 0$                                                | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$                      |
| **Normal (Gaussian)**   $X \sim N(\mu, \sigma^2)$   | $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$   for $x \in \mathbb{R}$ | $F(x) = \Phi\left(\frac{x-\mu}{\sigma}\right)$   where $\Phi$ is the std. normal CDF       | $\mu$               | $\sigma^2$                                 |

---

### Key and Parameter Definitions

- **$n$** (Binomial): Number of trials.
- **$p$**: Probability of success.
- **$r$** (Negative Binomial): Number of successes until stopping.
- **$N$** (Hypergeometric): Population size.
- **$K$** (Hypergeometric): Number of success states in the population.
- **$\lambda$**: Rate parameter (Poisson, Exponential).
- **$a, b$**: Lower and upper bounds of the uniform distribution.
- **$\mu, \sigma^2$**: Mean and variance of the normal distribution.
- **$\lfloor x \rfloor$**: The floor function, denoting the greatest integer less than or equal to $x$ .
- **$\binom{n}{k}$**: The binomial coefficient, "n choose k".

AI-generated, for reference only