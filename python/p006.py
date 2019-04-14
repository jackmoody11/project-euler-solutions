# Find the difference between (1 + 2 + 3 + ... + 100) ^ 2 and 1^2 + 2^2 + ... + 100^2


def compute():
    return sum(i for i in range(101))**2 - sum(i**2 for i in range(101))

if __name__ == '__main__':
    print(compute())