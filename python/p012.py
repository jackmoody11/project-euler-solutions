# Find the smallest triangle number that has over five hundred divisors
# Need to check that this works (is currently taking too long)
from math import sqrt


def num_divisors(n):
	end = int(sqrt(n))
    # ex: 10 has divisors 1 2 5 10
    # 1 2 | 5 10 -> 2 captured * 2 = 4 divisors
    # ex: 16 has divisor 1 2 | 4 8 16 -> 3 captured * 2 = 6,
    # but 4 also be counted once

	result = sum(2
		for i in range(1, end)
		if n % i == 0)
	if end**2 == n:
		result += 1
	return result


def compute():
    i, num = 1, 1
    while True:
        if num_divisors(num) > 500:
            return num
        else:
            i += 1
            num += i


if __name__ == '__main__':
    print(compute())
