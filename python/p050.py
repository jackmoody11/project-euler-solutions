from utils import prime_cache, primes

LIMIT = 1_000_000
CACHE = prime_cache(LIMIT)
PRIMES = primes(LIMIT)


def compute():
    max_consec_count = 0
    max_consec_count_num = 0
    len_primes = len(PRIMES)
    for i in range(len_primes):
        consecutive_count = 1
        consecutive_sum = PRIMES[i]
        for j in range(i + 1, len_primes):
            consecutive_sum += PRIMES[j]
            consecutive_count += 1
            if consecutive_sum >= LIMIT:
                break
            elif consecutive_count > max_consec_count and CACHE[consecutive_sum]:
                max_consec_count = consecutive_count
                max_consec_count_num = consecutive_sum
    return max_consec_count_num

if __name__ == "__main__":
    print(compute())
            