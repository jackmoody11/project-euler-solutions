def is_one_nine_pandigital(n):
    d_pdigital = 0
    pdig_str = ''
    i = 1
    while d_pdigital < 9:
        pdig_str += str(n * i)
        d_pdigital += len(pdig_str)
        i += 1
    # There should be a more elegant way to do this conditional
    if len(set(pdig_str)) == len(pdig_str) == 9 and '0' not in set(pdig_str):
        return (True, int(pdig_str))
    else:
        return (False, 0)

def compute():
    # No 4 digit number can be 
    pd_max = 0
    for i in range(1, 99999):
        res = is_one_nine_pandigital(i)
        if res[0] and res[1] > pd_max:
            pd_max = res[1]
            index = i
    return pd_max

if __name__ == '__main__':
    print(compute())