# Created by Adarsh N B at 2/28/2024

# Description:
"""
Construct a binary tree given preorder traversal and inorder traversal of the same tree
Time complexity - O(n)
Space complexity - O(h)
"""
from typing import List, Optional
from interview_problem_solutions.utils.tree import Node


def build_tree(preorder: List[int], inorder: List[int]) -> Node:
    in_map = {}
    for i, c in enumerate(inorder):
        in_map[c] = i

    root = build_tree_rec(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, in_map)
    return root


def build_tree_rec(preorder: List[int], pre_start: int, pre_end: int,
                   inorder: List[int], in_start: int, in_end: int,  in_map: dict) -> Optional[Node]:

    if pre_start > pre_end or in_start > in_end:
        return None

    root = Node(preorder[pre_start])
    inorder_root = in_map[preorder[pre_start]]
    left_length = inorder_root - in_start
    root.left = build_tree_rec(preorder, pre_start=pre_start+1, pre_end=pre_start+left_length,
                               inorder=inorder, in_start=0, in_end=inorder_root-1, in_map=in_map)
    
    root.right = build_tree_rec(preorder, pre_start=pre_start+left_length+1, pre_end=pre_end,
                                inorder=inorder, in_start=inorder_root+1, in_end=in_end, in_map=in_map)

    return root
