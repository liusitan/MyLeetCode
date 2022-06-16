#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = {n:i for i, n in enumerate( sorted(score,reverse=True))}
        medals = ["Gold Medal","Silver Medal","Bronze Medal"]
        return [str(s[i]+1 ) if s[i] >= len(medals) else medals[s[i]] for i in score]
# @lc code=end

