def fib(n):
    ax, bx = 1, 2  # set indices
    a, b = 1, 1  # set values
    while b < n:
        a, b = b, a + b
        ax += 1
        bx += 1
    return bx


print(fib(10**(1000 - 1)))  # have to subtract 1 since 10^x gives an x + 1 digit number
