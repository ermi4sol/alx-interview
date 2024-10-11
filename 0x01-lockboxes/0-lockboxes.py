#!/usr/bin/python3
"""
This module contains the `canUnlockAll` function which determines if all boxes
in a list of lists can be unlocked using the keys found within the boxes.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes: A list of lists, where each sublist represents the keys in that box.

    Returns:
        True if all boxes can be unlocked, False otherwise.
    """
    # Number of boxes
    n = len(boxes)
    
    # Set to keep track of which boxes have been opened
    opened_boxes = set([0])  # We can always open box 0
    keys = [0]  # Stack/queue to explore new boxes (starting from box 0)
    
    # Continue exploring while there are keys to use
    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes and key < n:
                # If we find a new box that hasn't been opened, open it and explore it
                opened_boxes.add(key)
                keys.append(key)
    
    # If all boxes are opened, return True
    return len(opened_boxes) == n

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
    print(canUnlockAll(boxes))  # True

    boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[0]]
    print(canUnlockAll(boxes))  # True

    boxes = [[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], 
             [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], 
             [9, 5, 8, 8], [6, 2, 8, 6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], 
             [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], 
             [4, 2, 9, 6, 6, 5, 5]]
    print(canUnlockAll(boxes))  # True
