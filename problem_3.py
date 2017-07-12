# -*- coding: utf-8 -*-

"""Largest prime factor."""
# https://projecteuler.net/problem=3

from app import Problem


class Prime:
    """generate primes."""

    def __init__(self):
        self.primes = [2]

    def __iter__(self):
        return self

    def next(self):
        nextNum = self.primes[-1] + self.primes[-1] % 2 + 1
        while True:
            for prime in self.primes:
                if nextNum % prime == 0:
                    break
            else:
                self.primes.append(nextNum)
                return self.primes[-2]
            nextNum += 2


class Problem3(Problem):
    """Largest prime factor."""

    def __init__(self):
        self.name = "problem 3"
        self.num = 600851475143

    def solve(self):
        # self.num = 600851475143
        factor = []
        for prime in Prime():
            while self.num % prime == 0:
                factor.append(prime)
                self.num = int(self.num / prime)
            if self.num == 1 or self.num < prime:
                break

        return factor[-1]


Problem3().run()
