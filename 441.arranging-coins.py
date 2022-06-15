#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        n = 2 *n 
        l = 0
        r = n//4+1
        while( l < r):
            m = (l+r)//2 + 1
            tmp = m * (m + 1)
            if tmp < n:
                l = m
            elif tmp == n:
                return m
            else:
                r = m - 1
        return l
s = Solution()
s.arrangeCoins(1)
# @lc code=end

