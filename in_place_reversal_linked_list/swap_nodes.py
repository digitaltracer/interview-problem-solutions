# Created by Adarsh N B at 9/10/2023

# Description:
"""
Given the linked list and an integer k, return the head of the linked list after swapping the values of the kth node
from the beginning and the kth node from the end of the linked list

Time complexity - O(n)
"""
from interview_problem_solutions.utils.linked_list import LinkedList
from interview_problem_solutions.utils.linked_list_node import LinkedListNode
from interview_problem_solutions.utils.print_linked_list import print_list_with_forward_arrow


def swap_nodes(head: LinkedListNode, k: int) -> LinkedListNode:
    counter = 1
    cur_node = head

    while counter < k:
        cur_node = cur_node.next
        counter += 1

    front = cur_node
    # now we have the counter set to kth and the node for reference as well

    end = head

    while cur_node.next:
        cur_node, end = cur_node.next, end.next

    tmp = front.data
    front.data = end.data
    end.data = tmp
    return head


if __name__ == "__main__":
    input_list = [
        [1, 2, 3, 4, 5, 6, 7],
        [6, 9, 3, 10, 7, 4, 6],
        [6, 9, 3, 4],
        [6, 2, 3, 6, 9],
        [6, 2]
    ]
    k_int = [2, 3, 2, 3, 1]
    for index, inp in enumerate(input_list):
        li_list = LinkedList()
        li_list.create_linked_list(inp)
        print_list_with_forward_arrow(swap_nodes(li_list.head, k_int[index]))
        print()
