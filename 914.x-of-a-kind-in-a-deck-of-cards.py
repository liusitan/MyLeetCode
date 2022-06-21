#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

# @lc code=start
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        m  = {}
        for i in deck:
            m[i] = m.get(i,0) + 1
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        
        m.values()
        return reduce(gcd, m.values())>1
# @lc code=end

