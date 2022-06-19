#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from random import randrange
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k %(len(nums))
        n = len(nums)

        nums[:] = nums[n-k:] + nums[:n-k]

        
# @lc code=end

