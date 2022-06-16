#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if s == []:
            return 0
        gc = g.copy()
        sc = s.copy()
        gc.sort()
        gc.reverse()
        sc.sort()
        sc.reverse()
        res= 0
        si = 0; 
        for g in gc:
            if sc[si] >= g:
                res+=1
                si+=1
                if si == len(sc):
                    break
        return res 
# @lc code=end


