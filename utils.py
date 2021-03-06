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
        next_num = self.primes[-1] + self.primes[-1] % 2 + 1
        while True:
            sup = int(next_num**.5)
            for prime in self.primes:
                if prime > sup:
                    self.primes.append(next_num)
                    return self.primes[-2]
                elif next_num % prime == 0:
                    break
            else:
                self.primes.append(next_num)
                return self.primes[-2]
            next_num += 2


def is_palindrome(num):
    str_num = str(num)
    k = int(len(str_num) / 2)
    for i in xrange(k):
        if str_num[i] != str_num[- i - 1]:
            return False
    return True


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


def factorial(n):
    result = 1
    for value in xrange(2, n + 1):
        result *= value
    return result


def combinatorial_number(m, n):
    if n > m:
        return 0
    result = 1
    for i in xrange(n + 1, m + 1):
        result *= i
    for i in xrange(1, m - n + 1):
        result /= i
    return result


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def get_proper_divisors(num):
    result = [1]
    pre = []
    sup = int(num**.5) + 1
    for item in xrange(2, sup):
        if num % item == 0:
            pre.append(item)
    result.extend(pre)
    if len(pre) > 0 and pre[-1]**2 == num:
        pre.pop(-1)
    for item in pre[::-1]:
        result.append(int(num / item))
    return result
