# Created by Adarsh N B at 3/2/2024

# Description:
"""
LC 51
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate
a queen and an empty space, respectively.
Time complexity - 
Space complexity - 
"""
from typing import List
from copy import deepcopy
"""
The logic here is to start placing the queen column by column and check if the current position gets attacked by
any queens placed before that. If that doesn't work, remove the current placement and move on to the next option.

The challenge here is to find if the current placed queen gets attacked by any queens placed before. If so, go back
Now, queen can attack in 8 directions, but since we don't need to check for the columns that will be placed, and 
only one queen will be placed in a column, the number of directions in reduced to 3. 
Left, Left upper diagonal and left lower diagonal.

Now, bruteforce method is exponential in nature. So by summing up column and row value (0 to n-1), we can observe
the following.
Left row -> Array of size n indicating which row has been occupied. When a Q is placed in a particular column on some
row, this row number is marked as true.
Left lower diagonal -> Array of size (2n-1).If you sum up row and column in the nxn board, you'll notice the left
lower diagonal values are the same. So, when you place a Q, you mark up (row+column) value to true 
Left Upper diagonal ->   Like described in the above, (n-1 + col - row)
"""


def solve_n_queens(n: int) -> List[List[str]]:
    ans: List[List[str]] = []
    board: List[str] = ["." * n for _ in range(n)]

    row = [True] * n
    upper_diagonal = [True] * (2*n-1)
    lower_diagonal = [True] * (2*n-1)

    solve(0, board, ans, row, upper_diagonal, lower_diagonal, n)
    return ans


def solve(col: int, board: List[str], ans: List[List[str]], left_row: List[bool], upper_diagonal: List[bool],
          lower_diagonal: List[bool], n: int) -> None:

    if col == n:
        ans.append(board)
        return

    for row in range(n):
        if left_row[col] and upper_diagonal[n+1+col-row] and lower_diagonal[row+col]:
            left_row[col] = upper_diagonal[n+1+col-row] = lower_diagonal[row+col] = False
            row_board = board[row]
            row_board_updated = row_board[:col] + "Q" + row_board[col+1:]
            board[row] = row_board_updated
            solve(col+1, deepcopy(board), ans, deepcopy(left_row), deepcopy(upper_diagonal),
                  deepcopy(lower_diagonal), n)
            # if the question suggests return any one of the possible placements, we would not be going through if
            # the above function returns true
            board[row] = row_board
            left_row[col] = upper_diagonal[n + 1 + col - row] = lower_diagonal[row + col] = True


"""
The above solution tried to place queen column wise. Let's take an approach where we will start placing the queen
row wise.
Like mentioned above, the main challenge here is to make sure the current placed queen is not attacked by previously
placed queens. Now since we are placing queen row-wise, the directions that we should check for are.
1. same column -> old column != new proposed column
2. left down diagonal -> to check for diagonal, let's see 
3. right down diagonal
"""
