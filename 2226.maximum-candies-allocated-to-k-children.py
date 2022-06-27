#
# @lc app=leetcode id=2226 lang=python3
#
# [2226] Maximum Candies Allocated to K Children
#

# @lc code=start
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
       
        def satisfy(candies, c, k):
            return sum([candy//c for candy in candies]) >=k
        total = sum(candies)
        l = 1
        r = total//k +1
        while l< r: 
            m = ((l + r) //2) + 1
            if (satisfy(candies,m,k)) : l = m
            else: r = m- 1
        if sum(candies) < k:
            return 0
        return l
s = Solution()
print(s.maximumCandies([5,8,6],3))
# @lc code=end

