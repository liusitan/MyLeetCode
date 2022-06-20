#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x %2==0] + [x for x in nums if x%2==1]
# @lc code=end

