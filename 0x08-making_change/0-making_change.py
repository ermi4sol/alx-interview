#!/usr/bin/python3
"""
Solution to the Coin Change Problem using Dynamic Programming
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    
    Args:
        coins (list): List of coin denominations
        total (int): Target total amount
    
    Returns:
        int: Fewest number of coins needed to meet total, 
             or -1 if total cannot be met
    """
    # Handle base cases
    if total <= 0:
        return 0
    
    # Initialize dynamic programming array
    # dp[i] will store the minimum coins needed to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through all amounts from 1 to total
    for amount in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= amount:
                # Update minimum coins needed for current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Return result, or -1 if total cannot be met
    return dp[total] if dp[total] != float('inf') else -1