def cycle_len(n):
    seen = set()
    i = 1
    total_len = 0
    while i not in seen:
        seen.add(i)
        i = (10 * i) % n
        total_len += 1
    return total_len

def compute():
    max_len = (0, 0) # (d, length of cycle)
    for d in range(2, 1000):
        c_len = cycle_len(d)
        if c_len > max_len[1]:
            max_len = (d, c_len)
    return max_len[0]


if __name__ == "__main__":
    print(compute())