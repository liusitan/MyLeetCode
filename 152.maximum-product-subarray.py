#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax = nums[0]
        imin = nums[0]
        gmax = nums[0]
        for i in nums[1:]:
            candidate = (imax * i, imin*i, i )
            imax = max(candidate)
            imin = min(candidate)
            gmax = max(imax,gmax)
        return gmax
        
# @lc code=end

