# Currently incorrect -- needs work

from itertools import combinations
from math import sqrt

def proper_divisors(n):
    divs = set()
    for i in range(1, n // 2):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs.difference({n})

def list_abundants(n):
    abundants = []
    for i in range(12, n + 1):
        if sum(proper_divisors(i)) > i:
            abundants.append(i)
    return abundants


def compute():
    combos = list(combinations(list_abundants(28123), 2))
    sms = {sum(i) for i in combos}
    res = sum([j for j in range(1, 28124) if j not in sms])
    return sum([j for j in range(1, 28124) if j not in sms])


if __name__ == '__main__':
    print(compute())
