# Created by Adarsh N B at 2/26/2024

# Description:
"""
A binary tree is said to have children sum property if the sum of the children nodes' values sum to be the value of its
parent.

The problem here is to convert any binary tree to have this property by only incrementing the value of a node by 1
The question, however doesn't ask you to optimize the number of increments you do. But optimize the time complexity to
convert the tree to a children sum property binary tree
Time complexity - 
Space complexity - 
"""
from interview_problem_solutions.utils.tree import Node


def children_sum_property(root: Node) -> None:

    if root is None:
        return

    children_sum = 0

    if root.left:
        children_sum += root.left.data
    if root.right:
        children_sum += root.right.data

    if children_sum >= root.data:
        root.data = children_sum
    else:
        if root.left:
            root.left.data = root.data
        if root.right:
            root.right.data = root.data

    children_sum_property(root.left)
    children_sum_property(root.right)

    children_sum_recal = 0
    if root.left:
        children_sum_recal += root.left.data
    if root.right:
        children_sum_recal += root.right.data

    root.data = children_sum_recal
