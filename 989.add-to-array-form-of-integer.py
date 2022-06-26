#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
from typing import Deque, List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for i in  num:
            n = n*10 + i
        kl = Deque()
        k = k + n
        while k:
            kl.appendleft(k%10)
            k//=10
            
        return kl
# @lc code=end

