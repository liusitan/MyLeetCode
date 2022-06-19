#
# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#

# @lc code=start
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        freq = {}
        for i in licensePlate:
            if i.isalpha():
                freq[i.lower()      ] = freq.get(i.lower(), 0)  +1
        words = sorted(words,key=lambda x: len(x))
        for word in words:
            f_c = freq.copy()
            for c in word: 
                if c in f_c and f_c[c] > 0:
                    f_c[c] -=1
                    
            if sum(f_c.values()) == 0:
                return word
s = Solution()
s.shortestCompletingWord("1s3 PSt",["step","steps","stripe","stepple"])
                
# @lc code=end

