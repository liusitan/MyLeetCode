#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1 = {}
        m2 = {}
        def frequency(nums1, m1):
            for i in nums1:
                if i in m1.keys():
                    m1[i] +=1
                    continue
                m1[i] = 1
        frequency(nums1,m1)
        frequency(nums2,m2)
        res  = []
        for key in m1.keys():
            if key in m2.keys():
                 res += [key]* min(m1[key], m2[key])
        return res
# @lc code=end

