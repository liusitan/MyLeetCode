#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        cur = s_nums[0]
        range = s_nums[0] + 1
        def consecutiveN(idx,nums): 
            n = nums[idx]
            origin = idx
            while idx < len(nums) and nums[idx] == n:
                idx+=1
            return (idx - origin, n, idx)
        nid = 0
        laststat = (0,s_nums[0],0)
        thisstat = ()
        max_count = 0
        while nid < len(s_nums):
            thisstat = consecutiveN(nid,s_nums)
            nid = thisstat[2]
            if abs(laststat[1] - thisstat[1])== 1:
                max_count = max(max_count, laststat[0]+thisstat[0])
            
            laststat = thisstat
        return max_count
            
                
            
# @lc code=end

