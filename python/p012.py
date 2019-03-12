# Find the smallest triangle number that has over five hundred divisors
# Need to check that this works (is currently taking too long)
from math import sqrt


def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def compute():
    # We know that to have 500 divisors, num >= 500
    # i * (i + 1) / 2 is >= 500 when i = 32, so start there
    i = 7
    while True:
        num = sum(range(i))
        divisors = find_divisors(num)
        if len(divisors) > 500:
            return num
        else:
            i += 1


if __name__ == '__main__':
    print(compute())
