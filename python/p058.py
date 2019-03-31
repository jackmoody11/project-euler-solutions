from utils import is_prime


def compute():
    # Let 1 be on level = 0, 3, 5, 7, 9 on level = 1
    prime_count = 3
    level = 1
    while prime_count / (4*level + 1) >= 0.10:
        level += 1
        for i in range(-1, 3):
            if is_prime((2*level)**2 + 2 * i * level + 1):
                prime_count += 1
        
    return 2 * level + 1 # side length is 2 * level + 1


if __name__ == "__main__":
    print(compute())