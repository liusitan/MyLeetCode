#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        str_len = len(strs[0])

        sorted = [True]*str_len
        prev = strs[0]
        for sstr in strs[1:]:
            for i in range(str_len):
                if sorted[i] and sstr[i] < prev[i]:
                    sorted[i] = False
            prev = sstr
        return sorted.count(False)
# @lc code=end

