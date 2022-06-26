#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = []
        q = [1]
        if n == 1:
            return 1
        p2,p3,p5 = 0,0,0
        while len(q) < n:
            q.append(min(q[p2]*2,q[p3]*3,q[p5]*5))
            if q[-1] == q[p2]*2: p2+=1
            if q[-1] == q[p3]*3: p3+=1
            if q[-1] == q[p5]*5: p5+=1
        return q[-1]
s = Solution()
s.nthUglyNumber(10)    
# @lc code=end

