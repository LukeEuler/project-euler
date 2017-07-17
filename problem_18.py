# -*- coding: utf-8 -*-

"""Maximum path sum deepth."""
# https://projecteuler.net/problem=18

from app import Problem


class Problem18(Problem):
    """Maximum path sum deepth."""

    def __init__(self):
        self.name = "problem 18"
        file = open("problem_18.txt")
        self.triangle = []
        line = file.readline()
        while line:
            self.triangle.append([int(item)
                                  for item in line.strip('\n').split()])
            line = file.readline()
        file.close()

    def solve(self):
        maxDeepth = len(self.triangle)
        for deepth in range(1, maxDeepth):
            for i in range(1, len(self.triangle[deepth]) - 1):
                self.triangle[deepth][i] = max(
                    self.triangle[deepth - 1][i - 1],
                    self.triangle[deepth - 1][i]) + self.triangle[deepth][i]
            self.triangle[deepth][0] += self.triangle[deepth - 1][0]
            self.triangle[deepth][-1] += self.triangle[deepth - 1][-1]
        return max(self.triangle[-1])


Problem18().run()
