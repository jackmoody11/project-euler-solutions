def count_rectangles(m, n):
    """ Count number of rectangles within m x n rectangle. """
    return m * n * (m+1) * (n+1) // 4


def compute():
    m, n = 1, 1
    min_diff = 0
    min_diff_area = 0
    upper = 2000
    for m in range(1, upper):
        for n in range(1, upper):
            rectangles = count_rectangles(m, n)
            diff = abs(rectangles - 2_000_000)
            if min_diff == 0 or diff < min_diff:
                min_diff = diff
                min_diff_area = m * n
            if rectangles > 2_000_000:
                break
    return min_diff_area


if __name__ == "__main__":
    print(compute())
