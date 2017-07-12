# -*- coding: utf-8 -*-

"""Sum square difference."""
# https://projecteuler.net/problem=6

from app import Problem


class Problem6(Problem):
    """Sum square difference."""

    def __init__(self):
        self.name = "problem 6"
        self.num = 100

    def solve(self):
        squareSum, sumSquare = 0, 0
        for value in xrange(1, self.num + 1):
            squareSum += value**2
            sumSquare += value
        sumSquare = sumSquare**2
        return sumSquare - squareSum


Problem6().run()
