#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
from typing import Deque


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = Deque()
        for op in ops:
            if op == "D":
                s.append(s[-1]*2)
            elif op == "C":
                s.pop()
            elif op == "+":
                s.append(s[-1]+s[-2])
            else:
                s.append(int(op))
        sum = 0
        while s:
            sum += s.pop()
        return sum
# @lc code=end

