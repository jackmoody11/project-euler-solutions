# Compute the sum of the even fibonacci numbers less than 4,000,000


def fib(n):
    a, b = 1, 1
    fibs = [1, ]
    while a <= n:
        a, b = b, a + b
        fibs.append(a)
    return fibs


if __name__ == '__main__':
    fs = fib(4_000_000)
    print(sum(f for f in fs if f % 2 == 0))
