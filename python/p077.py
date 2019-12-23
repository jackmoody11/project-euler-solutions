from utils import primes


def compute():
    PRIMES = primes(1000)
    target = 10  # we are given that 10 only has 5 prime partitions
    while True:
        prime_partitions = [0] * (target + 1)
        prime_partitions[0] = 1
        for p in PRIMES:
            for j in range(p, target + 1):
                prime_partitions[j] += prime_partitions[j - p]
        if prime_partitions[target] > 5000:
            break
        target += 1
    return target


if __name__ == "__main__":
    print(compute())
