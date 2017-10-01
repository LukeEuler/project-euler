# -*- coding: utf-8 -*-

"""Lattice paths."""
# https://projecteuler.net/problem=15

from app import Problem
from utils import combinatorial_number


class Problem15(Problem):
    """Lattice paths."""

    def __init__(self):
        self.name = "problem 15"
        self.num = 20

    def solve(self):
        return combinatorial_number(2 * self.num, self.num)


Problem15().run()
