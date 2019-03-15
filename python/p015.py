# There are 40 movements (20 downs and 20 rights), so the answer
# is 40 choose 20
from utils import binom


def compute():
    return int(binom(40, 20))


if __name__ == '__main__':
    print(compute())
