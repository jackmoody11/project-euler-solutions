# Not yet solved
from utils import is_pent


def pent(n):
    return (3 * n**2 - n) / 2

def compute():
    k = 2
    while True:
        for j in range(1, k):
            pk = pent(k)
            pj = pent(j)
            if is_pent(pk - pj) and is_pent(pk + pj):
                return pk - pj


if __name__ == "__main__":
    print(compute())
