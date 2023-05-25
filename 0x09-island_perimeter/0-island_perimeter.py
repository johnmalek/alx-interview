#!/usr/bin/python3
"""
A python module
"""


def island_perimeter(grid):
    """
    a function that returns the perimeter
    of a grid
    args:
        grid: a list of list of integers
    returns:
        perimeter (int)
    """
    if not grid:
        return 0

    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                perimeter += 4

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
