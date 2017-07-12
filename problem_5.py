# -*- coding: utf-8 -*-

"""Smallest multiple."""
# https://projecteuler.net/problem=5

from app import Problem
from utils import lcm


def isPalindrome(num):
    strNum = str(num)
    k = int(len(strNum) / 2)
    for i in xrange(k):
        if strNum[i] != strNum[- i - 1]:
            return False
    return True


class Problem4(Problem):
    """Smallest multiple."""

    def __init__(self):
        self.name = "problem 5"
        self.num = 20

    def solve(self):
        result = 1
        for value in xrange(2, self.num):
            result = lcm(result, value)
        return result


Problem4().run()
