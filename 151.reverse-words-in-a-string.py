#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
import re


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ss = re.split("[\s]+",s)
        ss.reverse()
        return ' '.join(ss)
# @lc code=end

