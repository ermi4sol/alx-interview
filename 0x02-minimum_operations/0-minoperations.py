#!/usr/bin/python3
"""
Module containing the minOperations function
"""

def minOperations(n):
    """Calculates the minimum number of operations to reach exactly n H's.
    
    Args:
        n (int): The target number of 'H' characters.
    
    Returns:
        int: The minimum number of operations needed, or 0 if impossible.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    # Use prime factorization to determine the minimum operations
    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
