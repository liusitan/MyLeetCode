#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
from typing import List

# i make sure that r is alwarys at the right + peak range
# and the l is always at the left range
# then m is at the middle of left and right. Each time, l = m +1, r = m, in this way, 
# the moment that l = r is when l is right out of  left, which is peak.
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l  = 0
        r = len(arr) - 1
        while l<r:
            m  = (l+r)//2
            if arr[m] < arr[m+1]:
                l = m + 1
            else:
                r = m 
        return l
    
s = Solution()
s.peakIndexInMountainArray([0,1,0])
# @lc code=end

