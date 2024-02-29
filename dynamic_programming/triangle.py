# Created by Adarsh N B at 1/15/2024

# Description:
"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the
current row, you may move to either index i or index i + 1 on the next row.
1 <= triangle.length <= 200
-10**4 <= triangle[i][j] <= 10**4

Time complexity - 
Space complexity - 
"""
from typing import List
from sys import maxsize


def triangle_recursion(triangle: List[List[int]]) -> int:
    if len(triangle) == 1:
        return triangle[0][0]
    else:
        # since the sum won't be more than 10**7 initialising to that. we can use maxsize instead.
        d2 = [10**7]
        dp = [[10**7]]
        for i in range(2, len(triangle)+1):
            dp.append(d2 * i)
        return triangle_recursion_helper(0, 0, triangle, dp)


def triangle_recursion_helper(i: int, j: int, triangle: List[List[int]], dp: List[List[int]]) -> int:
    if i == len(triangle) - 1:
        return triangle[i][j]
    if j > i + 1:
        return maxsize

    if dp[i][j] != 10**7:
        return dp[i][j]

    down = triangle[i][j] + triangle_recursion_helper(i + 1, j, triangle, dp)
    diagonal = triangle[i][j] + triangle_recursion_helper(i + 1, j + 1, triangle, dp)
    return min(down, diagonal)


if __name__ == "__main__":
    triangles = [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], [[-10]]]
    for t in triangles:
        print(triangle_recursion(t))
