#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pool = set()
        for i in nums:
            if i in pool:
                return True
            pool.add(i)
        return False
# @lc code=end

