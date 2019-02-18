# Currently incorrect -- needs work

from itertools import combinations


def is_abundant(n):
    div_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            div_sum += i
            if div_sum > n:
                return True
    return False


def list_abundants(n):
    abundants = []
    for i in range(12, n + 1):
        if is_abundant(i):
            abundants.append(i)
    return abundants


def compute():
    combos = list(combinations(list_abundants(28123), 2))
    sms = {sum(i) for i in combos}
    return sum([j for j in range(1, 28124) if j not in sms])
