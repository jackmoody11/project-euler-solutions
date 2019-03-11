# There are 40 movements (20 downs and 20 rights), so the answer
# is 40 choose 20
from math import factorial


def binom(n, r):
    return (factorial(n) / ((factorial(r) * factorial(n - r))))


def compute():
    return int(binom(40, 20))


if __name__ == '__main__':
    print(compute())
