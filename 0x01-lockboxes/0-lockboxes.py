def canUnlockAll(boxes):
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

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
