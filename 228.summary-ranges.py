#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        l = nums[0]
        r = nums[0]
        res = []
        def toStr(l,r):
            if (l==r):
                return str(l)
            else:
                return str(l) + "->" + str(r)
        
        for i in nums:
            if i - r > 1:
                res.append(toStr(l,r))
                l = i
            r = i
        res.append(toStr(l,r))
        return res    
                
                
# @lc code=end

