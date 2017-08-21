# -*- coding: utf-8 -*-

"""Non-abundant sums."""
# https://projecteuler.net/problem=23

from app import Problem
from utils import getProperDivisors


class Problem23(Problem):
    """Non-abundant sums."""

    def __init__(self):
        self.name = "problem 23"
        self.max = 28123

    def solve(self):
        abundants = []
        for value in xrange(1, self.max + 1):
            if sum(getProperDivisors(value)) > value:
                abundants.append(value)
        nonAbundants = set()
        for index, itemLeft in enumerate(abundants):
            if itemLeft >= self.max / 2:
                break
            for itemRight in abundants[index:]:
                value = itemLeft + itemRight
                if value > self.max:
                    break
                else:
                    nonAbundants.add(value)
        allSum = int(self.max * (self.max + 1) / 2)
        return allSum - sum(nonAbundants)


Problem23().run()
