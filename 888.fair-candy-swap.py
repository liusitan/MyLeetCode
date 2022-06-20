#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

# @lc code=start
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_aliceSizes = sum(aliceSizes)
        sum_bobSizes = sum(bobSizes)
        if sum_aliceSizes > sum_bobSizes:
            diff = sum_aliceSizes - sum_bobSizes
            diff //=2
            s = set([i - diff for i in aliceSizes])
            for i in bobSizes:
                if i in s:
                    return [i+diff,i]
        else:
            diff =  sum_bobSizes - sum_aliceSizes
            diff //=2

            s = set([i - diff for i in bobSizes])
            for i in aliceSizes:
                if i in s:
                    return [i,i+diff]
# @lc code=end

