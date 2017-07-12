# -*- coding: utf-8 -*-

"""Even Fibonacci numbers."""
# https://projecteuler.net/problem=2

from app import Problem
from utils import Fibonacci


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
