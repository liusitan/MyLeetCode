#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from collections import deque
from typing import Deque, List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        mynums = nums.copy()
        mynums.sort()
        res = []
        tmp = Deque()
        def permuteHelper(nums: List[int]) ->None:
            traversed = set()
            if not nums:
                res.append(list(tmp))
                return
            for i in nums:
                if( i in traversed):
                    continue
                else:
                    traversed.add(i)
                    tmp.append(i)
                    mynums = nums.copy()
                    mynums.remove(i)
                    permuteHelper(mynums) 
                    tmp.pop()
        permuteHelper(mynums)
        return res
s = Solution()
t1 = [1,2,3]
t2 = [1,1,1]
t3= [1]
t4 = []
t5 = [2,2,1,1]

print(s.permuteUnique(t5))
# @lc code=end

# [[2,2,1,1],[2,1,2,1],[2,1,1,2],[1,2,2,1],[2,1,1,2],![1,1,2,2]]

# [![1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]