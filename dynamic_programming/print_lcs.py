# Created by Adarsh N B at 3/7/2024

# Description:
"""
Same as longest common subsequence. There the output was the length of the lcs. Here print the actual string.
Time complexity - 
Space complexity - 
"""


def lcs_tabulation(s: str, t: str) -> str:
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

    lcs_length = dp[n][m]
    i = n
    j = m

    common_str = ""

    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            common_str = s[i-1] + common_str
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return common_str


if __name__ == "__main__":
    print(lcs_tabulation("abde", "qace"))
