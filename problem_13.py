# -*- coding: utf-8 -*-

"""Large sum."""
# https://projecteuler.net/problem=13

from app import Problem


class Problem13(Problem):
    """Large sum."""

    def __init__(self):
        self.name = "problem 13"
        f = open("problem_13.txt")
        line = f.readline()
        self.nums = []
        while line:
            self.nums.append(int(line.strip('\n')))
            line = f.readline()
        f.close()

    def solve(self):
        result = 0
        for num in self.nums:
            result += num
        return str(result)[:10]


Problem13().run()
