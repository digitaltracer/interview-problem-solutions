# Created by Adarsh N B at 11/15/2023

# Description:
"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
LC: 152
"""
from typing import List


class Solution:

    @staticmethod
    def max_product_subarray(nums: List[int]) -> int:
        cur_max = cur_min = 1
        res = max(nums)

        for num in nums:
            if num == 0:
                cur_max = cur_min = 1
            tmp = cur_max * num
            cur_max = max(tmp, num * cur_min, num)
            cur_min = min(tmp, num*cur_min, num)
            res = max(res, cur_max)

        return res
