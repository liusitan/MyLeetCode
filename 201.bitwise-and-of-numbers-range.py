#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0:
            return 0 
        bl = bin(left)
        br = bin(right)
        bl = '0' *  (32 - (len(bl)-2))+ bl[2:]
        br = '0' * (32 - (len(br)-2)) + br[2:]
        f1l = bl.index('1')
        f1r = br.index('1')
        if f1l !=f1r:
            return 0
        end = f1l
        for i,j in zip(bl[f1l+1:],br[f1r+1:]):
            if i == j :
                f1l+=1
            else:
                break
        sum = 0
        for i in range(f1r,f1l+1):
            sum += int(bl[i]) <<(31-i)
        return sum
s = Solution()
print(s.rangeBitwiseAnd(5,7))
# @lc code=end

