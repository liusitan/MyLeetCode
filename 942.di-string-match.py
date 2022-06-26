#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#

# @lc code=start
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        D = len(s)
        I = 0
        res = []
        for i in s:
            if i == "I":
                res.append(I)
                I = I + 1
            else:
                res.append(D)
                D = D-1
        res.append(D)
        return res
# @lc code=end

