def fib(n):
    ax, bx = 1, 2  # set indices
    a, b = 1, 1  # set values
    while b < n:
        a, b = b, a + b
        ax += 1
        bx += 1
    return bx


def compute():
    return fib(10**(1000 - 1))  # 10**x gives an x + 1 digit number


if __name__ == '__main__':
    print(compute())
