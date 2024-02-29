# Created by Adarsh N B at 1/12/2024

# Description:
"""
Given a nxm maze with obstacles, count and return the number of paths to reach the right bottom cell from top left cell.
A cell in the given maze has a value -1 if its a blockage or a dead end else 0.
You are allowed to move right or left.

(This is exactly similar to total unique paths, except we need to add a condition for the sum up.)

Time complexity - 
Space complexity - 
"""
from typing import List
from copy import deepcopy


def maze_obstacles_tabular(maze: List[List[int]]) -> int:
    m = len(maze)  # number of rows in the matrix
    n = len(maze[0])  # number of columns

    prev = [0] * n

    for i in range(m):
        curr = [0] * n
        for j in range(n):
            if i >= 0 and j >= 0 and maze[i][j] == -1:
                curr[j] = 0
            elif i == 0 and j == 0:
                curr[j] = 1
            else:
                up, left = 0, 0
                if i > 0:
                    up = prev[j]
                if j > 0:
                    left = curr[j-1]
                curr[j] = up + left
        prev = deepcopy(curr)

    return prev[n-1]


if __name__ == "__main__":
    maz = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
    print(maze_obstacles_tabular(maz))
