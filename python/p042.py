import csv
from utils import word_score

def is_triangle_word(word):
    triangle_nums = {(n**2 + n)/2 for n in range(1, 30)}
    if word_score(word) in triangle_nums:
        return True
    return False

def compute():
    # Read words
    file = "p042.txt"
    with open(file, 'r') as f:
        csv_f = csv.reader(f)
        words = list(csv_f)[0]
    # Count number of words that are triangle words
    return sum([is_triangle_word(word) for word in words])


if __name__ == "__main__":
    print(compute())