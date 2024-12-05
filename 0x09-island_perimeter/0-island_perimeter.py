#!/usr/bin/python3
"""Module for working out island perimeter"""


def island_perimeter(grid):
    """Function for working out island perimeter
       Args:
        grid - a list of list of integers
       Return:
        (int) - island perimeter
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                total = 4
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    total -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    total -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    total -= 1
                if i > 0 and grid[i - 1][j] == 1:
                    total -= 1
                perimeter += total
    return perimeter
