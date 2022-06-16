#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
import re


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s == "":
            return True
        l = len(s)
        for i in range(1,l//2+1): 
            if(l%i==0):
                if re.fullmatch("(" + s[:i]+")+",s):
                    return True
        return False 
s = Solution()
print(s.repeatedSubstringPattern("ababba")   )           
# @lc code=end

