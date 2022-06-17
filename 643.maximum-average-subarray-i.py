#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k-1
        s = sum(nums[l:r+1])
        maxs = s
        nl = len(nums)-1
        while r < nl:
            cachenumsl = nums[l]
            l+=1
            r+=1
            s= s - cachenumsl + nums[r]
            maxs = max(maxs,s)
        return maxs/k
            
# @lc code=end

