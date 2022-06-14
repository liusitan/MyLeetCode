#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10 :
            return num
        else:
            digits = 0
            while(num != 0):
                digits += num % 10 
                num //=10
            return self.addDigits(digits)
# @lc code=end

