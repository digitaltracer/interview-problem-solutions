# Created by Adarsh N B at 3/10/2024

# Description:
"""
A Subsequence of a string is the string that is obtained by deleting 0 or more letters from the string and keeping the
rest of the letters in the same order.
We are given two strings, 'string' and 'sub'. Find the number of subsequences of 'string' which are equal to 'sub'.

Time complexity - 
Space complexity - 
"""
from typing import List

"""
We have to find distinct subsequences of string that matches to sub. As there is no uniformity in data, there is no 
other way than trying out all the ways. (which means we will have to use recursion)
As usual, we will be using two indices on these two strings i and j.
Two scenarios are possible.
1. string[i] == sub[j]
        in which case we have two options. One is to match this character and another is to see if the jth char
        in sub will match with some other character in string. 
        In programming terms, two recursion calls will be made, f(i-1, j-1) and f(i-1, j)
2. string[i] != sub[j]
        here there is no other choice as we have to match the jth character. So we just call f(i-1, j)
"""


def distinct_subsequences_memoized(string: str, sub: str) -> int:
    n = len(string)
    m = len(sub)
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    return distinct_subsequences_memoized_helper(string, sub, n-1, m-1, dp)


def distinct_subsequences_memoized_helper(string: str, sub: str, i: int, j: int, dp: List[List[int]]) -> int:
    if j < 0:
        return 1

    if i < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if string[i] == sub[j]:
        option1 = distinct_subsequences_memoized_helper(string, sub, i-1, j-1, dp)
        option2 = distinct_subsequences_memoized_helper(string, sub, i-1, j, dp)
        dp[i][j] = option1 + option2

    else:
        dp[i][j] = distinct_subsequences_memoized_helper(string, sub, i-1, j, dp)

    return dp[i][j]


def distinct_subsequences_tabular(string: str, sub: str) -> int:
    n = len(string)
    m = len(sub)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    for j in range(1, m+1):
        dp[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if string[i-1] == sub[j-1]:
                op1 = dp[i-1][j-1]
                op2 = dp[i-1][j]
                dp[i][j] = op1 + op2
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][m]

def subsequenceCounting(s1, s2, n, m):
    # Initialize a DP table to store the count of distinct subsequences
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

    # Base case: There is exactly one subsequence of an empty string s2 in s1
    for i in range(n + 1):
        dp[i][0] = 1

    # Initialize dp[0][i] to 0 for i > 0 since an empty s1 cannot have a non-empty subsequence of s2
    for i in range(1, m + 1):
        dp[0][i] = 0

    # Fill in the DP table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the current characters match, we have two choices:
            # 1. Include the current character in both s1 and s2 (dp[i-1][j-1])
            # 2. Skip the current character in s1 (dp[i-1][j])
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) if s1[i - 1] == s2[j - 1] else dp[i - 1][j]

    # The final value in dp[n][m] is the count of distinct subsequences
    return dp[n][m]


if __name__ == "__main__":
    print(distinct_subsequences_tabular("babgbag", "bag"))
    print(distinct_subsequences_memoized("babgbag", "bag"))
    print(subsequenceCounting("babgbag", "bag", len("babgbag"), len("bag")))
