def fib(n):
    a, b = 1, 1
    fibs = [1, ]
    while a <= n:
        a, b = b, a + b
        fibs.append(a)
    return fibs

if __name__ == '__main__':
    fibs = fib(4_000_000)
    print(sum(fib for fib in fibs if fib % 2 == 0))
