def compute_operations(n):
    # Initialize the dp array where dp[i] stores the minimum number of operations to get to i
    dp = [0] * (n + 1)  # dp[0] is not used
    
    # To store the sequence of operations
    previous = [0] * (n + 1)
    
    for i in range(2, n + 1):
        # Start by assuming the only option is subtract 1
        min_operations = dp[i - 1] + 1
        previous[i] = i - 1  # Path to i is from i-1
        
        # Check if divisible by 2
        if i % 2 == 0:
            if dp[i // 2] + 1 < min_operations:
                min_operations = dp[i // 2] + 1
                previous[i] = i // 2
        
        # Check if divisible by 3
        if i % 3 == 0:
            if dp[i // 3] + 1 < min_operations:
                min_operations = dp[i // 3] + 1
                previous[i] = i // 3
        
        dp[i] = min_operations
    
    # Reconstruct the sequence of operations by backtracking
    sequence = []
    while n > 0:
        sequence.append(n)
        n = previous[n]
    
    # Reverse the sequence to start from 1
    sequence.reverse()
    
    return sequence

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
