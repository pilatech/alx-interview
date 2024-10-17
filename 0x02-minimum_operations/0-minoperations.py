#!/usr/bin/pyton3
"""Find out the minimum operations"""


def minOperations(n):
    """Implement the mimimum operations
    Args:
        n(number) - number of commands
    Return:
        (number) - minimum operations
    """
    if n == 0:
        return 0
    else:
        return 1 + minOperations(n - 1)
