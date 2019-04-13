from utils import list_totients

def compute():
    """
    Count number of coprimes for each value from 1 to 1,000,000 and then subtract 1 
    because 1/1 is not of the form n/d where n < d.
    """
    return sum(list_totients(1_000_000)) - 1

if __name__ == "__main__":
    print(compute())