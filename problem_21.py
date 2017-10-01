# -*- coding: utf-8 -*-

"""Amicable numbers."""
# https://projecteuler.net/problem=21

from app import Problem
from utils import get_proper_divisors


class Problem21(Problem):
    """Amicable numbers."""

    def __init__(self):
        self.name = "problem 21"
        self.num = 10000

    def solve(self):
        result = 0
        for value in xrange(1, self.num):
            anotherValue = sum(get_proper_divisors(value))
            if value == anotherValue:
                continue
            if value == sum(get_proper_divisors(anotherValue)):
                result += value
        return result


Problem21().run()
