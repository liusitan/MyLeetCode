#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start



class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_len = len( matrix)
        col_len = len(matrix[0])
        for i in range(row_len):
            e = matrix[i][0]
            r = i
            c = 0
            while r + 1 < row_len and c + 1 < col_len:
                r = r + 1
                c = c + 1
                if e!= matrix[r][c]:
                    return False
        for j in range(col_len):
            e = matrix[0][j]
            r = 0
            c = j
            while r + 1 < row_len and c + 1 < col_len:
                r = r + 1
                c = c + 1
                if e!= matrix[r][c]:
                    return False
        return True
# @lc code=end

