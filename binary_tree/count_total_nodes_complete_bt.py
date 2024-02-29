# Created by Adarsh N B at 2/27/2024

# Description:
"""
Count number of nodes in a complete binary tree in less than O(n)
LC 222
Time complexity - O(logn)
Space complexity - O(h)
"""
from interview_problem_solutions.utils.tree import Node


def get_left_height(node: Node) -> int:
    count = 0

    while node.left:
        count += 1
        node = node.left

    return count


def get_right_height(node: Node) -> int:
    count = 0

    while node.right:
        count += 1
        node = node.right

    return count


def count_nodes(root: Node) -> int:

    if root is None:
        return 0

    left_tree_height = get_left_height(root.left)
    right_tree_height = get_right_height(root.right)

    if left_tree_height == right_tree_height:
        return 2**left_tree_height - 1

    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)
