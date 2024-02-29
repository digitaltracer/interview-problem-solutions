# Created by Adarsh N B at 2/24/2024

# Description:
"""
Width - number of nodes that is possible to have in a level between any two nodes
Time complexity - 
Space complexity - 
"""
from queue import Queue
from interview_problem_solutions.utils.tree import Node
"""
The logic is to index the nodes and with that, the max width will be reduced to (node1_index - node2_index)+1
If you are going to index with 0 based indexing, the formula is 

         i
  2i+1      2i+2

For 1 based indexing it will be
         i
    2i      2i+1
    
But this approach will start storing a lot more memory than desired and has a possibility of overflow.
So, instead convert i to (i-min(index_of_level)) and then the children to 2i+1 and 2i+2
"""


class NodeIndexPair:

    def __init__(self, node: Node, index: int):
        self.node = node
        self.index = index


def max_width_of_binary_tree(root: Node):
    if root is None:
        return 0

    q = Queue()

    # adding (node, index_of_node)
    q.put(NodeIndexPair(root, 0))
    max_width = 0
    while not q.empty():
        queue_size = q.qsize()
        first = last = 0

        for i in range(queue_size):
            cur_node = q.get()
            min_index_of_level = 0
            if i == 0:
                min_index_of_level = cur_node.index
            ind = cur_node[1] - min_index_of_level
            if i == 0:
                first = ind
            if i == queue_size-1:
                last = ind

            if cur_node.node.left:
                q.put(NodeIndexPair(cur_node.node.left, (2*ind)+1))

            if cur_node.node.right:
                q.put(NodeIndexPair(cur_node.node.right, (2*ind)+2))

        max_width = max(max_width, last-first+1)
    return max_width
