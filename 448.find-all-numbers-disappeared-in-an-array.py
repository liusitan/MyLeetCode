#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
import enum


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = [-1] * (len(nums) + 1)
        for num in nums:
            i = abs(num) - 1
            nums[i] = -abs(nums[i])
        return [i+1 for i,x in enumerate(nums) if x > 0]
# @lc code=end

