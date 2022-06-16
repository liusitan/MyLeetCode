#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:#TODO:special case 0 in convert to base
            return '0'
        negative= num <0
        res = ''
        num = abs(num)
        while num > 0:
            res+= str(num%7)
            num//=7
        res= res[::-1]
        return res if not negative else ('-'+(res))
s = Solution()
print(s.convertToBase7(100))
# @lc code=end

