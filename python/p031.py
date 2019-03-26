def ways(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    # Set base case to 0 and initialize all others as 0
    ways = [1] + [0] * n

    # Go through each coin value index
    # and find number of ways to count remaining coins 
    # after taking away some value less than total
    for i in range(len(coins)):
        for j in range(coins[i], n + 1):
            ways[j] += ways[j - coins[i]]
    return ways[n]    

def compute():
    return ways(200)

if __name__ == "__main__":
    print(compute())