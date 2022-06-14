#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if( len(s) != len(t)):
            return False
        else: 
            maps = {}
            mapt = {}
            for (sc,tc) in zip(s,t):
                if (sc in maps.keys()) and maps[sc]!=tc:
                    return False
                if (tc in mapt.keys()) and mapt[tc]!=sc:
                    return False
                maps[sc] = tc
                mapt[tc] = sc
            return True  
# @lc code=end

