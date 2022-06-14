#
# @lc app=leetcode id=803 lang=python3
#
# [803] Bricks Falling When Hit
#

# @lc code=start
from typing import List
from xmlrpc.client import boolean

class DisJointSet: 
    set_size: List[int]
    roots:List[int] 
    def __init__(self,size:int):
        self.roots = list(range(size))
        self.set_size = [1] * size
    def find(self,x:int) -> int: 
        while self.roots[x] != x:
            x = self.roots[x] 
        return x
    def union(self,x:int,y:int) ->int: 
        rx = self.find(x)
        ry  = self.find(y)
        
        if(rx < ry):
            self.roots[ry] = rx
            self.set_size[rx] = self.set_size[ry] + self.set_size[rx]
        elif(rx>ry):
            self.roots[rx] = ry
            self.set_size[ry] = self.set_size[ry] + self.set_size[rx]

            
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:

        
        m = len(grid)
        n = len(grid[0])
        ds = DisJointSet(m*n + 1)
        for hit in hits: 
            if(grid[hit[0]][hit[1]] != 0):
                grid[hit[0]][hit[1]] = -1
        res =[]
        def toIx(i,j):
            return i * n + j + 1       
        def unionAround(i : int, j:int):
            if(grid[i][j] == 1):
                if(i == 0):
                    ds.union(0,toIx(i,j))

                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for direction in directions:
                    ni = i + direction[0]
                    nj = j+ direction[1]
                    if(ni < m and ni >= 0 and nj <n and nj >= 0 and grid[ni][nj] == 1):
                        ds.union(toIx(i,j),toIx(ni,nj))
        hits.reverse()
        # //init the disjoint set_size
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    unionAround(i,j)
        lastIterNum = ds.set_size[0]
        for i,j in hits:
            if(grid[i][j] == -1):
                grid[i][j] = 1
                unionAround(i,j)
                curIterNum = ds.set_size[0]
                res.append(max(curIterNum - lastIterNum-1,0) )
                lastIterNum = curIterNum
            else:
                res.append(0)
        res.reverse()
        return res
                



s = Solution()
grid = [[1,0,0,0],[1,1,1,0]]


hit = [[1,0]]


res = s.hitBricks(grid,hit)
print(res)
# @lc code=end

