#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
import re


class Solution:
    def countSegments(self, s: str) -> int:
        s =s.strip()
        if s == "":
            return 0
        return len(re.split('\s+',s))
s= Solution()
print(s.countSegments("   "))
# @lc code=end

