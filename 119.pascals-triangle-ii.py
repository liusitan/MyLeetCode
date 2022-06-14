#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        i = 2
        res = []
        cur = [0,1,1,0]
        while i <= rowIndex:
            for i in range(1,len(cur)):
                res.append(cur[i-1]+cur[i])
            cur = [0] + res + [0]
            res = []
                
                
        return cur[1:-1]                    
                    
# @lc code=end

