# -*- coding: utf-8 -*-

"""Largest prime factor."""
# https://projecteuler.net/problem=3

from app import Problem
from utils import Prime


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
