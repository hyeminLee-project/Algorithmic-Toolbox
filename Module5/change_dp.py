def change(money):
    # Initialize dp array where dp[i] is the minimum number of coins to make i money
    dp = [float('inf')] * (money + 1)
    dp[0] = 0  # 0 money requires 0 coins
    
    # Loop through each amount from 1 to money
    for i in range(1, money + 1):
        if i >= 1:
            dp[i] = min(dp[i], dp[i - 1] + 1)  # Use 1-coin if possible
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 1)  # Use 3-coin if possible
        if i >= 4:
            dp[i] = min(dp[i], dp[i - 4] + 1)  # Use 4-coin if possible

    return dp[money]  # Return the minimum coins needed for the given money

if __name__ == '__main__':
    m = int(input())
    print(change(m))
