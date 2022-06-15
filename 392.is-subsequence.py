#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0 
        ti = 0
        if s == "":
            return True
        for ti in range(len(t)):
            if(t[ti]==s[si]):
                si+=1
                if(si==len(s)):
                    return True
        return False
# @lc code=end

