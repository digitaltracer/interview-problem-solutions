# Created by Adarsh N B at 9/25/2023

# Description:
"""
Generate maximum returns with an initial capital c and given portfolios with profits and number of investments k
"""

from typing import List
from interview_problem_solutions.utils.min_heap import MinHeap
from interview_problem_solutions.utils.max_heap import MaxHeap


def maximum_capital(c: int, k: int, capitals: List[int], profits: List[int]) -> int:
    current_capital = c
    profits_max_heap = MaxHeap()
    capitals_min_heap = MinHeap()

    # adding index of the capital list as well, since the same index corresponds to the profit that capital gives
    for index, cap in enumerate(capitals):
        capitals_min_heap.insert((cap, index))

    for _ in range(k):

        while capitals_min_heap and capitals_min_heap.get_min()[0] <= current_capital:
            capital, index = capitals_min_heap.pop()
            # populate the profits max heap with the current capital
            profits_max_heap.insert(profits[index])

        # if there is no profit with the current capital you have.
        if not profits_max_heap:
            break

        current_capital += profits_max_heap.get_max()

    return current_capital


if __name__ == "__main__":
    inp = (
        (0, 1, [1, 1, 2], [1, 2, 3]),
        (1, 2, [1, 2, 2, 3], [2, 4, 6, 8]),
        (2, 3, [1, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
        (1, 3, [1, 2, 3, 4], [1, 3, 5, 7]),
        (7, 2, [6, 7, 8, 10], [4, 8, 12, 14]),
        (2, 4, [2, 3, 5, 6, 8, 12], [1, 2, 5, 6, 8, 9])
    )
    num = 1
    for i in inp:
        print(f"{num}.\tProject capital requirements:  {i[2]}")
        print(f"\tProject expected profits:      {i[3]}")
        print(f"\tNumber of projects:            {i[1]}")
        print(f"\tStart-up capital:              {i[0]}")
        print("\n\tMaximum capital earned: ",
              maximum_capital(i[0], i[1], i[2], i[3]))
        print("-" * 100, "\n")
        num += 1
