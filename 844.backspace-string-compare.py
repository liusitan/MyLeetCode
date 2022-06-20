#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
from typing import Deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sid = len(s)-1
        tid = len(t) - 1
        while True:
            backs = 0
            while sid >=0 and (s[sid] == '#' or backs> 0): 
                backs += 1 if s[sid]=='#'  else -1
                sid -=1
            backs = 0
            while  tid >=0 and (t[tid] == '#' or backs> 0):
                backs += 1 if t[tid]=='#'  else -1
                tid -=1
            if sid >= 0 and tid >=0 and s[sid]==t[tid]:
                sid -= 1
                tid -= 1           
            else:
                break
               
        return sid == -1 and tid == -1
# @lc code=end

