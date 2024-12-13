#!/usr/bin/python3
"""
Prime Game Solution:
This module implements a game where players take turns removing prime numbers
and their multiples from a set of consecutive integers.
"""

def generate_primes(n):
    """
    Generate all prime numbers up to n using the Sieve of Eratosthenes.
    
    Args:
        n (int): The upper limit for generating primes
    
    Returns:
        list: A list of prime numbers less than or equal to n
    """
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use the Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Collect and return the list of primes
    return [num for num in range(2, n+1) if is_prime[num]]

def game_round(n):
    """
    Simulate a single round of the Prime Game.
    
    Args:
        n (int): The upper limit of consecutive integers
    
    Returns:
        str: Name of the winner ('Maria' or 'Ben')
    """
    # Get all primes up to n
    primes = generate_primes(n)
    
    # If no primes, Ben wins
    if not primes:
        return 'Ben'
    
    # Track removed numbers and keep track of moves
    removed = [False] * (n + 1)
    current_player = 'Maria'
    
    # Continue the game until no moves are possible
    while True:
        # Find the first valid prime move
        move_found = False
        for prime in primes:
            if prime <= n and not removed[prime]:
                # Remove the prime and its multiples
                removed[prime] = True
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                
                # Switch players
                current_player = 'Ben' if current_player == 'Maria' else 'Maria'
                move_found = True
                break
        
        # If no move is possible, previous player wins
        if not move_found:
            return 'Ben' if current_player == 'Maria' else 'Maria'

def isWinner(x, nums):
    """
    Determine the overall winner of multiple game rounds.
    
    Args:
        x (int): Number of game rounds
        nums (list): List of upper limits for each round
    
    Returns:
        str or None: Name of the player who won the most rounds
    """
    # Validate inputs
    if not nums or x <= 0:
        return None
    
    # Track wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    # Play each round and count wins
    for n in nums[:x]:
        winner = game_round(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    
    return None