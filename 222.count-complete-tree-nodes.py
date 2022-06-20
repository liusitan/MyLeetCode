#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        height = 0
        cur = root
        while cur.left:
            height+=1
            cur = cur.left
        l = 0
        r = pow(2,height) - 1
        while l<r:
            m = (l+r)//2+1
            route = bin(m)[2:].zfill(height)
            cur = root
            for i in route:
                if i == '1':
                    cur = cur.right
                else:
                    cur = cur.left
            if cur:
                l = m
            else:
                r = m-1
        return l + pow(2,height)
                
                
                
s = Solution()
print(s.countNodes(TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3))))

# @lc code=end

