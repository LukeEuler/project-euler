# -*- coding: utf-8 -*-

"""Multiples of 3 and 5."""
# https://projecteuler.net/problem=1

from app import Problem


def _multilpe_of3or5(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    return False


class Problem1(Problem):
    """Multiples of 3 and 5."""
    def solve(self):
        result = 0
        for num in xrange(1, 1000):
            if _multilpe_of3or5(num):
                result += num

        return result


Problem1().run()
