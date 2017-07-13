# -*- coding: utf-8 -*-

"""Power digit sum."""
# https://projecteuler.net/problem=16

from app import Problem


class Problem16(Problem):
    """Power digit sum."""

    def __init__(self):
        self.name = "problem 16"
        self.num = 2**1000

    def solve(self):
        return sum(map(int, str(self.num)))


Problem16().run()
