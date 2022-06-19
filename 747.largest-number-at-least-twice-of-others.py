#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
from numpy import s_


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # if len(nums)==2:
        #     if nums[0] >= 2* nums[1]:
        #         return 0
        #     if 2*  nums[0] <= nums[1]:
        #         return 1
        #     return 0 
        largest = -1
        s_largest = -1
        largest_idx = -1
        for i,n in enumerate(nums): 
            if n > largest: 
                s_largest  = largest
                largest = n
                largest_idx = i 
            elif n > s_largest:
                s_largest = n
        return -1 if 2*s_largest > largest else largest_idx
                
# @lc code=end

