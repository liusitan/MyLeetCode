#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = set()
        for c in candyType:
            s.add(c)
        return min(len(candyType)//2, len(s))
# @lc code=end

