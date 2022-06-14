#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = set()
        row_size = len(grid)
        col_size = len(grid[0])
        if row_size == 1 and col_size ==1:
            return 0
        steps = 0
        q = deque([(0,0,k)])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        level_size = 1 
        next_level_size = 0
        while q:
            (r,c,rk) = q.popleft()
            level_size -=1
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                if nr < 0 or nr >= row_size or nc < 0 or nc >= col_size:
                    continue
                nrk = rk - grid[nr][nc]
                if  (nr,nc,nrk) in visited or nrk < 0:
                    continue
                if nr == row_size - 1 and nc == col_size - 1 and nrk >= 0:
                    return steps +1 
                else: 
                    next_level_size+=1
                    visited.add((nr,nc,nrk))
                    q.append((nr,nc,nrk))
            if(level_size == 0):
                steps += 1
                level_size =next_level_size
                next_level_size = 0
            
        return -1
s = Solution()
grid = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]
k = 1
s.shortestPath(grid,k)
# @lc code=end
