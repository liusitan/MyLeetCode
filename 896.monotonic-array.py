#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 0
        while i < (len(nums)-1) and nums[i]==nums[i+1] :
            i+=1
        if i >= len(nums)-1:
            return True
        direction = nums[i] > nums[i+1]
        for j in range(i, len(nums)-1):
            if nums[j] == nums[j+1]:
                continue
            if direction ^ (nums[j] >nums[j+1]):
                return False
        return True
# @lc code=end

