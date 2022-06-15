#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r = 0, len(s)-1
        ls = [c for c in s]
        def isVowel(c):
            if c in ['a','e','i','o','u','A','E','I','O','U']:
                return True
            return False
        while l< r:
            while not isVowel(ls[l]) and  l< r :
                l +=1
            while not isVowel(ls[r]) and l<r:
                r-=1
            if l<r:
                tmp = ls[l]
                ls[l] = ls[r]
                ls[r] = tmp
            l +=1
            r -= 1
        return ''.join(ls)
s= Solution()
s.reverseVowels(" ")
# @lc code=end

