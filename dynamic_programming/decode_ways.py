# Created by Adarsh N B at 11/11/2023

# Description:
"""
Given the string in integers ex. "12324" where 1 -> A and 2 -> B so on, find the number of ways in which the
integer string can be decoded.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        first = second = 1  # initialising the first char of the string as this. since we are validating its not zero

        # base case to invalidate the decoding
        if s.startswith("0"):
            return 0

        second_digit_after_two = {"0", "1", "2", "3", "4", "5", "6"}

        for n in range(1, len(s)):
            if s[n] == "0":
                if s[n-1] == "0":
                    return 0
                tmp = max(second - 1, 1)
            elif s[n-1] == "1" or (s[n-1] == "2" and s[n] in second_digit_after_two):
                tmp = second + first
            else:
                tmp = second
            first = second
            second = tmp

        return second


if __name__ == "__main__":
    solution = Solution()

    qns = ["10", "2101", "2611055971756562"]
    for i in qns:
        print(solution.numDecodings(i))
