---
Title: Binomial Theorem
Date: 2023-04-27 17:45
Category: maths
Tags: maths
Summary: A brief overview of the binomial theorem.
Status: published
---

Below is the binomial theorem:

$$(a + b)^{n} = \sum_{k = 0}^{n} \binom{n}{k} a^{n - k}b^{k}$$

The notation $\binom{n}{k}$ means, "The number of ways to choose $k$ elements from a set containing $n$ elements in total." This can also be expressed algebraically as:

$$\binom{n}{k} = \frac{n!}{k!(n - k)!}$$

The pattern of coefficients associated with each term after expanding $(a + b)^{n}$ follows the pattern observed in **Pascal's Triangle**. Indeed, the triangle can be formed using $\binom{n}{k}$, where $n$ represents the **row** of the triangle and $k$ represents the **term** within that row. Numbering of rows and terms begins at 0, so the triangle is formed as follows:

$$
\binom{0}{0} \\
\binom{1}{0} \binom{1}{1} \\
\binom{2}{0} \binom{2}{1} \binom{2}{2} \\
\binom{3}{0} \binom{3}{1} \binom{3}{2} \binom{3}{3} \\
\binom{4}{0} \binom{4}{1} \binom{4}{2} \binom{4}{3} \binom{4}{4}
$$

And so on.
