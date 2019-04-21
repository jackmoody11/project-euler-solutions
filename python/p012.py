# Find the smallest triangle number that has over five hundred divisors
from math import sqrt


def num_divisors(n):
    """
    ex: 10 has divisors 1 2 5 10
    1 2 | 5 10 -> 2 captured * 2 = 4 divisors
    ex: 16 has divisor 1 2 | 4 8 16 -> 3 captured * 2 = 6,
    but 4 also be counted once
    """
    end = int(sqrt(n))
    result = sum(2 for i in range(1, end) if n % i == 0)
    if end**2 == n:
        result += 1
    return result


def compute():
    n = 1
    while num_divisors(n*(n+1) // 2) < 500:
        n += 1
    return n*(n+1) // 2

if __name__ == '__main__':
    print(compute())
