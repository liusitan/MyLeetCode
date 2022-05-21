#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
'''
This question is based on the adder calculator. 
The general idea is pretty simple, code need to figure how to do addition and mod in using bit ops. 
For addition the tricks is how to do carry 
let's say n bit representation, bit n is updated from 1 to 0, only when the bit n-1 to bit 1 is 1. 
That's what line 20 and 21 does.
And for mod like operation, set to k when the value is k. The mask is configure for that
bascially a compaprision between x1,x2, and the representation of k. 
'''
# @lc code=start
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1,x2,mask = 0,0,0
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x2 & x1)
            x1 &= mask
            x2 &= mask
        return x1
# @lc code=end

