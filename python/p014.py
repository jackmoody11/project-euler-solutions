# Find starting number (between 1 and 1,000,000) that
# has the longest collatz string (iterations to 1)

def length_collatz(n):
    i = 1
    while True:
        if n == 1:
            return i
        elif n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        i += 1


def compute():
    my_max = (0, 0)  # (starting value, number of steps)
    for i in range(1, 1_000_001):
        l = length_collatz(i)
        if l > my_max[1]:
            my_max = (i, l)
    return my_max[0]


if __name__ == '__main__':
    print(compute())
