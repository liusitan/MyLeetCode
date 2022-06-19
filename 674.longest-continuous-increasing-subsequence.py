#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        last = float('-inf')
        length = 0
        max_len = 0
        for i in nums:
            if i> last:
                length = length+1
            else:
                max_len = max(max_len,length)
                length = 1
            last = i
        max_len = max(max_len,length)
        return max_len

# @lc code=end

