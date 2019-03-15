from utils import prod

filename = "p011.txt"

# convert to list of lists
with open(filename) as f:
    matrix = [list(map(int, line.split())) for line in f]

def compute():
    # Start in the top left corner of the matrix
    # Go from left to right and (if possible) check 
    # products down, right, and diagonally (left and right)
    # We don't need to check left, since the right product
    # will catch all products which would be caught with
    # left
    max_p = 0
    for r in range(len(matrix) - 4):
        for c in range(len(matrix)):
            down = prod((matrix[r-i][c] for i in range(4)))
            if c >= 3:
                left_diag = prod((matrix[r+i][c-i] for i in range(4)))
            if c <= 16:
                right = prod((matrix[r][c+i] for i in range(4)))
                right_diag = prod((matrix[r+i][c+i] for i in range(4)))
            if c >=3 and c<= 16:
                m = max((down, left_diag, right, right_diag))
            elif c < 3:
                m = max((down, right, right_diag))
            elif c > 16:
                m = max((down, left_diag))
            if m > max_p:
                max_p = m
    return max_p


if __name__ == '__main__':
    print(compute())