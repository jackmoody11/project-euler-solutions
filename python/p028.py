def level_sum(n):
    """
    Except for n = 0, each level looks like this
    (2n + 1)^2 - 2n ------ {2n} ------ (2n + 1)^2
    |                                          |
    |                                          |    
    |                                          |
  {2n}                                       {2n}
    |                                          |
    |                                          |
    |                                          |
    (2n + 1)^2 - 4n ------ {2n} ------ (2n + 1)^2 - 8n
    """
    return 4*(2*n + 1)**2 - 12*n

def compute():
    total = 1
    for i in range(1, 501):
        total += level_sum(i)
    return total

if __name__ == "__main__":
    print(compute())
