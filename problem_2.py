# -*- coding: utf-8 -*-

"""Even Fibonacci numbers."""
# https://projecteuler.net/problem=2

from app import Problem


class Fibonacci:
    """generate fibnacci numbers."""

    def __init__(self):
        """Fibonacci begins with 1, 1."""
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


class Problem2(Problem):
    """Even Fibonacci numbers."""

    def __init__(self):
        self.name = "problem 2"

    def solve(self):
        sum = 0
        fibs = Fibonacci()
        for num in fibs:
            if num > 4000000:
                break
            if num % 2 == 0:
                sum += num

        return sum


Problem2().run()
