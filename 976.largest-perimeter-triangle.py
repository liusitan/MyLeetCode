#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums,reverse=True)
        for i in range(len(nums)-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i+1]+nums[i+2] + nums[i]
        return 0
# @lc code=end

