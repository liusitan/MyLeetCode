#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
from typing import List
from unicodedata import decimal


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            n = i
            success = True
            while n != 0 : 
                if n%10 == 0 or  not i%(n % 10)==0:
                    success  = False 
                    break
                n//=10
            if success:
                res.append(i)
        return res
s = Solution()
print(s.selfDividingNumbers(1,22))
# @lc code=end

