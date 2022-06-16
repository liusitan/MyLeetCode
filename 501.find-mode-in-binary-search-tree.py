#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversed = []
        def inOrder(root:Optional[TreeNode]):
            if root:
                inOrder(root.left)
                self.traversed += [root.val]
                inOrder(root.right)
        inOrder(root)
        cur = self.traversed[0]
        count = 0
        maxCount = 0
        mode = self.traversed[0]
        m = {}
        res = []
        for n in self.traversed:
            if cur == n:
                count += 1
            else:
                m[cur] = count
                count = 1
                cur = n
        m[cur] = count

        modefreq = max(m.values())
        for k,v in m.items():
            if v == modefreq:
                res.append(k)
        return res
s = Solution()
r = TreeNode()
r.val = 1
r.right = TreeNode(2)
r.right.left = TreeNode(2)
print(s.findMode(r))
# @lc code=end

