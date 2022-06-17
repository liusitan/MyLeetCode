#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]
        next = 0
        cur = 1
        remaining = 1
        sum = 0
        res = []
        q = Deque()
        q.append(root)
        while q:
            e = q.popleft()
            sum += e.val
            if e.left:
                q.append(e.left)
                next+=1
            if e.right:
                q.append(e.right)
                next+=1
            
            remaining-=1
            if remaining == 0:
                res.append(sum/cur)
                cur = next
                remaining = next
                sum = 0
                next = 0
        return res
        
# @lc code=end

