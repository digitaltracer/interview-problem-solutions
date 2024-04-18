# Created by Adarsh N B at 4/7/2024

# Description:
"""
LC 133
Given a reference of a node in a **connected** undirected graph.
Return the deep copy of the graph.

Each node in the graph contains a value(int) and a list(List[node]) of its neighbours.
For simplicity, each node's value is same as its index (1-indexed)
Time complexity - O(n+m)  n - number of nodes. m - number of edges
Space complexity - O(n)
"""
from typing import List, Optional
from __future__ import annotations
"""
It is important that its given as a connected graph. Otherwise with just a single node, it would not be possible
to clone the entire graph
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbours = []

    def set_neighbours(self, neighbours: List[Node]):
        self.neighbours = neighbours


def clone_graph(node: Node) -> Optional[Node]:
    if node is None:
        return node
    maps_node = {}
    return clone_node(node, maps_node)


def clone_node(node: Node, nodes_map: dict[Node, Node]) -> Node:
    new_node = Node(node.val)
    nodes_map[node] = new_node

    for nd in node.neighbours:
        if nodes_map.get(node):
            # just update the neighbors for new nodes
            new_node.neighbours.append(nodes_map.get(nd))
        else:
            new_node.neighbours.append(clone_node(nd, nodes_map))

    return new_node
