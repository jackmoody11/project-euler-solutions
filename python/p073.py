from utils import farey_count

def compute():
    return farey_count(12_000, 1, 3, 1, 2)

if __name__ == "__main__":
    print(compute())