# Created by Adarsh N B at 1/14/2024

# Description:
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the
sum of all numbers along its path.

Time complexity - 
Space complexity - 
"""
from typing import List
from copy import deepcopy
from sys import maxsize


def min_path_sum_rec(grid: List[List[int]]) -> int:

    m = len(grid)
    n = len(grid[0])
    d2 = [-1] * n
    dp = []
    for _ in range(m):
        dp.append(deepcopy(d2))
    return min_path_sum_rec_helper(m-1, n-1, grid, dp)


def min_path_sum_rec_helper(m: int, n: int, grid: List[List[int]], dp: List[List[int]]) -> int:

    if m == 0 and n == 0:
        return grid[0][0]

    if m < 0 or n < 0:
        return maxsize

    if dp[m][n] != -1:
        return dp[m][n]

    up = grid[m][n] + min_path_sum_rec_helper(m-1, n, grid, dp)
    left = grid[m][n] + min_path_sum_rec_helper(m, n-1, grid, dp)

    dp[m][n] = min(up, left)
    return dp[m][n]


def min_path_sum_tab(grid: List[List[int]]) -> int:

    m = len(grid)
    n = len(grid[0])
    prev = [maxsize] * n

    for i in range(m):
        curr = [maxsize] * n
        for j in range(n):
            up, left = maxsize, maxsize
            if i == 0 and j == 0:
                curr[j] = grid[0][0]
            else:
                if i > 0:
                    up = prev[j]
                if j > 0:
                    left = curr[j-1]
                curr[j] = grid[i][j] + min(up, left)
        prev = curr
    return prev[n-1]


if __name__ == "__main__":
    grd = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    expected = 7
    print(min_path_sum_rec(grd))
    print(min_path_sum_tab(grd))
