# We only want the first 10 digits, so use fact that
# ab (mod c) = (a (mod c) * b (mod c)) (mod c)
# or more generally \left(\prod_{i=1}^{n}a_{i} \right) (mod b) = 
# \left(\prod_{i=1}^{n} a_{i} (mod b) \right) (mod b)
from utils import prod

def compute():
    bin_power = [int(i) for i in str(bin(7830457))[2:]][::-1]
    mod_generator = (2**(2**idx) % 10**10 for idx, v in enumerate(bin_power) if v == 1)
    total_mod = (prod(mod_generator) * 28433 + 1) % 10**10
    return total_mod

if __name__ == "__main__":
    print(compute())