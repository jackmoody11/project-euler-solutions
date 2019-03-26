from math import sqrt
from math import factorial


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def binom(n, r):
    """Returns 'n choose r'. """
    return (factorial(n) / ((factorial(r) * factorial(n - r))))

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def prod(l):
    """
    Takes an iterable and returns product of numbers in iterable.
    Will return 1 if iterable is empty.
    """
    p = 1
    for arg in l:
        p *= arg
    return p

def is_pandigital(n):
    digits = len(n)
    if digits >= 10:
        return False
    string_n = str(n)
    for i in range(1, digits + 1):
        if str(i) not in string_n:
            return False
    return True