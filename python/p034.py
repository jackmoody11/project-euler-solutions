# Once we get to a decimal place where adding 9! = 362,880
# can't keep up, we will not be able to get curious numbers
# that are any larger
# Since 7 * 9! < 9,999,999, we can limit our search to be
# below 7 * 9! = 2,540,160
# Since 2! + 6 * 9! = 2,177,282 < 2,999,999, we know that no number
# will exceed this either
FACTORIALS = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24,
              5: 120, 6: 720, 7: 5_040, 8: 40_320, 9: 362_880}


def compute():
    total = 0
    nums = set()
    # Do not include 1! or 2! since they are not sums
    for i in range(3, 2_177_283):
        if i == sum([FACTORIALS[int(c)] for c in str(i)]):
            total += i
            nums.add(i)
    return total, max(nums)


if __name__ == '__main__':
    print(compute())
