# This will solve the knapsack problem. 


def solve_knapsack(profits, weights, capacity):
    # dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    return solve_knapsack_helper_bottom_up(profits, weights, capacity)


def solve_knapsack_helper(profits, weights, capacity, currIdx):
    # check base if capacity is not 0 or currIdx out of bound profits
    if capacity <= 0 or currIdx >= len(profits):
        return 0
    # check if current weight is good with capacity
    profit1 = 0
    if weights[currIdx] <= capacity:
        # compute profit1 with current weight
        profit1 = profits[currIdx] + solve_knapsack_helper(profits, weights, capacity - weights[currIdx], currIdx + 1)
    # compute profit2 without current weight
    profit2 = solve_knapsack_helper(profits, weights, capacity, currIdx + 1)
    # max(profit1, profit2)
    return max(profit1, profit2 )

def solve_knapsack_helper_dp(dp, profits, weights, capacity, currIdx):
    # check base if capacity is not 0 or currIdx out of bound profits
    if capacity <= 0 or currIdx >= len(profits):
        return 0
    # check result in dp first
    if dp[currIdx][currIdx] != -1:
        return dp[currIdx][currIdx]
    # check if current weight is good with capacity
    profit1 = 0
    if weights[currIdx] <= capacity:
        # compute profit1 with current weight
        profit1 = profits[currIdx] + solve_knapsack_helper(profits, weights, capacity - weights[currIdx], currIdx + 1)
    # compute profit2 without current weight
    profit2 = solve_knapsack_helper(profits, weights, capacity, currIdx + 1)
    
    # store result into dp 
    dp[currIdx][currIdx] = max(profit1, profit2)

    return dp[currIdx][currIdx]

def solve_knapsack_helper_bottom_up(profits, weights, capacity):
    # basic checks [check for capacity, n != len(profits), n == 0]
    n = len(profits)
    if capacity <=0 or n != len(profits) or n == 0:
        return 0
    # initialize dp 2d array 
    dp = [[0 for x in range(capacity + 1)] for y in range(len(profits))]
    # initialize first row with profits[0] if weight[0] < c
    for c in range(capacity + 1):
        if weights[0] < c:
            dp[0][c] = profits[0]
    # intialize first column with 0 since it is 0 weight column
    for p in range(len(profits)):
        dp[p][0] = 0
    # start compute each row and then col
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c - weights[i]]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)
    return dp[n - 1][capacity] 

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()