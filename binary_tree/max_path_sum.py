# Created by Adarsh N B at 2/21/2024

# Description:
"""
Self explanatory
Time complexity - 
Space complexity - 
"""
from typing import List
from interview_problem_solutions.utils.tree import Node


def max_path_sum(node: Node) -> int:
    max_sum = [0]
    max_sum_down(node, max_sum)
    return max_sum[0]


def max_sum_down(node: Node, max_sum: List[int]) -> int:
    if node is None:
        return 0

    left_sum = max(0, max_sum_down(node.left, max_sum))
    right_sum = max(0, max_sum_down(node.right, max_sum))

    max_sum[0] = max(max_sum[0], node.data + left_sum + right_sum)

    # you are choosing either right or left of the tree as you can traverse both in a path
    return node.data + max(left_sum, right_sum)
