# Created by Adarsh N B at 11/9/2023

# Description:
"""
Given a list of costs, you can start at either at index 0 or 1. get the min cost to reach the final floor (index+1)
"""

from typing import List


class Solution:
    """
    Its assumed that the costs list will at least be of length 2
    """
    @staticmethod
    def min_cost_climbing_stairs(costs: List[int]) -> int:
        costs.append(0)

        for i in range(len(costs) - 3, -1, -1):
            costs[i] += min(costs[i+1], costs[i+2])

        return min(costs[0], costs[1])
