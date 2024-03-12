# Created by Adarsh N B at 3/4/2024

# Description:
"""
LC 131
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Time complexity - 
Space complexity - 
"""
from typing import List
from copy import deepcopy


def palindrome_partitioning(s: str) -> List[List[str]]:
    path: List[str] = []
    ans: List[List[str]] = []
    partition_string(s, 0, path, ans)
    return ans


def partition_string(s: str, ind: int, path: List[str], ans: List[List[str]]) -> None:
    if ind == len(s):
        ans.append(path)
        return

    for i in range(ind, len(s)):
        if is_palindrome(s, ind, i):
            path.append(s[ind: i+1])
            partition_string(s, i+1, deepcopy(path), ans)
            path.pop()


def is_palindrome(s: str, start: int, end: int) -> bool:
    # Since we are not caring about implementation of this, going to use string methods
    substr = s[start:end+1]
    return substr[:] == substr[::-1]


if __name__ == "__main__":
    print(palindrome_partitioning("aabb"))
