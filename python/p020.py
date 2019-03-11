from math import factorial


def compute():
    f = str(factorial(100))
    return sum([int(i) for i in f])


if __name__ == '__main__':
    print(compute())
