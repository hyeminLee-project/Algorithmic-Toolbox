def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    
    # Create a DP table to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: fill the first row and column
    for i in range(m + 1):
        dp[i][0] = i  # It takes 'i' deletions to convert the first_string[0:i] to an empty string
    for j in range(n + 1):
        dp[0][j] = j  # It takes 'j' insertions to convert an empty string to second_string[0:j]
    
    # Fill the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first_string[i - 1] == second_string[j - 1]:
                cost = 0  # No operation needed if characters match
            else:
                cost = 1  # Substitution needed if characters differ
            
            dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                           dp[i][j - 1] + 1,      # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution
    
    # The result is the edit distance between the two full strings
    return dp[m][n]

if __name__ == "__main__":
    first_string = input().strip()
    second_string = input().strip()
    print(edit_distance(first_string, second_string))
