from utils import read_matrix


def compute():
    matrix = read_matrix('p081.txt')
    # Calculate scores for bottom row and right most column
    for i in range(len(matrix) - 2, -1, -1):
        matrix[len(matrix)-1][i] += matrix[len(matrix) -
                                           1][i+1]  # Take care of bottom row
        matrix[i][len(matrix)-1] += matrix[i +
                                           1][len(matrix)-1]  # right most column

    for r in range(len(matrix)-2, -1, -1):
        for c in range(len(matrix)-2, -1, -1):
            # work up and left to find sum of minimum path
            matrix[r][c] += min(matrix[r+1][c], matrix[r][c+1])
    return matrix[0][0]


if __name__ == "__main__":
    print(compute())
