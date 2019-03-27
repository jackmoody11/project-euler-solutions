from math import sqrt
from math import factorial
import string


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime(n):
    prime_count = 0
    i = 1
    while prime_count < n:
        i += 1
        if is_prime(i):
            prime_count += 1
        
    return i

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

def word_score(name):
    c_scores = {string.ascii_uppercase[i]: i + 1 for i in range(26)}
    score = 0
    for c in name:
        score += c_scores[c]
    return score

def is_pent(n):
    # n = (3 * x**2 - x)/2
    # for x to be int, (1 + sqrt(24n + 1)/2 
    # must be int
    pen_test = (1 + sqrt(24*n + 1))/6
    if pen_test == int(pen_test):
        return True
    return False

def is_tri(n):
    # Same reasoning as is_pent
    # means (-1 + sqrt(1 + 8n))/2 must be int
    tri_test = (-1 + sqrt(1 + 8*n))/2
    if tri_test == int(tri_test):
        return True
    return False

def is_hex(n):
    # See tri and pent explanation
    hex_test = (1 + sqrt(1 + 8*n))/4
    if hex_test == int(hex_test):
        return True
    return False