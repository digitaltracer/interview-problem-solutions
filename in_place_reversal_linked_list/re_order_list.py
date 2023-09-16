# Created by Adarsh N B at 9/7/2023

# Description:
"""
Given the head of a singly linked list, reorder the list as if it were folded on itself.
This solution takes in 2 problems that are solved. i.e., reversing a linked list and finding the middle of the linked
list
"""

from interview_problem_solutions.utils.linked_list import LinkedList
from interview_problem_solutions.utils.linked_list_node import LinkedListNode
from interview_problem_solutions.utils.print_linked_list import print_list_with_forward_arrow


def reverse_linked_list(head: LinkedListNode) -> LinkedListNode:
    cur = head
    prev, nxt = None, None

    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    head = prev
    return head


def middle_of_linked_list(head: LinkedListNode) -> LinkedListNode:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def reorder_list(head: LinkedListNode) -> LinkedListNode:
    # We are merging the logic of the two methods above

    if not head:
        return head

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # now we have slow at the centre of the linked list
    # setting None to prev would break the linked list into two at centre
    prev, curr = None, slow

    # reversing the second half of linked list.
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    first, second = head, prev

    # now start re-ordering the linked list.
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head

# 1 -> 2 -> 3 -> 4 -> 5 -> 6


def re_order_list2(head: LinkedListNode) -> LinkedListNode:

    middle_node = middle_of_linked_list(head)

    reversed_second_half_head = reverse_linked_list(middle_node)
    # return reversed_second_half_head

    # cut the linked list in half
    reversed_second_half_head.next = None

    first, second = head, reversed_second_half_head

    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head


if __name__ == "__main__":
    lists = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    for i in lists:
        linked_list = LinkedList()
        linked_list.create_linked_list(i)
        print("first one")
        print_list_with_forward_arrow(reorder_list(linked_list.head))
        print("\nSecond one")
        print_list_with_forward_arrow(re_order_list2(linked_list.head))
        print()
