# Find the smallest triangle number that has over five hundred divisors
from math import sqrt


def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def compute():
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
