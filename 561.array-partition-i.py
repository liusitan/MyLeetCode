#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#

# @lc code=start
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        rsnums = sorted(nums,reverse=True)
        res = 0
        for i in range(1,len(rsnums),2):
            res += rsnums[i]
        return res
s = Solution()
print(s.arrayPairSum([1,4,3,2]))
# @lc code=end

