# Created by Adarsh N B at 1/16/2024

# Description:
"""
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of
cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located in the top-left corner (0, 0), and
Robot #2 is located in the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.

Time complexity - 
Space complexity - 
"""
from typing import List
from copy import deepcopy


def cherry_pickup_rec(grid: List[List[int]]) -> int:
    # we need dp[rows][cols][cols]
    cols = len(grid[0])
    rows = len(grid)
    dp = []
    d2 = []
    for _ in range(cols):
        d2.append([-10**10 for _ in range(cols)])
    for _ in range(rows):
        dp.append(deepcopy(d2))
    return cherry_pickup_rec_helper(0, 0, len(grid[0]) - 1, rows, cols, grid, dp)


def cherry_pickup_rec_helper(i: int, j1: int, j2: int, rows: int, columns: int,
                             grid: List[List[int]], dp: List[List[List[int]]]) -> int:

    if j1 < 0 or j1 >= columns or j2 < 0 or j2 >= columns:
        return -10 ** 10

    if dp[i][j1][j2] != -10**10:
        return dp[i][j1][j2]

    if i == rows - 1:
        if j1 == j2:
            return grid[i][j1]
        else:
            return grid[i][j1] + grid[i][j2]

    max_sum = -10 ** 10

    for dj1 in range(-1, 2):
        for dj2 in range(-1, 2):
            if j1 == j2:
                new_sum = grid[i][j1] + cherry_pickup_rec_helper(i + 1, j1 + dj1, j2 + dj2, rows, columns, grid, dp)
            else:
                new_sum = grid[i][j1] + grid[i][j2] + cherry_pickup_rec_helper(i + 1, j1 + dj1, j2 + dj2,
                                                                               rows, columns, grid, dp)
            max_sum = max(max_sum, new_sum)
    dp[i][j1][j2] = max_sum
    return dp[i][j1][j2]


if __name__ == "__main__":
    grd = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(cherry_pickup_rec(grd))
