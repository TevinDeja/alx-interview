#!/usr/bin/python3
"""
Using dynamic programming to calculate the minimum number of operations
"""

def minOperations(n):
    """
    Computing the minimum operations needed to achieve n 'H' characters
    """
    if n <= 1:
        return 0
    
    # Initialize an array to store the minimum operations for each number up to n
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        # Initialize with a large number
        dp[i] = float('inf')
        
        # Try all possible factors of i
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                # If j is a factor, we can copy j and paste i/j - 1 times
                dp[i] = min(dp[i], dp[j] + (i // j))
        
        # If i is prime, we need to copy all and paste i-1 times
        if dp[i] == float('inf'):
            dp[i] = i
    
    return dp[n]
