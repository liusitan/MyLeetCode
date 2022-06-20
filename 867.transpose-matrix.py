#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows_len = len(matrix)
        cols_len = len(matrix[0])
        res = [[0] * rows_len for i in range(cols_len)]
        for i in range(rows_len):
            for j in range(cols_len):
                print(i,j)
                res[j][i] = matrix[i][j]
        return res 
# @lc code=end

