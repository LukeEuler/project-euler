# -*- coding: utf-8 -*-

"""Longest Collatz sequence."""
# https://projecteuler.net/problem=14

from app import Problem


class Problem14(Problem):
    """Longest Collatz sequence."""

    def __init__(self):
        self.name = "problem 14"
        self.maxStart = 1000000

    def getNext(self, num):
        if num % 2 == 0:
            return int(num / 2)
        return 3 * num + 1

    def solve(self):
        result = 1
        maxLength = 1
        record = {1: 1}
        for num in xrange(1, self.maxStart):
            if num in record:
                continue

            baseLength = 0
            list = []
            while True:
                list.insert(0, num)
                num = self.getNext(num)
                if num in record:
                    baseLength = record.get(num)
                    break

            for index, item in enumerate(list):
                length = baseLength + index + 1
                if length > maxLength:
                    maxLength = length
                    result = item
                record[item] = length

        return result


Problem14().run()
