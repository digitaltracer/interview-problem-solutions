# Created by Adarsh N B at 2/28/2024

# Description:
"""
Construct a unique binary tree given inorder and post order traversals of a binary tree
Time complexity - O(n)
Space complexity - O(h)
"""
from typing import List, Optional
from interview_problem_solutions.utils.tree import Node


def build_tree(inorder: List[int], postorder: List[int]) -> Node:

    in_map = {}
    for i, c in inorder:
        in_map[c] = i

    root = build_tree_rec(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, in_map)
    return root


def build_tree_rec(inorder: List[int], in_start: int, in_end: int,
                   postorder: List[int], post_start: int, post_end: int, in_map: dict) -> Node:
    root = Node(postorder[post_end])

    root_index = in_map[root.data]
    left_length = root_index - in_start

    root.left = build_tree_rec(inorder, in_start=in_start, in_end=root_index-1, postorder=postorder,
                               post_start=post_start, post_end=post_start+left_length-1, in_map=in_map)

    root.right = build_tree_rec(inorder, in_start=root_index+1, in_end=in_end, postorder=postorder,
                                post_start=post_start+left_length, post_end=post_end-1, in_map=in_map)

    return root
