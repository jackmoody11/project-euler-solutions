from utils import list_totients, is_permutation

LIMIT = 10_000_000
TOTIENTS = list_totients(LIMIT)

def compute():
    (min_n, min_ratio) = (2, 2)
    for n in range(2, LIMIT + 1):
        if n/TOTIENTS[n] < min_ratio and is_permutation(n, TOTIENTS[n]):
            (min_n, min_ratio) = (n, n/TOTIENTS[n])
    return min_n

if __name__ == "__main__":
    print(compute())