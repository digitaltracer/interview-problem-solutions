# Created by Adarsh N B at 2/24/2024

# Description:
"""
Given a binary tree, Find the Lowest Common Ancestor for two given Nodes p and q
The lowest common ancestor is defined between two nodes x and y as the lowest node in T that has both p and q as
descendants (where we allow a node to be a descendant of itself.)
Time complexity - 
Space complexity - 
"""
from typing import Optional
from interview_problem_solutions.utils.tree import Node

"""
The answer has to be in either left subtree or right subtree. If it isn't found in either then root is the LCA

"""


def lowest_common_ancestor(root: Node, p: Node, q: Node) -> Optional[Node]:
    if root is None or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # Left is None which means we couldn't find either p or q. So both of them have to be in right subtree
    if left is None:
        return right

    # right is None which means we couldn't find either p or q in right subtree. So, they will be in left subtree.
    if right is None:
        return left

    # Both have results. which means, one of them is in left and another in right subtree. which implies root is LCA
    else:
        # both left and right are not None
        return root
