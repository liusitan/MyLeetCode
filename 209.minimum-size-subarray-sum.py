#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        nums_len = len(nums)
        sum = 0
        maxl = 1<<30
        for r in range(nums_len):
            sum += nums[r]
            while sum - nums[l] >= target:
                sum -= nums[l]
                l+=1
            if sum >= target:
                maxl = min(maxl,r-l +1) 
        sum += nums[l]
        return maxl if maxl!=(1<<30) else 0
s = Solution()
s.minSubArrayLen(7, [2,3,1,2,4,3])
# @lc code=end

