#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
import collections
from typing import Deque


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = {}
        visited ={}
        for c in s:
            freq[c] = freq.get(c,0) + 1
            visited[c] = False
        stack = Deque()
        for c in s:
            freq[c] -= 1
            if visited[c]:
                continue
            while stack and stack[-1] >= c and freq[stack[-1]] >=1:
                visited[stack.pop()] = False
            stack.append(c)
            visited[c] = True
        return ''.join(stack)
                
s = Solution()
print(s.removeDuplicateLetters("bcabc"))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

