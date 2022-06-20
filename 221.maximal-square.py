#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows_len = len(matrix)
        cols_len = len(matrix[0])
        dp = [[0]*(cols_len+1) for i in range(rows_len+1)]
        max_side = 0
        for i in range(rows_len):
            for j in range(cols_len):
                if(matrix[i][j] == "1"):
                    dp[i+1][j+1] = min(dp[i][j+1],dp[i+1][j],dp[i][j]) + 1
                    max_side = max(max_side,dp[i+1][j+1])
        return max_side*max_side
# @lc code=end

