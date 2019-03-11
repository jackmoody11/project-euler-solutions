def compute():
    s = str(2**1000)
    return sum(int(i) for i in s)


if __name__ == '__main__':
    print(compute())
