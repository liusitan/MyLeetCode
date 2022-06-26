#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
from numpy import str0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        sold = 0
        rest = 0
        for i,p in enumerate(prices):
            prevhold = hold
            hold = max(hold,rest - p)
            rest = max(rest,sold)
            sold = prevhold + p
        return max(sold,rest)
# @lc code=end

