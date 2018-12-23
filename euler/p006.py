# Find the difference between (1 + 2 + 3 + ... + 100) ^ 2 and 1^2 + 2^2 + ... + 100^2


def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))


def square_of_sum(n):
    return sum(i for i in range(1, n + 1))**2


def compute():
    return square_of_sum(100) - sum_of_squares(100)


if __name__ == '__main__':
    print(compute())