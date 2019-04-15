FACTORIALS = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24,
              5: 120, 6: 720, 7: 5_040, 8: 40_320, 9: 362_880}
LIMIT = 1_000_000  

def compute():
    """
    Initialize sequence lengths as 0 (except for seq_len of 0).
    Count length of sequence until you either repeat or fall on a 
    number where you know the sequence length and then add that sequence 
    length to the list.
    """
    seq_len = [1] + [0] * (LIMIT - 1)
    for i in range(1, LIMIT):
        n = i
        seen = set()
        count = 0
        while n not in seen:
            seen.add(n)
            count += 1
            n = sum([FACTORIALS[int(c)] for c in str(n)])
            if n < i:
                count += seq_len[n]
                break
        seq_len[i] = count
    return sum(1 for i in range(len(seq_len)) if seq_len[i] == 60)


if __name__ == "__main__":
    print(compute())