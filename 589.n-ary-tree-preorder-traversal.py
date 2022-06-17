#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
from typing import Deque


class Solution:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return [] # TODO: root = None
        res = []
        s = Deque()
        s.append(root)
        while s:
            t = s.pop()
            res.append(t.val)
            if t.children:
                tc = t.children.copy()
                tc.reverse()
                for c in tc:
                    s.append(c)
        return res
            
# @lc code=end

