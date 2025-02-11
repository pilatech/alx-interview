#!/usr/bin/python3
"""Module implementing Prime Game
"""


def isWinner(x, nums):
    """Finds the winner of of prime game after 'x' rounds.
    """
    if x < 1 or not nums:
        return None
    Maria_wins, Ben_wins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        Ben_wins += primes_count % 2 == 0
        Maria_wins += primes_count % 2 == 1
    if Maria_wins == Ben_wins:
        return None
    return 'Maria' if Maria_wins > Ben_wins else 'Ben'
