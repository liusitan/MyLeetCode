#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
from audioop import reverse


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        h = x ^y
        br = bin(h)[2:]
        br = br[::-1]
        f = 0
        for i,n in enumerate(br):
            if n == '1':
                f+=1
        return f
s = Solution()
s.hammingDistance(3,1)      
# @lc code=end

