# Created by Adarsh N B at 3/7/2024

# Description:
"""
Given two strings, 's' and 't' with lengths 'm' and 'n', find the length of the 'Longest Common Subsequence'.
Time complexity - 
Space complexity - 
"""
from typing import List


def lcs_rec(s: str, t: str) -> int:
    # TC - O(nm)
    # SC - O(nm) + O(n+m) (stack space)
    dp = [[-1 for _ in range(len(s))] for _ in range(len(t))]
    return lcs_rec_helper(s, t, len(s)-1, len(t)-1, dp)


def lcs_rec_helper(s: str, t: str, ind1: int, ind2: int, dp: List[List[int]]) -> int:

    if ind1 < 0 or ind2 < 0:
        return 0

    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]

    if s[ind1] == t[ind2]:
        dp[ind1][ind2] = 1 + lcs_rec_helper(s, t, ind1-1, ind2-1, dp)
    else:
        try1 = lcs_rec_helper(s, t, ind1-1, ind2, dp)
        try2 = lcs_rec_helper(s, t, ind1, ind2-1, dp)
        dp[ind1][ind2] = max(try1, try2)

    return dp[ind1][ind2]


def lcs_tabulation(s: str, t: str) -> int:
    n = len(s)
    m = len(t)
    # we are going for m+1 and n+1 as we cannot check for -1 like we did in recursion
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n+1):
        dp[i][0] = 0

    for i in range(m+1):
        dp[0][i] = 0

    for ind1 in range(1, n+1):
        for ind2 in range(1, m+1):
            if s[ind1-1] == t[ind2-1]:
                dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
            else:
                dp[ind1][ind2] = max(dp[ind1-1][ind2], dp[ind1][ind2-1])

    return dp[n][m]
