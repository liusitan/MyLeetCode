#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def encode(word:str):
            res = 0
            for i in set(word):
                res |=  (1<<(ord(i) - ord('a') + 1))
            return res
        encoded = [encode(w) for w in words]
        res = 0
        words_len = len(words)
        for i in range(words_len):
            for j in range(i,words_len):
                if encoded[i] & encoded[j] == 0:
                    res = max(res,len(words[i])* len(words[j]) )
        return res
s= Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
# @lc code=end

