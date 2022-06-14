#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
from string import ascii_uppercase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            i = columnNumber % 26
            res = chr(ord('A') + ((i-1)%26) ) + res
            columnNumber =(columnNumber - 1)//26
        return res 
# @lc code=end

