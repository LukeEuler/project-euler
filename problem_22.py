# -*- coding: utf-8 -*-

"""Names scores."""
# https://projecteuler.net/problem=22

from app import Problem


class Problem22(Problem):
    """Names scores."""

    def __init__(self):
        self.name = "problem 22"
        file = open("problem_22.txt")
        line = file.readline()
        file.close()
        self.names = [item.strip('"') for item in line.split(",")]
        self.names.sort()

    def solve(self):
        result = 0
        for index, item in enumerate(self.names):
            value = sum([ord(c) - 64 for c in item])
            result += value * (index + 1)
        return result


Problem22().run()
