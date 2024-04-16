# Created by Adarsh N B at 2/28/2024

# Description:
"""
Serialize a binary tree to a string and when the same string is passed to the deseriazation method it should
return the binary tree.
Time complexity - O(n)
Space complexity - O(n)
"""
from queue import Queue
from interview_problem_solutions.utils.tree import Node

"""
                                                                                                                                                           
                +----------------------------------------------------------------------------+                                                             
                |   Perform depth first traversal and start serializing into a string/stream |                                                             
                |                                                                            |                                                             
                +----------------------------------------------------------------------------+                                                             
    -                                                   |                                                                                                  
                                                        |                                                                                                  
                   +--------------------------------------------------------------------------------+                                                      
                   |  Also serialize a marker to represent NULL pointer that helps in deserializing |                                                      
                   +-----------------------------------|--------------------------------------------+                                                      
                                                       |                                                                                                   
                                                       |                                                                                                   
-                           +---------------------------------------------------------+                                                                    
                            |Deserialize the string/stream using pre-order traversal  |                                                                    
                            +-------------------------|-------------------------------+                                                                    
                                                      |                                                                                                    
             -                                        |                                                                                                    
                  +----------------------------------------------------------------------------------------------+                                         
                  |During deserialization, create a new node for every non marker node using pre-order traversal |                                         
                  +----------------------------------------------------------------------------------------------+  

"""


def serialize_binary_tree(root: Node) -> str:
    res = ""
    if root is None:
        return res
    q = Queue()
    q.put(root)

    while q.not_empty:
        node = q.get()

        if node is None:
            res = res + "null "
            continue

        res = res + node.data + " "
        q.put(node.left)
        q.put(node.right)

    return res


def deserialize_binary_tree(node_str: str) -> Node:
    node_values = node_str.split(" ")

    root = Node(int(node_values[0]))
    i = 1
    q = Queue()
    q.put(root)
    while i < len(node_values):
        parent_root = q.get()
        if node_values[i] != "null":
            parent_root.left = Node(int(node_values[i]))
            q.put(parent_root.left)
        i += 1
        if node_values[i] != "null":
            parent_root.right = Node(int(node_values[i]))
            q.put(parent_root.right)

    return root
