# -*- coding: utf-8 -*-

"""Non-abundant sums."""
# https://projecteuler.net/problem=23

from app import Problem
from utils import get_proper_divisors


class Problem23(Problem):
    """Non-abundant sums."""

    def __init__(self):
        self.name = "problem 23"
        self.max = 28123

    def solve(self):
        abundants = []
        for value in xrange(1, self.max + 1):
            if sum(get_proper_divisors(value)) > value:
                abundants.append(value)
        non_abundants = set()
        for index, itemLeft in enumerate(abundants):
            if itemLeft >= self.max / 2:
                break
            for itemRight in abundants[index:]:
                value = itemLeft + itemRight
                if value > self.max:
                    break
                else:
                    non_abundants.add(value)
        all_sum = int(self.max * (self.max + 1) / 2)
        return all_sum - sum(non_abundants)


Problem23().run()
