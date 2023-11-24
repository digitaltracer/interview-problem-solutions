# Created by Adarsh N B at 11/10/2023

# Description:
"""
Find the longest palindromic substring in a given string
"""
from typing import List


class Solution:

    @staticmethod
    def longest_palindromic_substring(string: str) -> str:

        result = ""
        result_length = 0

        # finding odd length palindromes
        left, right = 0, 0
        for i in range(len(string)-1):

            left = right = i

            while left >= 0 and string[left] == string[right] and right <= len(string)-1:
                cur_palindrome_length = (right-left) + 1
                if cur_palindrome_length > result_length:
                    result = string[left: right+1]
                    result_length = (right-left) + 1

                left -= 1
                right += 1

            left = i
            right = i + 1

            while left >= 0 and string[left] == string[right] and right <= len(string)-1:
                cur_palindrome_length = (right-left) + 1
                if cur_palindrome_length > result_length:
                    result = string[left: right+1]
                    result_length = (right-left) + 1

                left -= 1
                right += 1

        return result


if __name__ == "__main__":
    input_strs = ["ababac", "opinion", "cool", "reaccar"]
    print([Solution.longest_palindromic_substring(i) for i in input_strs])
