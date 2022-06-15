#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
        middle = 0; 
        res = 0
        for v in freq.values():
            if(v%2 == 0):
               res  += v 
            else:
                res += v-1
                middle = 1
        return res + middle
# @lc code=end

