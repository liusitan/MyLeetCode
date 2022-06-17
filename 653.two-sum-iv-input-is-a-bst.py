#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Deque, Dict, Optional, Set


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = Deque()
        res = set()
        s.append(root)
        while s:
            e = s.pop()
            if e.left:
                s.append(e.left)
            if e.right:
                s.append(e.right)
            if e.val in res:
                return True
            res.add(k-e.val)        
        return False
            
# @lc code=end

