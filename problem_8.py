# -*- coding: utf-8 -*-

"""Largest product in a series."""
# https://projecteuler.net/problem=8

from app import Problem


class Problem8(Problem):
    """Largest product in a series."""

    def __init__(self):
        self.name = "problem 8"
        self.length = 13
        f = open("problem_8.txt")
        self.numbers = []
        line = f.readline()
        while line:
            self.numbers.extend([int(x) for x in line.strip('\n')])
            line = f.readline()
        f.close()

    def solve(self):
        result = 0
        for index in xrange(len(self.numbers) - self.length):
            product = 1
            for i in range(self.length):
                product *= self.numbers[index + i]
            result = max(product, result)
        return result


Problem8().run()
