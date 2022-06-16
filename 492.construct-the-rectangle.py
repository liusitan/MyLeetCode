#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sq = sqrt(area)
        sq = int(sq)
        for i in range( sq, 0, -1):
            if(area%i ==0):
                return [area//i,i]
            
# @lc code=end

