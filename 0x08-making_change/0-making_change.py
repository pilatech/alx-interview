#!/usr/bin/python3
"""File for implementing 'makeChange' function
"""


def getLargest(coins, total):
    """get largest changeworthy coin
    Args:
        coins - (list) the coins to choose from
        total - (int) the amount to find change for
    """
    largest = 0
    for coin in coins:
        if coin <= total and coin > largest:
            largest = coin
    return largest


def makeChange(coins, total):
    """Determine minimum number of coins for a change
    Args:
        coins - (list) the coins we have
        total - (int) the amount we need change for
    """
    if total <= 0:
        return 0
    change = []
    while (total > 0):
        largest = getLargest(coins, total)
        if largest == 0:
            break
        change.append(largest)
        total -= largest
    if total > 0:
        return -1
    return len(set(change))
