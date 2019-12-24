# Would like to speed this up by not using brute force approach
from math import log10


def sum_digit_squares(n):
    """ Returns sum of square of each digit in number n.
    >>> sum_digit_squares(11)
    2
    >>> sum_digit_squares(93)
    90
    """
    total = 0
    while n > 0:
        total += (n % 10)**2
        n //= 10
    return total


def compute():
    LIMIT = 10_000_000
    # max sum for 7 digit number is 9_999_999 case which is 81 * 7 where 7 = log10(10**7)
    arrivals = [0] * (9**2 * int(log10(LIMIT)) + 1)
    arrivals[1] = 1
    total = 0
    for i in range(1, LIMIT + 1):
        start = i
        while i != 1 and i != 89:
            if i < len(arrivals) and arrivals[i]:
                i = arrivals[i]
                break
            i = sum_digit_squares(i)
        if start < len(arrivals):
            arrivals[start] = i
        if i == 89:
            total += 1
    return total


if __name__ == "__main__":
    print(compute())
