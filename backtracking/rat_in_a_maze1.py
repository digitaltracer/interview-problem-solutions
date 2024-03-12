# Created by Adarsh N B at 3/4/2024

# Description:
"""
Consider a rat placed at (0, 0) in a square matrix of (n x n). It has to reach its destination (n-1, n-1).
Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can
move are U(up), D(own), R(ight) and L(eft).
Value 0 at a cell in the matrix represents that the path is blocked and rat cannot move to it while value 1 at a cell
in the matrix represents that the rat can travel through it.
Note: In a path, no cell can be visited twice.
The output should be printed in lexicographical (sorted) order.
Time complexity - 
Space complexity - 
"""
from typing import List, Set, Tuple

"""
The method is simple just like others. Starting at (0, 0) you start by trying to move every direction that's possible.
But since the solution requires us to return in a lexicographical order, one way is to have a result and then sort it.
But we can avoid it, if we start our attempts by D then L then R and then U. By doing this we don't have a need
to sort at the end.
"""


def rat_in_maze(matrix: List[List[int]], n: int) -> List[str]:
    ans: List[str] = []
    if matrix[0][0] != 1:
        return ans
    visited_indices: Set[Tuple[int, int]] = set()
    # This is to calculate the next index/point based on the movement. For ex. Down -> x = x+1, y = y +0
    dx = [+1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    rat_helper(0, 0, "", ans, visited_indices, dx, dy, matrix, n)
    return ans


def rat_helper(x: int, y: int, cur_path: str, ans: List[str], visited: Set[Tuple[int, int]], dx: List[int],
               dy: List[int], matrix: List[List[int]], n: int) -> None:
    if x == y == n-1:
        ans.append(cur_path)
        return

    directions = "DLRU"
    for ind in range(4):
        nxt_x: int = x + dx[ind]
        nxt_y: int = y + dy[ind]
        if 0 <= nxt_y < n and 0 <= nxt_x < n and matrix[nxt_x][nxt_y] == 1 and (nxt_x, nxt_y) not in visited:
            cur_path = cur_path + directions[ind]
            visited.add((nxt_x, nxt_y))
            rat_helper(nxt_x, nxt_y, cur_path, ans, visited, dx, dy, matrix, n)
            cur_path = cur_path[:-1]
            visited.remove((nxt_x, nxt_y))


if __name__ == "__main__":
    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    n = 4
    res = rat_in_maze(m, n)
    print(res)
