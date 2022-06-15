#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = n
        return num > 0 and (num&(num-1)) == 0 and (num & 0x55555555) != 0;
# @lc code=end

