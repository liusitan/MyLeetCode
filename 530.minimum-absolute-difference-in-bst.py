#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mindiff = float('inf')
        def helper(root:Optional[TreeNode]):
            if root:
                lmax,lmin= helper(root.left)
                rmax,rmin = helper(root.right)
                self.mindiff = min(self.mindiff,abs(root.val-lmax),abs(root.val - rmin) )
                return max(root.val,rmax),min(root.val,lmin)
            else:
                return float('-inf'),float('inf')
        helper(root)
        return self.mindiff
s = Solution()
r = TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(6))
print(s.getMinimumDifference(r))
                
# @lc code=end

