# Created by Adarsh N B at 3/7/2024

# Description:
"""

Time complexity - 
Space complexity - 
"""


def longest_common_substring(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)
    
    # let's take the tabulation approach since it's very similar to LCS
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = 0

    # if the question asks for the actual substring instead of 

    return max([max(dp[i]) for i in range(n+1)])


if __name__ == "__main__":
    s1 = "abcjklp"
    s2 = "acjkp"

    print("The Length of Longest Common Substring is", longest_common_substring(s1, s2))
