#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        s = Deque()
        v = root.val
        s.append(root)
        while s:
            n = s.pop()
            if n.val != v:
                return False
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
        return True
# @lc code=end

