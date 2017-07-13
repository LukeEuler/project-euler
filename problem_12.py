# -*- coding: utf-8 -*-

"""Highly divisible triangular number."""
# https://projecteuler.net/problem=12

from app import Problem
from utils import Prime


class Problem12(Problem):
    """Highly divisible triangular number."""

    def __init__(self):
        self.name = "problem 12"
        self.num = 500
        self.primes = []
        for prime in Prime():
            self.primes.append(prime)
            if len(self.primes) > 500:
                break

    def triangle(self, num):
        return int(num * (num + 1) / 2)

    def factorsNum(self, num):
        result = 1
        for prime in self.primes:
            if prime > num:
                break
            primeFactorsNum = 0
            while num % prime == 0:
                primeFactorsNum += 1
                num = int(num / prime)
            result *= (primeFactorsNum + 1)

        return result

    def solve(self):
        n = 1
        while True:
            triangle = self.triangle(n)
            result = self.factorsNum(triangle)
            if result > self.num:
                return triangle
            n += 1


Problem12().run()
