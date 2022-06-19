#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        p = bits.pop() 
        if p != 0:
            return False
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                i+=1
            else:
                i+=2
        return i == len(bits)
s = Solution()
print(s.isOneBitCharacter([1,0,0]))
# @lc code=end

