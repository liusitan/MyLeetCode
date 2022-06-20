#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        def robhelper(nums):
            not_robbed = nums[0]
            robbed = nums[1]
            for i in range(2,len(nums)):
                tmp_not_robbed =not_robbed
                not_robbed = max(robbed,not_robbed)
                robbed = tmp_not_robbed+nums[i]
            return max(not_robbed,robbed)
        return max(robhelper(nums[:-1]),robhelper(nums[1:]))
s = Solution()
print(s.rob([1,2,3,1])  )       
# @lc code=end

