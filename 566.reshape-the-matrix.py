#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ori_rows = len(mat)
        ori_cols = len(mat[0])
        if ori_rows * ori_cols != r * c:
            return mat
        cur_row = []
        res = []
        for i in range(ori_rows):
            for j in range(ori_cols):
                cur_row.append(mat[i][j])
                if len(cur_row) == c: #distinguish between row and col
                    res.append(cur_row)
                    cur_row = []
        return res
        
# @lc code=end

