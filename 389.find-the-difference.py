#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l1 = [0] * 26
        l2 = [0] * 26
        for c in s:
            l1[ord(c)- ord('a')]+=1        
        for c in t:
            l2[ord(c)- ord('a')]+=1
        for i in range(26):
            if l1[i] != l2[i]:
                return chr(i+ord('a'))
        # return t[-1]
# @lc code=end

