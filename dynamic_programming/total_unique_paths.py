# Created by Adarsh N B at 1/12/2024

# Description:
"""
You are present at point a which is the top left cell of an mxn matrix. Your destination is point b which is the
bottom right cell of the same matrix.
Your task is to find total number of unique paths from point a to point b.
You can either move right or down at each step.

Time complexity - 
Space complexity - 
"""
from typing import List
from copy import deepcopy


def total_unique_paths_rec(m: int, n: int) -> int:

    d2 = [-1] * m
    dp = []
    for _ in range(n):
        dp.append(deepcopy(d2))

    dp = [[-1, -1], [-1, -1]]

    res = total_unique_paths_rec_helper(m-1, n-1, dp)
    print(dp)
    return res


def total_unique_paths_rec_helper(m: int, n: int, dp: List[List[int]]) -> int:

    if m == 0 and n == 0:
        return 1

    if m < 0 or n < 0:
        return 0

    for i in range(m):
        for j in range(n):
            if dp[i][j] != -1:
                return dp[i][j]

            up = total_unique_paths_rec_helper(i-1, j, dp)
            left = total_unique_paths_rec_helper(i, j-1, dp)
            dp[i][j] = up + left
    return dp[m-1][n-1]


def total_unique_paths_tab(m: int, n: int) -> int:
    prev = [0] * n

    for i in range(m):
        curr = [0] * n
        for j in range(n):
            up, left = 0, 0
            if i > 0:
                up = prev[j]
            if j > 0:
                left = curr[j-1]
            if i == 0 and j == 0:
                curr[j] = 1
            else:
                curr[j] = up + left
        prev = deepcopy(curr)
    print(prev)
    return prev[n-1]


if __name__ == "__main__":
    print(total_unique_paths_rec(2, 2))
    print(total_unique_paths_tab(2, 2))
    print(total_unique_paths_tab(3, 2))
