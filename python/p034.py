# Once we get to a decimal place where adding 9! = 362,880
# can't keep up, we will not be able to get curious numbers
# that are any larger
# Since 7 * 9! < 9,999,999, we can limit our search to be
# below 7 * 9! = 2,540,160
# Since 2! + 6 * 9! = 2,177,282 < 2,999,999, we know that no number
# will exceed this either
# Further, since 2! + 0! + 5*9! < 2,000,000 and 1! + 6*9! is the
# first number which at least reaches its own value (1,999,999),
# we can set 1,999,999 as our upper bound
FACTORIALS = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24,
              5: 120, 6: 720, 7: 5_040, 8: 40_320, 9: 362_880}

def f_sum(n):
    """
    Calculate sum of factorials of digits.
    Breaks early if sum > number.
    """
    factorial_sum = 0
    i = n
    while factorial_sum <= n:
        if i == 0:
            break
        factorial_sum += FACTORIALS[i % 10]
        i //= 10
    return factorial_sum    

def compute():
    # Do not include 1! or 2! since they are not sums
    return sum((i for i in range(3, 2_000_000) if i == f_sum(i)))

if __name__ == '__main__':
    print(compute())
