#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        stat = {}
        for i in moves:
            stat[i] = stat.get(i,0) +1
        return stat.get("R",0) == stat.get("L",0) and stat.get("D",0)== stat.get("U",0)
# @lc code=end

