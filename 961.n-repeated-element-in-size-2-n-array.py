#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        t = nums[0]
        n = 0
        for i in range(len(nums)-2):
            if nums[i]== nums[i+1] or nums[i] == nums[i+2]:
                return nums[i]
        return nums[-1]
# @lc code=end

