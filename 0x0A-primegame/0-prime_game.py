#!/usr/bin/python3
"""Prime Game Module"""

def is_prime(n):
    """
    Check if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    Determine the winner of the prime number game
    """
    if x == 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [i for i in range(1, n+1) if is_prime(i)]
        while primes:
            if len(primes) % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1
            prime = primes[0]
            primes = [i for i in primes if i % prime != 0]

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
