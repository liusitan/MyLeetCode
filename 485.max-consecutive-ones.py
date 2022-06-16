#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc = 0
        c = 0
        for num in nums:
            if num == 0:
                maxc = max(maxc,c)
                c = 0
            else:
                c = c+1
        maxc = max(maxc,c)
        return maxc
# @lc code=end

