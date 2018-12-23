# Compute the sum of all multiples of 3 and 5 less than 1000


def compute():
    ans = sum(i for i in range(1000) if (i % 3 == 0 or i % 5 == 0))
    return str(ans)


if __name__ == '__main__':
    print(compute())


