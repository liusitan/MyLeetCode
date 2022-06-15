#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(" ")
        m1 = {}
        m2 = {}
        if(len(ss)!=len(pattern)):
            return False
        for (p,s) in zip(pattern, ss):
            if p in m1.keys():
                if m1[p] != s:
                    return False
            if s in m2.keys():
                if m2[s] != p:
                    return False
            m1[p] = s
            m2[s] = p
        return True
# @lc code=end

