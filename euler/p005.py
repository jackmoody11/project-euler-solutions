# Find the smallest number that is divisible by the numbers 1, 2, ..., 20
def is_divisible_up_to(x, n):
    for i in range(2, n):
        if x % i != 0:
            return False
    return True


def compute():
    x = 2520
    while not is_divisible_up_to(x, 20):
        x += 20
    return x


if __name__ == '__main__':
    print(compute())
