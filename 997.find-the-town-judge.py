#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inward = [0] *(n+1)
        outward = [0] *(n+1)
        for rel in trust:
            inward[rel[1]] +=  1
            outward[rel[0]] =  1
        possible_judge = 0
        for i in range(1,n+1):
            if outward[i] == 0:
                possible_judge = i
                break
        return possible_judge if inward[possible_judge]==n-1 else -1
# @lc code=end

