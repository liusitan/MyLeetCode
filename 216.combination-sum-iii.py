#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
import enum
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k,n,pool,res,tmp):
            if k <= 0 or n<=0:
                if k== 0 and n==0:
                    res.append(tmp.copy())
                else:
                    return
            for i, v in enumerate(pool):
                if n - v >= 0:
                    tmp.append(v)
                    helper(k-1,n-v,pool[i+1:],res,tmp)
                    tmp.pop()
        res = []
        helper(k,n,list(range(9,0,-1)),res,[])
        return res
                
s = Solution()
print(s.combinationSum3(3,7)       ) 
# @lc code=end

