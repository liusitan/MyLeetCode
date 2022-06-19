#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        l = 0
        r = 31
        b = 0
        while(l<=r):
            m = (l+r)//2
            sn = n>>m
            if sn ==1:
                b = m
                break
            elif sn > 1:
                l = m + 1
            elif sn < 1:
                r  = m -1
        if b %2 == 1:
            return n == (((1<<(b+1))-1) & 0xAAAAAAAA)
        else:
            return n==(((1<<(b+1))-1) & 0x55555555)                      
s = Solution()
s.hasAlternatingBits(5)
# @lc code=end

