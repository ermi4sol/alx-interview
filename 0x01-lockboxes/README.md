# Lockboxes Problem

## Description
This project provides a solution to the "Lockboxes" problem. Given a series of locked boxes, each containing a set of keys, the goal is to determine if all the boxes can be opened. Each box is numbered sequentially, and keys are represented by integers. A key with the number `i` opens the corresponding box `i`.

The first box is always unlocked (box 0). The task is to check whether it's possible to open all the boxes using the keys found inside the boxes.

## Function Prototype
```python
def canUnlockAll(boxes)
```

### Parameters:
- `boxes`: A list of lists, where each inner list contains integers representing keys to other boxes.

### Return:
- `True` if all boxes can be opened.
- `False` if some boxes remain locked.

## Example
```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- Code must adhere to the PEP 8 style guide (version 1.7.x)
- A `README.md` file at the root of the folder is mandatory
- All files should be executable
- The first line of all Python files must be `#!/usr/bin/python3`
- All files should end with a new line

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alx-interview.git
   ```
2. Navigate to the directory:
   ```bash
   cd alx-interview/0x01-lockboxes
   ```
3. Run the test file:
   ```bash
   ./main_0.py
   ```

## Files
- `0-lockboxes.py`: Contains the implementation of the `canUnlockAll` function.
- `main_0.py`: Example test cases to demonstrate how the function works.
- `README.md`: Project documentation.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
