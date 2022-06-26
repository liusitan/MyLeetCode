#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        j = 0; 
        for i in range(1,n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i-j*j]+1,dp[i])
                j+=1
        
        return dp[-1]
s = Solution()
print(s.numSquares(12))
             
# @lc code=end

