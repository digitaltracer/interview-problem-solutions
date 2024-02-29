# Created by Adarsh N B at 1/6/2024

# Description:
"""
A frog is crossing a river. The river is divided into some number of units, and at each unit,
there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
Given a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by
landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units.
The frog can only jump in the forward direction.

Time complexity - 
Space complexity - 
"""
from typing import List


def frog_jump(stones: List[int]) -> bool:
    current_index = 1
    prev_index = 0
    return helper(stones, prev_index, current_index)


def helper(stones: List[int], prev_index: int, current_index: int) -> bool:

    if current_index == len(stones) -1:
        return True

    last_jump = stones[current_index] - stones[prev_index]

    next_index = current_index + 1

    new_jump_dist = stones[next_index] - stones[current_index]

    if new_jump_dist in {last_jump-1, last_jump, last_jump+1}:
        pass

