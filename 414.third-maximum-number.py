#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start


from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = float('-inf')
        m2 = float('-inf')
        m3 = float('-inf')
        for i in nums:
            if i > m1:
                m3 = m2
                m2 = m1
                m1 = i
            elif i!=m1 and  i > m2:
                m3 = m2
                m2 = i
            elif i!= m2 and i!=m1 and i > m3:
                m3 = i
        return m3 if m3 !=float('-inf') else m1
s  = Solution()
s.thirdMax([1,2])
# @lc code=end

