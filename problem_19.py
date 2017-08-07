# -*- coding: utf-8 -*-

"""Counting Sundays."""
# https://projecteuler.net/problem=19

from app import Problem
from utils import isLeapYear


class Problem19(Problem):
    """Counting Sundays."""

    def __init__(self):
        self.name = "problem 19"
        self.first = 1900
        self.firstMod = 1
        self.start = 1901
        self.end = 2000
        self.month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def solve(self):
        sum = 0
        mod = self.firstMod
        for year in xrange(self.first, self.end + 1):
            if isLeapYear(year):
                self.month[1] = 29
            for m in self.month:
                mod = (mod + m) % 7
                if year >= self.start and mod == 0:
                    sum += 1
            self.month[1] = 28
        if mod % 7 == 0:
            sum -= 1
        return sum


Problem19().run()
