from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def prod(l):
    """
    Takes a list and returns product of numbers in list.
    Will return 1 if list is empty.
    """
    p = 1
    for arg in l:
        p *= arg
    return p