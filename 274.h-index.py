#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations,reverse=True)
        h_index = 0
        for i,v in enumerate(citations):
            cur  = min(i+1,v)
            h_index = max(h_index,cur)
        return h_index
            
# @lc code=end

