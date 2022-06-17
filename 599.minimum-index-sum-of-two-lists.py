#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m1 = {name: i for i,name in enumerate(list1)}
        m2 = {name: i for i,name in enumerate(list2)}
        intersection =[key for key in  m1.keys() if key in m2.keys()]
        m3  = {name: m1[name] + m2[name] for name in intersection}
        least_index = min(m3.values())
        res = []
        for k,v in m3.items():
            if v == least_index:
                res.append(k)
        return res       
# @lc code=end

