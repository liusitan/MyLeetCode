#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        columnTitleR = columnTitle[::-1]
        
        for c in columnTitle:
            res *= 26
            res += ord(c) - ord('A') + 1
        return res
        
# @lc code=end

