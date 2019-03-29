from math import sqrt


def d(n):
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)


def amicables(n):
    ams = []
    for i in range(1, n + 1):
        di = d(i)
        ddi = d(di)
        if i == ddi != di:
            ams.append(i)
    return ams

def compute():
    return sum(amicables(10_000))

if __name__ == '__main__':
    print(compute())
