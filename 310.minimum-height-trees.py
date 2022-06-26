#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
# from this import d
from typing import List

# from this import d

class Solution:
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.d1 = [0] * n 
        self.d2 = [0] * n 
        self.up = [0] * n
        self.d1c = [0] * n
        self.m = {i:[] for i in range(n)}
        for edge in edges:
            self.m[edge[0]].append(edge[1])
            self.m[edge[1]].append(edge[0])
        
        def dfsdown(cur,parent):
            children = self.m[cur]
            
            for child in children:
                if child!=parent:
                    dfsdown(child,cur)
                    d = self.d1[child] +1
                    if d > self.d1[cur]:
                        self.d2[cur] = self.d1[cur]
                        self.d1[cur] = d
                        self.d1c[cur] = child
                    elif d > self.d2[cur]:
                        self.d2[cur] = d
        
        def dfsup(cur,parent):
            children = self.m[cur]
            for i in children:
                if i != parent:
                    if i == self.d1c[cur]:
                        self.up[i] = max(self.up[cur],self.d2[cur])+1
                    else:
                        self.up[i] = max(self.up[cur],self.d1[cur]) + 1
                    dfsup(i,cur)

                
        
        dfsdown(0,-1)
        dfsup(0,-1)
        res = []
        mind = n+1
        for i, j in zip(self.up,self.d1):
            mind = min(max(i,j),mind)
        for i in range(n):
            if mind == max(self.up[i],self.d1[i]):
                res.append(i)
        return res
s = Solution()
print(s.findMinHeightTrees(4,[[1,0],[1,2],[1,3]]))
# @lc code=end

