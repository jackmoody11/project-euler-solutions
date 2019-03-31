from utils import digital_sum

def compute():
    max_d = 0
    for a in range(1, 100):
        for b in range(1, 100):
            d_sum = digital_sum(a**b)
            if d_sum > max_d:
                max_d = d_sum
    return max_d

if __name__ == "__main__":
    print(compute())