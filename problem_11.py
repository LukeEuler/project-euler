# -*- coding: utf-8 -*-

"""Largest product in a grid."""
# https://projecteuler.net/problem=11

from app import Problem


class Problem11(Problem):
    """Largest product in a grid."""

    def __init__(self):
        self.name = "problem 11"
        self.length = 4
        f = open("problem_11.txt")
        self.numbers = []
        line = f.readline()
        while line:
            self.numbers.append([int(x) for x in line.strip('\n').split(' ')])
            line = f.readline()
        f.close()

    def solve(self):
        return max(self.transverse(),
                   self.vertical(),
                   self.diagonal(),
                   self.antiDiagonal())

    def product(self, list):
        result = 0
        if len(list) < self.length:
            return result
        for i in xrange(0, len(list) - self.length):
            value = reduce(lambda x, y: x * y, list[i:i + self.length])
            result = max(result, value)
        return result

    def transverse(self):
        result = 0
        for i in xrange(len(self.numbers)):
            value = self.product(self.numbers[i])
            result = max(result, value)
        return result

    def vertical(self):
        result = 0
        for j in xrange(len(self.numbers[0])):
            list = []
            for i in xrange(len(self.numbers)):
                list.append(self.numbers[i][j])
            value = self.product(list)
            result = max(result, value)
        return result

    def diagonal(self):
        result = 0
        height, width = len(self.numbers), len(self.numbers[0])

        i = 0
        for j in xrange(width):
            list = []
            x, y = i, j
            while (x < height and y < width):
                list.append(self.numbers[x][y])
                x += 1
                y += 1
            value = self.product(list)
            result = max(result, value)

        j = 0
        for i in xrange(1, height):
            list = []
            x, y = i, j
            while (x < height and y < width):
                list.append(self.numbers[x][y])
                x += 1
                y += 1
            value = self.product(list)
            result = max(result, value)

        return result

    def antiDiagonal(self):
        result = 0
        height, width = len(self.numbers), len(self.numbers[0])

        i = 0
        for j in xrange(width):
            list = []
            x, y = i, j
            while (x < height and y > -1):
                list.append(self.numbers[x][y])
                x += 1
                y -= 1
            value = self.product(list)
            result = max(result, value)

        j = width - 1
        for i in xrange(1, height):
            list = []
            x, y = i, j
            while (x < height and y > -1):
                list.append(self.numbers[x][y])
                x += 1
                y -= 1
            value = self.product(list)
            result = max(result, value)

        return result


Problem11().run()
