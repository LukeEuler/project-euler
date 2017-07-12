# -*- coding: utf-8 -*-

"""Even Fibonacci numbers."""
# https://projecteuler.net/problem=2


class Fibonacci:
    """generator fibnacci numbers ."""

    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


sum = 0
fibs = Fibonacci()
for num in fibs:
    if num > 4000000:
        break
    if num % 2 == 0:
        sum += num

print sum
