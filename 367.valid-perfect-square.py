#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = 1<<31
        while(l <= r):
            m = (l+r)//2
            msq = m*m
            if( msq< num):
                l = m + 1
            elif (msq == num):
                return True
            else: 
                r = m - 1
        return False
                
# @lc code=end

