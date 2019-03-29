# Find starting number (between 1 and 1,000,000) that
# has the longest collatz string (iterations to 1)
# If we get to a known collatz length, add that to the
# current count, and we are done - will save a lot of time

def compute():
    LIMIT = 1_000_001
    length_collatz = [0] * LIMIT
    for i in range(2, LIMIT):
        count = 0
        x = i
        while x >= i and x != 1:
            count += 1
            if x % 2 == 0:
                x //= 2
            else:
                x = x * 3 + 1
        length_collatz[i] = length_collatz[x] + count
    return length_collatz.index(max(length_collatz))

if __name__ == '__main__':
    print(compute())
