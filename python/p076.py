# Too slow - needs to be further optimized
def partition(n, m):
    if n == m:
        return 1 + partition(n, m-1)
    elif m == 0 or n < 0:
        return 0
    elif n == 0 or m == 1:
        return 1
    else:
        return partition(n, m-1) + partition(n-m, m)

if __name__ == "__main__":
    print(partition(100, 99))