#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_len =len(matrix)
        cols_len = len(matrix[0])
        r = rows_len -1
        c = 0
        while r >= 0 and c <cols_len:
            if target == matrix[r][c]:
                return True
            if matrix[r][c] > target:
                r -=1
            else:
                c +=1
        return False
        
        
# @lc code=end

