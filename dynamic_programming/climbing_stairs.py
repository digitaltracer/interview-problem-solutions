# Created by Adarsh N B at 1/4/2024

# Description:
"""
You have been given a number of stairs. Initially you are at 0th stair and you need to reach the nth stair.
Each time you can climb either 1 or 2 steps. You are return the number of distinct ways in which you can climb
from 0th to nth stair.

Time complexity -
Space complexity -
"""
from typing import List


def count_distinct_ways_to_climb_stair_rec(n: int) -> int:

    dp = [-1] * (n+1)

    return count_distinct_ways_to_climb_stair_rec_mem(n, dp)


def count_distinct_ways_to_climb_stair_rec_mem(n: int, mem: List[int]) -> int:
    if n == 0 or n == 1:
        return 1

    if mem[n] != -1:
        return mem[n]

    left = count_distinct_ways_to_climb_stair_rec_mem(n - 1, mem)
    right = count_distinct_ways_to_climb_stair_rec_mem(n - 2, mem)

    mem[n] = left + right

    return mem[n]


def count_distinct_ways_to_climb_stair_tab(n: int) -> int:

    if n == 1:
        return 1

    prev = 0
    first = 1

    for i in range(n):
        res = prev + first
        prev = first
        first = res

    return first


if __name__ == "__main__":
    print(count_distinct_ways_to_climb_stair_rec(50))
    print(count_distinct_ways_to_climb_stair_tab(50))
