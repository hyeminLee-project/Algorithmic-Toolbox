def lcs3(first_sequence, second_sequence, third_sequence):
    n = len(first_sequence)
    m = len(second_sequence)
    q = len(third_sequence)
    
    # Create a 3D DP table initialized to 0
    dp = [[[0] * (q + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, q + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
    # Return the length of the longest common subsequence
    return dp[n][m][q]

if __name__ == '__main__':
    # Input for the three sequences
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    # Call lcs3 and print the result
    print(lcs3(a, b, c))
