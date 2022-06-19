#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(dp)):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2] + cost[i-2])
            # return dp[i]
        return min(dp[-1] + cost[-1],dp[-2] + cost[-2])
# @lc code=end

