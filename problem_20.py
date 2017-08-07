# -*- coding: utf-8 -*-

"""Factorial digit sum."""
# https://projecteuler.net/problem=20

from app import Problem
from utils import factorial


class Problem20(Problem):
    """Factorial digit sum."""

    def __init__(self):
        self.name = "problem 20"
        self.num = 100

    def solve(self):
        sum = 0
        strValue = str(factorial(self.num))
        for item in strValue:
            sum += int(item)
        return sum


Problem20().run()
