# 0x02. Minimum Operations

## Description
This project focuses on calculating the **minimum number of operations** required to achieve a given number of "H" characters in a text file using only two operations:
1. **Copy All**: Copies all the characters in the file.
2. **Paste**: Pastes the copied content into the file.

The goal is to determine the fewest steps needed to reach exactly `n` characters.

---

## Learning Objectives
- **Dynamic Programming**: Breaking down the problem into subproblems.
- **Prime Factorization**: Using prime factors to optimize the solution.
- **Greedy Algorithms**: Making the optimal choice at each step.
- **Python Programming**: Implementing loops, functions, and conditionals.

---

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3 (version 3.4.3)
- Code must follow **PEP 8** style guidelines (version 1.7.x)
- All files must be executable (`chmod +x`)
- The script must start with `#!/usr/bin/python3`
- A `README.md` file is mandatory

---

## Usage

### Input
- The function accepts a single integer, `n`, representing the target number of "H" characters.
- If `n < 2`, the function returns 0.

### Output
- The function returns the **minimum number of operations** required to achieve exactly `n` characters.

---

## Example

Create a test file called `0-main.py`:

```python
#!/usr/bin/python3
"""
Main file for testing the minOperations function
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

Make both files executable:
```bash
chmod +x 0-minoperations.py 0-main.py
```

Run the test:
```bash
./0-main.py
```

**Expected Output:**
```
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
Min # of operations to reach 9 char: 6
```

---

## How It Works
1. **Prime Factorization**:  
   - The function calculates the prime factors of `n`.
   - For each prime factor, it adds the factor value to the total operations.

2. **Why Prime Factorization?**  
   - The problem can be reduced to multiplying smaller groups to get `n`.  
   - This is equivalent to finding the sum of prime factors.

---

## Edge Cases
- If `n` is less than 2, return 0.
- The function handles both small and large values of `n` efficiently.

---

## Author
Ermiyas Solomon
This project is part of the **ALX Interview Preparation** track.