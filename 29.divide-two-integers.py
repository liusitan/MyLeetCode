#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1): return 2147483647
        dd,dv,res = abs(dividend),abs(divisor),0
        for i in range(32)[::-1]:
            if(dd >= (dv << i)):
                res += 1 << i
                dd -= dv<<i
        return res if(dividend>0)==(divisor>0) else -res
s = Solution()
s.divide(3,1)
# @lc code=end

