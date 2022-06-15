#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        x = [0] *(n+1)
        for i in range(n+1):
            x[i] = x[i//2] + i %2
        return x
            
# @lc code=end

