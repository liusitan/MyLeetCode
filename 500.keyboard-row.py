#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
import re
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f = "[qwertyuiop]+"
        s = "[asdfghjkl]+"
        t = "[zxcvbnm]+"
        res = []
        for word_ in words:
            word = word_.lower()
            if re.fullmatch(f,word) or re.fullmatch(s,word) or re.fullmatch(t,word):
                res.append(word_)
        return res
# @lc code=end

