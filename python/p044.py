# Not yet solved
from utils import is_pent

def pent(n):
    return (3 * n**2 - n) / 2

def sum_diff_pent(pk, pj):
    if pk > pj:
        return is_pent(pk - pj) and is_pent(pk + pj)
    else:
        return is_pent(pj - pk) and is_pent(pj + pk)

def compute():
    k = 2
    # Store pentagonal numbers less than k
    pents = [1]
    min_d = None
    while True:
        pk = pent(k)
        for pj in reversed(pents):
            diff = pk - pj
            # Break if differences get bigger than existing minimum
            if min_d and diff >= min_d:
                break
            # Else, check condition
            elif sum_diff_pent(pk, pj):
                min_d = diff
        # Add k to pents before continuing
        pents.append(pk)
        k += 1
        # If smallest difference is greater than minimum (when min has been set), break
        if min_d and pent(k) - pent(k - 1) > min_d:
            break
    # return diff value as int rather than float (pent function returns float)
    return int(min_d)


if __name__ == "__main__":
    print(compute())
