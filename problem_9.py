# -*- coding: utf-8 -*-

"""Special Pythagorean triplet."""
# https://projecteuler.net/problem=9

from app import Problem


class Problem9(Problem):
    """Special Pythagorean triplet."""

    def __init__(self):
        self.name = "problem 9"

    def solve(self):
        for c in xrange(499, 1, -1):
            for a in xrange(1, c - 1):
                b = 1000 - c - a
                if a > b:
                    break
                if (c ** 2 - a ** 2 - b ** 2) == 0:
                    return a * b * c
        return 0


Problem9().run()
