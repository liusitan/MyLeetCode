#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pool  = {}
        for i,v in enumerate(nums): 
            if v in pool.keys():
                if(k >= (i - pool[v])):
                    return True
            pool[v] = i
        return False
# @lc code=end

