def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, operators, min_dp, max_dp):
    min_value = float('inf')
    max_value = -float('inf')

    # Try every operator between i and j
    for k in range(i, j):
        op = operators[k]
        a = evaluate(max_dp[i][k], max_dp[k+1][j], op)
        b = evaluate(max_dp[i][k], min_dp[k+1][j], op)
        c = evaluate(min_dp[i][k], max_dp[k+1][j], op)
        d = evaluate(min_dp[i][k], min_dp[k+1][j], op)

        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    
    return min_value, max_value

def maximum_value(dataset):
    digits = []
    operators = []

    # Parse the dataset into digits and operators
    for i in range(len(dataset)):
        if i % 2 == 0:
            digits.append(int(dataset[i]))
        else:
            operators.append(dataset[i])

    n = len(digits)
    
    # Initialize DP tables
    min_dp = [[0] * n for _ in range(n)]
    max_dp = [[0] * n for _ in range(n)]
    
    # Base case: for each single number, the min and max are the number itself
    for i in range(n):
        min_dp[i][i] = digits[i]
        max_dp[i][i] = digits[i]
    
    # Fill DP tables
    for s in range(1, n):  # s is the step (distance between i and j)
        for i in range(n - s):  # i is the starting point
            j = i + s  # j is the ending point
            min_dp[i][j], max_dp[i][j] = min_and_max(i, j, operators, min_dp, max_dp)
    
    # The result is the maximum value for the entire expression
    return max_dp[0][n-1]

if __name__ == "__main__":
    print(maximum_value(input()))
