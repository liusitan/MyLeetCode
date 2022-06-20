#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, A: List[int], k: int) -> int:
                return max(0, max(A) - min(A) - 2 * k)

# @lc code=end

