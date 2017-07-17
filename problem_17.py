# -*- coding: utf-8 -*-

"""Number letter counts."""
# https://projecteuler.net/problem=17

from app import Problem
from inflect import engine


class Problem17(Problem):
    """Number letter counts."""

    def __init__(self):
        self.name = "problem 17"
        self.num = 1000

    def solve(self):
        sum = 0
        e = engine()
        for item in xrange(1, self.num + 1):
            word = e.number_to_words(item)
            word = word.replace(' ', '').replace('-', '')
            sum += len(word)
        return sum


Problem17().run()
