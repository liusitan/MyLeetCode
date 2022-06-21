#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # odds = [n for n in nums if n % 2 ==1]
        # evens = [n for n in nums  if n %2 == 0]
        # res = [odds.pop() if i%2 == 1 else evens.pop() for i in range(len(nums))]
        # return res
        o = 1
        e = 0 
        len_num = len(nums)
        while o < len_num and e < len_num:
            while(o < len_num and nums[o]%2 == 1):
                o = o+2
            while(e < len_num and nums[e]%2 == 0):
                e = e+2
            if o < len_num and e < len_num:
                nums[o],nums[e]  = nums[e],nums[o]
        return nums
            
# @lc code=end

