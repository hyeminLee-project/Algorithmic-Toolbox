def max_gold(W, weights):
    n = len(weights)
    # Create a 2D array to store the maximum weights
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill the dp table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:  # If the weight of the current bar is less than or equal to the current capacity
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + weights[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]  # If the current bar cannot be included

    return dp[n][W]

# Input reading
W, n = map(int, input().split())
weights = list(map(int, input().split()))

# Function call
result = max_gold(W, weights)
print(result)
