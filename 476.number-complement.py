#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        tmp = num
        count = 0
        while tmp > 0:
            tmp >>=1
            count+=1
        
        return ~num & ((1<<count) - 1)
s = Solution()
print(s.findComplement(5))
# @lc code=end

