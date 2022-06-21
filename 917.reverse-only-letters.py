#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        char_list = list(s)
        while l < r:
            while l < r and not char_list[l].isalpha():
                l+=1
            while l< r and  not char_list[r].isalpha():
                r-=1
            char_list[l],char_list[r] = char_list[r],char_list[l]
            
            l+=1
            r -=1
        return ''.join(char_list)
# @lc code=end

