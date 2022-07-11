# Project Euler

## Problem 53 - Combinatoric Selections

There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, $\displaystyle\binom{5}{3} = 10$.

In general, $\displaystyle\binom{n}{r} = \displaystyle\frac{n!}{r! (n-r)!}$, where $r \leq n$, $n! = n \times (n-1) \times \dots \times 3 \times 2 \times 1$, and $0! = 1$.

It is not until $n = 23$,
that a value exceeds one-million: $\displaystyle\binom{23}{10} = 1144066$.

How many, not necessarily distinct, values of $\displaystyle\binom{n}{r}$ for $1 \leq n \leq 100$, are greater than one-miliion?
