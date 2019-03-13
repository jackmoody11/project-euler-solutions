file = "p067.txt"

with open(file) as f:
    triangle = [list(map(int, line.split())) for line in f]

def compute():
    # Start at second to last row (first row already done)
    for row in reversed(range(len(triangle)-1)):
        # for each column in the row, find maxed triangle value  
        # (either down or down and to the right)
        for col in range(len(triangle[row])):
            # Add maxed triangle value to current value
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    # return top value after having triangles "compete"
    return triangle[0][0]

if __name__ == '__main__':
    print(compute())