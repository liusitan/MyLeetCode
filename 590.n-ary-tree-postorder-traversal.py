#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import Deque


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        d = Deque()
        d.append(root)
        res = Deque()
        while d:
            n = d.pop()
            res.appendleft(n.val)
            if n.children:
                for c in n.children:
                    d.append(c)
        return res
# @lc code=end

