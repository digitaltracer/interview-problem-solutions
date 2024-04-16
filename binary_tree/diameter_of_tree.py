# Created by Adarsh N B at 4/13/2024

# Description:
"""
Given a binary tree, you need to compute the length of the tree’s diameter. The diameter of a binary tree is the
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
Time complexity - O(n)
Space complexity - O(n)
"""
from typing import List
from interview_problem_solutions.utils.tree import Node, BinaryTree


def diameter_of_tree(root: Node) -> int:
    diameter = [0]
    return get_height(root, diameter)


def get_height(node: Node, diameter: List[int]) -> int:
    if node is None:
        return 0

    left_height = get_height(node.left, diameter)
    right_height = get_height(node.right, diameter)

    diameter[0] = max(diameter[0], max(left_height, right_height))

    return 1 + diameter[0]


if __name__ == "__main__":
    tree = BinaryTree([1, 2, 3, 4, 5, 6])
    print(diameter_of_tree(tree.root))
