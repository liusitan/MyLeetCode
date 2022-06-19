#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        m = {}
        for i in range(len(s)-10+1):
            m[s[i:i+10]] =m.get(s[i:i+10],0) + 1
        return [k for k,v in m.items() if v > 1]
s = Solution()
s.findRepeatedDnaSequences("AAAAAAAAAAA")
# @lc code=end

