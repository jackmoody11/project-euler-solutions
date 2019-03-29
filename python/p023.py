# My initial solution was correct, but much slower
# Using https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p023.py
# helped speed this process up (especially for testing purposes)

def compute():
    LIMIT = 28124
    divisor_sum = [0] * LIMIT
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisor_sum[j] += i
    abundants = [i for i, x in enumerate(divisor_sum) if x > i]

    sum_of_two = [False] * LIMIT
    for i in abundants:
        for j in abundants:
            if i + j < LIMIT:
                sum_of_two[i + j] = True
            else:
                break
    return sum(i for i, x in enumerate(sum_of_two) if not x)


if __name__ == '__main__':
    print(compute())
