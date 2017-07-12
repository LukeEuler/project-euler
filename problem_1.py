# -*- coding: utf-8 -*-

"""Multiples of 3 and 5."""
# https://projecteuler.net/problem=1


def _multilpeOf3or5(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    return False


sum = 0
for num in xrange(1, 1000):
    if _multilpeOf3or5(num):
        sum += num

print sum
