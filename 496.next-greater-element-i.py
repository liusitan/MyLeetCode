#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from typing import Deque


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = Deque()
        m = {}
        res =[]
        for num in nums2:
            while st and num > st[-1] :
                m[st.pop()] = num
            st.append(num)
        for num in nums1:
            res.append(m.get(num,-1))
        return res
# @lc code=end

