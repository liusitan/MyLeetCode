#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        l = len(nums)
        for i in range(1,l):
            res = res ^ nums[i]
        return res
s = Solution()
t1 = [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]

s.singleNumber(t1)
            
# @lc code=end

