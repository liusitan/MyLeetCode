#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = 0
        for c in word:
            if c.isupper():
                n+=1
        if n== 0:
            return True
        elif n == len(word):
            return True
        elif n==1 and word[0].isupper():
            return True
        else:
            return False
# @lc code=end

