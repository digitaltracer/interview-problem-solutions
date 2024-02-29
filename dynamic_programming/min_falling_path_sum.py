# Created by Adarsh N B at 1/15/2024

# Description:
"""
LC 931
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that is either
directly below or diagonally left/right.
Specifically,the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)

Time complexity - 
Space complexity - 
"""
from typing import List
from copy import deepcopy
from sys import maxsize


def min_falling_path_sum_rec(matrix: List[List[int]]) -> int:
    # since its nxn matrix, just calculating either column length or row length would be enough.
    n = len(matrix)
    dp = []
    for _ in range(n):
        dp.append([maxsize for _ in range(n)])
    results = []
    for i in range(n):
        res = min_falling_path_sum_rec_helper(n - 1, i, matrix, deepcopy(dp))
        results.append(res)
    return min(results)


def min_falling_path_sum_rec_helper(i: int, j: int, matrix: List[List[int]], dp: List[List[int]]) -> int:
    if i < 0 or j >= len(matrix):
        return maxsize

    if i == 0:
        return matrix[0][j]

    if dp[i][j] != maxsize:
        return dp[i][j]

    up = matrix[i][j] + min_falling_path_sum_rec_helper(i - 1, j, matrix, dp)
    up_left = matrix[i][j] + min_falling_path_sum_rec_helper(i - 1, j - 1, matrix, dp)
    up_right = matrix[i][j] + min_falling_path_sum_rec_helper(i - 1, j + 1, matrix, dp)

    dp[i][j] = min(up, up_left, up_right)
    n = len(matrix)
    # TODO: there is something wrong with this solution. Keeping this on hold
    return dp[i][j]


def min_falling_path_sum_tab(matrix: List[List[int]]) -> int:
    # let's write a solution even for m x n matrix
    m = len(matrix)
    n = len(matrix[0])
    prev = matrix[0]
    for i in range(1, m):
        curr = [maxsize] * n
        for j in range(n):
            if j == 0:
                curr[j] = matrix[i][j] + min(prev[j], prev[j+1])
            elif j == n-1:
                curr[j] = matrix[i][j] + min(prev[j], prev[j-1])
            else:
                curr[j] = matrix[i][j] + min(prev[j-1], prev[j], prev[j+1])
        prev = [i for i in curr]
    return min(prev)


if __name__ == "__main__":
    matrices = [[[2, 1, 3], [6, 5, 4], [7, 8, 9]], [[-19, 57], [-40, -5]]]
    print([min_falling_path_sum_rec(m) for m in matrices])
    print([min_falling_path_sum_tab(m) for m in matrices])
