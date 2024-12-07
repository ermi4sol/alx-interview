# Island Perimeter

## Project Description

This project implements a solution to calculate the perimeter of an island in a 2D grid. The challenge involves writing a Python function that determines the total perimeter of an island represented by a matrix of 0s (water) and 1s (land).

## Concepts Covered

- 2D Array (Matrix) Manipulation
- Conditional Logic
- Grid Traversal
- Perimeter Calculation Algorithms

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- Python 3.4.3 on Ubuntu 20.04 LTS
- PEP 8 style guidelines (version 1.7)
- No external module imports
- All files must end with a new line
- Mandatory `README.md` file
- All files must be executable

### Problem Constraints
- Grid is a list of lists of integers
- 0 represents water
- 1 represents land
- Cells are square with side length 1
- Cells connect horizontally/vertically (not diagonally)
- Grid width and height ≤ 100
- Grid is surrounded by water
- Only one island (or no island) exists
- No "lakes" within the island

## Function Specification

### `island_perimeter(grid)`

**Parameters:**
- `grid`: A 2D list representing the island map

**Returns:**
- Integer representing the island's perimeter

**Example:**
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Algorithm Approach

1. Iterate through each cell in the grid
2. For land cells (value 1):
   - Start with 4 potential sides
   - Subtract 1 for each adjacent land cell
3. Accumulate the exposed edges
4. Return total perimeter

## Performance

- **Time Complexity:** O(rows * cols)
- **Space Complexity:** O(1)

## Usage

```bash
./0-main.py
```

## Author
[Ermiyas Solomon]