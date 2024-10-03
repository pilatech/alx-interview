#!/usr/bin/python3
"""Create Pascal Triangle"""


def pascal_triangle(n):
    """Prints Pascal Triangle
    Args:
        n: number of lines
    Return:
        a list of sublist on n count representing Pascal Triangle
        or an empty list if n is less than or equal to 0
    """
    if n <= 0:
        return []
    return [1, 2, 3]
