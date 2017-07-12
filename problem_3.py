# -*- coding: utf-8 -*-

"""Largest prime factor."""
# https://projecteuler.net/problem=3


class Prime:
    """generate primes."""

    def __init__(self):
        self.primes = [2]

    def __iter__(self):
        return self

    def next(self):
        nextNum = self.primes[-1] + self.primes[-1] % 2 + 1
        while True:
            for prime in self.primes:
                if nextNum % prime == 0:
                    break
            else:
                self.primes.append(nextNum)
                return self.primes[-2]
            nextNum += 2


num = 600851475143
factor = []
for prime in Prime():
    while num % prime == 0:
        factor.append(prime)
        num = int(num / prime)
    if num == 1 or num < prime:
        break

print factor[-1]
