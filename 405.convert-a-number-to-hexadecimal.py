#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        bin = []
        for i in range(32):
            bin.append(num&1)
            num >>= 1
        res = []
        for i in range(8):
            sub = bin[i*4: i*4 + 4]
            val = 0
            for i,b in enumerate(sub):
                val = val + (b <<i) 
            if val < 10: 
                res.append(str(val))
            else:
                res.append(chr(ord('a') + val - 10))
        res.reverse()
        while res[0] == '0' and len(res)>1:
            res.remove('0')
        return ''.join(res)
s = Solution()
s.toHex(26)
# @lc code=end

