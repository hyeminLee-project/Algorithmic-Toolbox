def lcs2(first_sequence, second_sequence):
    n = len(first_sequence)
    m = len(second_sequence)
    
    # Initialize the DP table with size (n+1) x (m+1), all filled with 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill the DP table based on the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # If elements match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # If they don't match
    
    # The length of the LCS is stored in dp[n][m]
    return dp[n][m]

if __name__ == '__main__':
    n = int(input())  # Length of first sequence
    a = list(map(int, input().split()))  # First sequence
    assert len(a) == n

    m = int(input())  # Length of second sequence
    b = list(map(int, input().split()))  # Second sequence
    assert len(b) == m

    # Compute and print the length of the LCS
    print(lcs2(a, b))
