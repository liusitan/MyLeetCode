#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
from math import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if (num == 1):#TODO special case for perfect number 1
            return False
        sum = 0 
        for i in range(2,int(sqrt(num))+1):
            if num%i == 0:
                sum += i + num//i #TODO optimization
        sum +=1
                
                
        return sum == num
s = Solution()
s.checkPerfectNumber(6)
# @lc code=end

