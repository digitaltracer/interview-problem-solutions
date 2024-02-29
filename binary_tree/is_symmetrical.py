# Created by Adarsh N B at 2/21/2024

# Description:
"""

Time complexity - 
Space complexity - 
"""
from interview_problem_solutions.utils.tree import Node


def is_symmetrical(node: Node) -> bool:
    return node is None or is_symmetrical_helper(node.left, node.right)


def is_symmetrical_helper(left_node: Node, right_node: Node) -> bool:
    if left_node is None or right_node is None:
        return left_node == right_node

    return left_node.data == right_node.data and is_symmetrical_helper(left_node.left, right_node.right) and \
        is_symmetrical_helper(left_node.right, right_node.left)
