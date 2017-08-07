# -*- coding: utf-8 -*-


class Fibonacci:
    """generate fibnacci numbers."""

    def __init__(self):
        """Fibonacci begins with 1, 1."""
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


class Prime:
    """generate primes."""

    def __init__(self):
        self.primes = [2]

    def __iter__(self):
        return self

    def next(self):
        nextNum = self.primes[-1] + self.primes[-1] % 2 + 1
        while True:
            sup = int(nextNum**.5)
            for prime in self.primes:
                if prime > sup:
                    self.primes.append(nextNum)
                    return self.primes[-2]
                elif nextNum % prime == 0:
                    break
            else:
                self.primes.append(nextNum)
                return self.primes[-2]
            nextNum += 2


def isPalindrome(num):
    strNum = str(num)
    k = int(len(strNum) / 2)
    for i in xrange(k):
        if strNum[i] != strNum[- i - 1]:
            return False
    return True


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


def combinatorialNumber(m, n):
    if n > m:
        return 0
    result = 1
    for i in xrange(n + 1, m + 1):
        result *= i
    for i in xrange(1, m - n + 1):
        result /= i
    return result


def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False
