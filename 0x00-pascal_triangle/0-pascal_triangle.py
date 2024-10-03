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
    pascal = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                if j == 1 or j == (i - 1):
                    row.append(i)
                else:
                    row.append(6)
        pascal.append(row)
    return pascal
