# Project Euler - Problem 53 - Combinatoric Selections
There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, <img src="https://render.githubusercontent.com/render/math?math={5 \choose 3} = 10">.

In general, <img src="https://render.githubusercontent.com/render/math?math={n \choose r} = \frac{n!}{r!(n-r)!}">, where <img src="https://render.githubusercontent.com/render/math?math=r \leq n">, <img src="https://render.githubusercontent.com/render/math?math=n! = n \times (n-1) \times \dots \times 3 \times 2 \times 1">, and <img src="https://render.githubusercontent.com/render/math?math=0! = 1">.

It is not until <img src="https://render.githubusercontent.com/render/math?math=n = 23">, that a value exceeds one-million: <img src="https://render.githubusercontent.com/render/math?math={23 \choose 10} = 1144066">.

How many, not necessarily distinct, values of <img src="https://render.githubusercontent.com/render/math?math={n \choose r}"> for <img src="https://render.githubusercontent.com/render/math?math=1 \leq n \leq 100">, are greater than one-million?
