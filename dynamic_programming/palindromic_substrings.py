# Created by Adarsh N B at 11/11/2023

# Description:
"""

"""


class Solution:

    def count_palindromes(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd length palindromes
            res += self.palindromes_count(s, left_pointer=i, right_pointer=i)
            # right length palindromes
            res += self.palindromes_count(s, left_pointer=i, right_pointer=i+1)

        return res

    @staticmethod
    def palindromes_count(s: str, left_pointer: int, right_pointer: int) -> int:
        res = 0

        while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
            res += 1
            left_pointer -= 1
            right_pointer += 1

        return res


if __name__ == "__main__":
    input_strs = ["ababac", "opinion", "cool", "reaccar"]
    print([Solution().count_palindromes(i) for i in input_strs])
