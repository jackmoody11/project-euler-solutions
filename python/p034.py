# Once we get to a decimal place where adding 9! = 362,880
# can't keep up, we will not be able to get curious numbers
# that are any larger
# Since 7 * 9! < 9,999,999, we can limit our search to be 
# below 7 * 9! = 2,540,160
from math import factorial as f


def compute():
    total = 0
    # Do not include 1! or 2! since they are not sums
    for i in range(3, 2_540_160):
        if i == sum([f(int(c)) for c in str(i)]):
            total += i
    return total

if __name__ == '__main__':
    print(compute())