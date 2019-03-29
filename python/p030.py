# Find the sum of all the numbers that can be 
# written as the sum of fifth powers of their digits.

def compute():
	# As stated in the problem, 1 = 1^5 is excluded.
	# If a number has at least n >= 7 digits, then even if every digit is 9,
	# n * 9^5 is still less than the number (which is at least 10^n).
    # Further, the sum of 6 digits raised to the fifth power can't exceed 6 * 9^5 = 354,294
	ans = sum(i for i in range(2, 354294) if i == fifth_power_digit_sum(i))
	return ans


def fifth_power_digit_sum(n):
	return sum(int(c)**5 for c in str(n))


if __name__ == "__main__":
	print(compute())