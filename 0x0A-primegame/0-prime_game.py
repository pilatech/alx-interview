#!/usr/bin/python3
"""Module implementing Prime Game."""


def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Get list of prime numbers in a range"""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes


def isWinner(x, nums):
    """Function for finding the winner
    """
    times_maria_won = 0
    times_ben_won = 0

    for num in nums:
        set_rounds = list(range(1, num + 1))
        set_primes = primes_in_range(1, num)

        if not set_primes:
            times_ben_won += 1
            continue

        is_maria_turn = True

        while (True):
            if not set_primes:
                if is_maria_turn:
                    times_ben_won += 1
                else:
                    times_maria_won += 1
                break

            smallest_prime = set_primes.pop(0)
            set_rounds.remove(smallest_prime)

            set_rounds = [x for x in set_rounds if x % smallest_prime != 0]

            is_maria_turn = not is_maria_turn

    if times_maria_won > times_ben_won:
        return "Winner: Maria"

    if times_maria_won < times_ben_won:
        return "Winner: Ben"

    return None
