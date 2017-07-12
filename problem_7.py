# -*- coding: utf-8 -*-

"""10001st prime."""
# https://projecteuler.net/problem=6

from app import Problem
from utils import Prime


class Problem7(Problem):
    """10001st prime."""

    def __init__(self):
        self.name = "problem 7"
        self.num = 10001

    def solve(self):
        index = 1
        for prime in Prime():
            if index == self.num:
                return prime
            index += 1


Problem7().run()
