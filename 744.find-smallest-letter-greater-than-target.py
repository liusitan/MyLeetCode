#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i) > ord(target):
                return i
        return letters[0]
# @lc code=end

