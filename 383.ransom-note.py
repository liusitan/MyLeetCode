#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f1 = [0] * 256
        f2 = [0] * 256
        for c in ransomNote:
            f1[ord(c) ] +=1
        for c in magazine:
            f2[ord(c)] +=1
        for i in range(256):
            if f1[i] > f2[i]:
                return False
        return True
        # @lc code=end

