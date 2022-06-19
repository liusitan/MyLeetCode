#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = [float('inf')] * len(s)
        r = [float('inf')]*len(s)
        closest = float('inf')
        for i,sc in enumerate(s):
            if sc == c:
                closest = i
            l[i] = closest
        closest = float('inf')

        for i in range(len(s)-1,-1,-1):
            if s[i] == c:
                closest = i
            r[i] =closest
        res =  [-1]*len(s)
        for i in range(len(s)):
            res[i] = min(abs(i -l[i]),abs(i-r[i]))
        return res
# @lc code=end

