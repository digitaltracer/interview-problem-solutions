# Created by Adarsh N B at 3/7/2024

# Description:
"""
Given a rod of length ‘N’ units. The rod can be cut into different sizes and each size has a cost associated with it.
Determine the maximum cost obtained by cutting the rod and selling its pieces.

Note:
1. The sizes will range from 1 to ‘N’ and will be integers.
2. The sum of the pieces cut should be equal to ‘N’.
3. Consider 1-based indexing.
Time complexity - 
Space complexity - 
"""
from typing import List


def rod_cutting_rec(n: int, price: List[int]) -> int:
    return rod_cutting_rec_helper(n-1, n, price)


def rod_cutting_rec_helper(ind: int, remaining_length: int, price: List[int]) -> int:

    if ind == 0:
        return price[0] * remaining_length

    not_take = 0 + rod_cutting_rec_helper(ind-1, remaining_length, price)
    take = -100
    rod_length = ind + 1  # since we are using 1 based indexing.
    if remaining_length >= rod_length:
        take = price[ind] + rod_cutting_rec_helper(ind, remaining_length-rod_length, price)

    return max(take, not_take)


if __name__ == "__main__":
    print(rod_cutting_rec(5, [2, 5, 7, 8, 10]))
