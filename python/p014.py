# Find starting number (between 1 and 1,000,000) that
# has the longest collatz string (iterations to 1)

# Unsolved - need to optimize algorithm (takes too long)

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
    max = (0, 0)  # (starting value, number of steps)
    for i in range(1_000_001):
        l = length_collatz(i)
        if l > max[1]:
            max = (i, l)
        if i % 10_000 == 0:
            print(i, l)
    return max[0]


if __name__ == '__main__':
    print(compute())
