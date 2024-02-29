# Created by Adarsh N B at 2/24/2024

# Description:
"""

Time complexity - 
Space complexity - 
"""
from typing import Optional
from interview_problem_solutions.utils.tree import Node


def lowest_common_ancestor(root: Node, p: Node, q: Node) -> Optional[Node]:
    if root is None or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left is None:
        return right

    if right is None:
        return left

    else:
        # both left and right are not None
        return root
