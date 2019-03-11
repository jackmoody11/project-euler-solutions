# Compute the sum of the even fibonacci numbers less than 4,000,000

def fib(n):
    a, b = 1, 1
    total = 0
    while a <= n:
        a, b = b, a + b
        if a % 2 == 0:
            total += a
    return total


if __name__ == '__main__':
    total = fib(4_000_000)
    print(total)
