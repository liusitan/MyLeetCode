#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        prev = 0
        rep = 0
        length = len(nums)
        total = 0
        for i in nums:
            if i== prev:
                rep  = i
                
            prev = i
            total+=i
        return [rep,length*(length+1)//2 - (total -rep) ]
# @lc code=end

