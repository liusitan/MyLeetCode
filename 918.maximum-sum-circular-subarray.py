#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from typing import List


class Solution:
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total,cur_min, cur_max, max_sum, min_sum = 0,0,0,nums[0],nums[0]
        
        for n in nums: 
            cur_min = min(cur_min,0) + n 
            cur_max = max(cur_max,0) + n 
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
            total += n
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
        # total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        # for a in A:
        #     curMax = max(curMax + a, a)
        #     maxSum = max(maxSum, curMax)
        #     curMin = min(curMin + a, a)
        #     minSum = min(minSum, curMin)
        #     total += a
        # return max(maxSum, total - minSum) if maxSum > 0 else maxSum       
s = Solution()
input = [-5,4,-6]
print(s.maxSubarraySumCircular(input))
# @lc code=end

