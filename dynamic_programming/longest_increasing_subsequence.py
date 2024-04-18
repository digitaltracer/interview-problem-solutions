# Created by Adarsh N B at 11/15/2023

# Description:
"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
LC 300
"""

from typing import List


class Solution:

    def longest_increasing_subsequence_rec(self, nums: List[int]) -> int:
        return self.lis_rec_helper(0, -1, nums)

    def lis_rec_helper(self, ind: int, prev_index: int, nums: List[int]) -> int:
        if ind == len(nums):
            return 0

        pick = 0
        if prev_index == -1 or nums[prev_index] < nums[ind]:
            pick = 1 + self.lis_rec_helper(ind+1, ind, nums)

        not_pick = 0 + self.lis_rec_helper(ind+1, prev_index, nums)

        return max(pick, not_pick)

    def lis_tabular(self, nums: List) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.longest_increasing_subsequence_rec([10, 9, 2, 5, 3, 7, 101, 18]))
