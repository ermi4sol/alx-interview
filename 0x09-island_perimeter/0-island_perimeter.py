#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.
    
    Args:
        grid (List[List[int]]): A 2D grid representing land and water.
                                0 represents water, 1 represents land.
    
    Returns:
        int: The perimeter of the island.
    """
    # If grid is empty, return 0
    if not grid or not grid[0]:
        return 0
    
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Only process land cells
            if grid[r][c] == 1:
                # Start with 4 sides for each land cell
                cell_perimeter = 4
                
                # Check above
                if r > 0 and grid[r-1][c] == 1:
                    cell_perimeter -= 1
                
                # Check below
                if r < rows - 1 and grid[r+1][c] == 1:
                    cell_perimeter -= 1
                
                # Check left
                if c > 0 and grid[r][c-1] == 1:
                    cell_perimeter -= 1
                
                # Check right
                if c < cols - 1 and grid[r][c+1] == 1:
                    cell_perimeter -= 1
                
                # Add the cell's contribution to total perimeter
                perimeter += cell_perimeter
    
    return perimeter