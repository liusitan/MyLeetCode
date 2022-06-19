#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i,j,N = 0,0,len(s)
        res = []
        while j < N:
            while j<N and s[i] == s[j]: 
                j+=1
            if j -i >= 3:
                 res.append([i,j-1])
            i = j
        return res
# @lc code=end

