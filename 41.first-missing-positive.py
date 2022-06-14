#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) 
        nums.append(0)
        for i in range(0,n+1):
            while(nums[i] >= 0 and nums[i] <= n and nums[i] !=nums[nums[i]]):
                nums[nums[i]],nums[i] = nums[i], nums[nums[i]]
        for i in range(1,n+1):
            if(nums[i] <= 0 or nums[i] != i):
                return i
        return n+1; 
s = Solution()

nums = [3,1]

print(s.firstMissingPositive(nums))
# @lc code=end

