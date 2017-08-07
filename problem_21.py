# -*- coding: utf-8 -*-

"""Amicable numbers."""
# https://projecteuler.net/problem=21

from app import Problem
from utils import getProperDivisors


class Problem21(Problem):
    """Amicable numbers."""

    def __init__(self):
        self.name = "problem 21"
        self.num = 10000

    def solve(self):
        result = 0
        for value in xrange(1, self.num):
            anotherValue = sum(getProperDivisors(value))
            if value == anotherValue:
                continue
            if value == sum(getProperDivisors(anotherValue)):
                result += value
        return result


Problem21().run()
