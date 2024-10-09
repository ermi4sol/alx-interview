#!/usr/bin/python3
"""
This module defines a function pascal_triangle(n) that generates
Pascal's Triangle up to a given number of rows n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s Triangle of n rows.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of lists: Pascal's Triangle represented as a list of lists.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # The first row of Pascal's Triangle

    # Generate the remaining rows of the triangle
    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Each row starts and ends with 1, and in between, we sum the two values above
        row = [1] + [prev_row[j - 1] + prev_row[j] for j in range(1, i)] + [1]
        triangle.append(row)

    return triangle
