# Coin Change Problem Solution

## Overview
This project implements an efficient solution to the Coin Change Problem using dynamic programming. The goal is to determine the minimum number of coins required to make up a given total amount from a list of available coin denominations.

## Problem Description
Given a set of coin denominations and a target total amount, the challenge is to find the fewest number of coins needed to make up that total. If the total cannot be achieved with the given coins, the function returns -1.

## Key Features
- Dynamic programming approach
- Handles various coin denomination sets
- Efficient algorithm with O(total * len(coins)) time complexity
- Robust error handling for edge cases

## Requirements
- Python 3.4.3+
- Ubuntu 20.04 LTS
- PEP 8 style guidelines

## Function Prototype
```python
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
```

## Example Usage
```python
# Example 1
print(makeChange([1, 2, 25], 37))  # Output: 7

# Example 2
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Algorithm Explanation
The solution uses dynamic programming to solve the coin change problem:
1. Create a dynamic programming array to store minimum coins for each amount
2. Iterate through all possible amounts from 0 to total
3. For each amount, try all coin denominations
4. Update the minimum number of coins needed
5. Return the minimum coins for the target total

## Time and Space Complexity
- **Time Complexity**: O(total * len(coins))
- **Space Complexity**: O(total)

## Limitations
- Assumes an infinite number of each coin denomination
- Works best with a diverse set of coin denominations

## Author
[Ermiyas Solomon]
```