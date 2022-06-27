#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq


class Solution:
    def kSmallestPairs(self, A: List[int], B: List[int], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        for i,a in enumerate(A):
            heapq.heappush(h,(a+B[0],i,0))
        res = []
        while k > 0 and h: 
            e = heapq.heappop(h)
            res.append([A[e[1]],B[e[2]]])
            if e[2] + 1 < len(B):
                heapq.heappush(h,(A[e[1]]+B[e[2]+1],e[1],e[2]+1))
            k-= 1
        return res
# @lc code=end

 