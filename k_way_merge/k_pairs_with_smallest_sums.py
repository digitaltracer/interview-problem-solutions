# Created by Adarsh N B at 10/5/2023

# Description:
"""

"""
from interview_problem_solutions.utils.min_heap import MinHeap


def k_smallest_pairs(list1, list2, k):
    list_length = len(list1)
    min_heap = MinHeap()
    pairs = []

    for i in range(min(k, list_length)):
        min_heap.insert((list1[i] + list2[0], i, 0))

    counter = 1

    while min_heap and counter <= k:
        least_pair_sum, i, j = min_heap.pop()
        pairs.append([list1[i], list2[j]])

        j += 1

        if len(list2) > j:
            min_heap.insert((list1[i] + list2[j], i, j))

        counter += 1

    return pairs


if __name__ == "__main__":
    list1 = [[2, 8, 9],
             [1, 2, 300],
             [1, 1, 2],
             [4, 6],
             [4, 7, 9],
             [1, 1, 2]]

    list2 = [[1, 3, 6],
             [1, 11, 20, 35, 300],
             [1, 2, 3],
             [2, 3],
             [4, 7, 9],
             [1]]

    k = [9, 30, 1, 2, 5, 4]

    for i in range(len(k)):
        print(i + 1, ".\t Input pairs: ", list1[i], ", ", list2[i],
              f"\n\t k = {k[i]}", sep="")
        print("\t Pairs with the smallest sum are: ",
              k_smallest_pairs(list1[i], list2[i], k[i]), sep="")
        print("-" * 100)
