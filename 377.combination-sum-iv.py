#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], m: int) -> int:
        dp = [0] * (m+1)
        dp[0] = 1
        for i in range(1,m+1):
            for n in nums:
                if i >=n :
                    dp[i] += dp[i-n]
        return dp[m]
# @lc code=end

