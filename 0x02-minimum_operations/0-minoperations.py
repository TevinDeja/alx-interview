#!/usr/bin/python3
"""
Calculating minimum operations
"""


def minOperations(n):
    """
    Calculates fewest no of operations needed
    """
    if n < 2:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
