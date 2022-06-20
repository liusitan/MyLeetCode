#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums)<=2:
            return list(set(nums))
        count1, count2, candidate1,candidate2 = 0,0,1,1
        for n in nums:
            if n == candidate1:
                count1+=1
            elif n== candidate2:
                count2+=1
            elif count1 == 0:
                count1,candidate1 = 1,n
            elif count2==0:
                count2,candidate2 = 1,n
            else:
                count1,count2 = count1- 1, count2-1
        return [n for n in (candidate1,candidate2) if nums.count(n) > (len(nums)//3)]
# @lc code=end

