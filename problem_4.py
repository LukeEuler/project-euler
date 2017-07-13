# -*- coding: utf-8 -*-

"""Largest palindrome product."""
# https://projecteuler.net/problem=4

from app import Problem
from utils import isPalindrome


class Problem4(Problem):
    """Largest palindrome product."""

    def __init__(self):
        self.name = "problem 4"

    def solve(self):
        maxNum = 1000
        minNum = 99
        result = 0

        for a in xrange(maxNum - 1, minNum, -1):
            for b in xrange(a, minNum, -1):
                num = a * b
                if isPalindrome(num):
                    minNum = b
                    result = max(result, num)
                    break
        return result


Problem4().run()
