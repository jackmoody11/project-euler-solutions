from utils import is_tri, is_pent, is_hex

def hex_num(i):
    return 2*i**2 -i

def compute():
    # We already found that H_143 satisfies this
    # condition, and we want to find the next num
    # that satisfies the condition
    # We use hex_num to generate the numbers, because this grows the fastest
    # and allows us to perform the least number of checks
    i = 144
    while True:
        num = hex_num(i)
        if is_tri(num) and is_pent(num):
            return num
        else:
            i += 1

if __name__ == "__main__":
    print(compute())
