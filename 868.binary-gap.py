#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        bs = bin(n)[2:]
        i = 0
        j = 0
        distance = 0
        while j < len(bs):
            if bs[j] == '1':
                j+=1
                while j < len(bs) and bs[j] == '0':
                    j+=1
                if j <len(bs):
                    distance = max(distance, j - i)
                    
            else:
                j+=1
            i = j
        return distance
# @lc code=end

