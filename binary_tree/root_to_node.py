# Created by Adarsh N B at 2/21/2024

# Description:
"""
Given a node (value in this case), find a path from root to the node.
(Assume node does not have a property called parent)

Time complexity - 
Space complexity - 
"""
from typing import List
from interview_problem_solutions.utils.tree import Node


def path_to_node(node: Node, target: int) -> List[int]:
    path = []
    node_path(node, path, target)
    return path


def node_path(node: Node, path: List[int], target: int) -> bool:
    if node is None:
        return False

    path.append(node.data)

    if node.data == target:
        return True

    if node_path(node.left, path, target) or node_path(node.right, path, target):
        return True

    path.pop()
    return False
