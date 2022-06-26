#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Deque, Optional


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = Deque()
        nextq =Deque()
        count = 2
        q.append(root)
        while q:
            
            e = q.pop()
            if e.left and e.right:
                if (e.left.val == x and e.right.val == y) or (e.left.val == y and e.right.val == x):
                    return False
            if e.left:
                if e.left.val == x or e.left.val == y:
                    count-=1
                nextq.append(e.left)
            if e.right:
                if e.right.val== y or e.right.val ==x:
                    count -=1
                nextq.append(e.right)
            if count == 0:
                return True
            if not q:
                q = nextq
                nextq = Deque()
                count = 2
        return count == 0   
s = Solution()
s.isCousins(TreeNode(1,TreeNode(2,None,TreeNode(4)),TreeNode(3,None,TreeNode(5))),5,4)         
# @lc code=end

