#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cs = {}
        for i in words[0]:
            cs[i] = cs.get(i,0) + 1
        for word in words[1:]:
            tmp = {}
            for i in  word:
                tmp[i] = tmp.get(i,0) + 1
            for i in cs:
                if i in tmp:
                    cs[i] = min(tmp[i],cs[i])
                else:
                    cs[i] = 0
        res = []
        for k,v in cs.items():
            res += [k] * v
        return res
            
# @lc code=end

