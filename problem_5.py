# -*- coding: utf-8 -*-

"""Smallest multiple."""
# https://projecteuler.net/problem=5

from app import Problem
from utils import lcm


class Problem5(Problem):
    """Smallest multiple."""

    def __init__(self):
        self.name = "problem 5"
        self.num = 20

    def solve(self):
        result = 1
        for value in xrange(2, self.num):
            result = lcm(result, value)
        return result


Problem5().run()
