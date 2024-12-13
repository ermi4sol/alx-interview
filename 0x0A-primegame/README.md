# Prime Game Project

## Overview
This project implements a strategic game where two players, Maria and Ben, compete by removing prime numbers and their multiples from a set of consecutive integers. The game tests algorithmic thinking, prime number generation, and game theory principles.

## Project Description
In the Prime Game, two players take turns selecting prime numbers from a set of consecutive integers from 1 to n. After a player chooses a prime number, they remove that number and all of its multiples from the set. The player who cannot make a move loses the game.

## Features
- Efficient prime number generation using the Sieve of Eratosthenes
- Optimal game strategy implementation
- Supports multiple game rounds with different set sizes
- Determines the overall winner based on the most wins

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- No external package dependencies

## Installation
1. Clone the repository
```bash
git clone https://github.com/ermi4sol/alx-interview.git
cd alx-interview/0x0A-primegame
```

2. Ensure the script is executable
```bash
chmod +x 0-prime_game.py
```

## Usage
Import and use the `isWinner()` function:
```python
#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner

# Example usage
x = 3
nums = [4, 5, 1]
winner = isWinner(x, nums)
print(f"Winner: {winner}")
```

## Algorithm Explanation
### Prime Number Generation
The project uses the Sieve of Eratosthenes algorithm to efficiently generate prime numbers:
- Creates a boolean array to mark prime and non-prime numbers
- Eliminates multiples of each prime number
- Time Complexity: O(n log log n)
- Space Complexity: O(n)

### Game Strategy
- Players alternate turns
- Each player removes the smallest available prime number and its multiples
- The player unable to make a move loses the round
- The overall winner is determined by the most rounds won

## Performance
- Supports up to 10,000 rounds
- Handles sets of consecutive integers up to 10,000
- Optimized for computational efficiency

## Constraints
- x (number of rounds) ≤ 10,000
- n (set size) ≤ 10,000
- No external package imports allowed

## Example
```python
# Example rounds
x = 3
nums = [4, 5, 1]
result = isWinner(x, nums)
# Expected output: "Ben"
```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Authors
[Ermiyas Solomon]