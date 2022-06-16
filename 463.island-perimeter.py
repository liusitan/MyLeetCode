#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rows =  len(grid)
        cols = len(grid[0])
        for i in range(rows) :
            for j in range(cols):
                if grid[i][j] == 1:
                    for v,h in directions:
                       if i +v < 0 or i + v >=rows or j + h < 0 or j + h >= cols:
                           perimeter+=1
                       elif grid[i+v][j + h] == 0:
                            perimeter+=1

        return perimeter   
s = Solution()
s.islandPerimeter([[1,1]])            
# @lc code=end

