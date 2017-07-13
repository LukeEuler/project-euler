# -*- coding: utf-8 -*-

"""Summation of primes."""
# https://projecteuler.net/problem=10

from app import Problem
from utils import Prime


class Problem10(Problem):
    """Summation of primes."""

    def __init__(self):
        self.name = "problem 10"
        self.num = 2000000

    def solve(self):
        result = 0
        for prime in Prime():
            if prime > self.num:
                return result
            result += prime


Problem10().run()
