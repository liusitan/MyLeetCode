#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        diff = t + 1
        buckets = {}
        def computebucketsindex(id,diff=diff,m=min(nums)):
            return (id-m)//diff
        for i,v in enumerate(nums):
            bid = computebucketsindex(v)
            if (bid-1) in buckets:
                if abs(buckets[bid-1] - v) <= t:
                    return True
            if (bid+1) in buckets:
                if abs(buckets[bid+1]-v) <=t:
                    return True
            if bid in buckets:
                return True
            buckets[bid] = v
            if i >=k:
                buckets.pop(computebucketsindex(nums[i-k]))
        return False
s = Solution()
print(s.containsNearbyAlmostDuplicate([1,2,3,1],3,0))
# @lc code=end

