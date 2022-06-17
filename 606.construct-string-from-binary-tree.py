#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from xmlrpc.client import FastUnmarshaller


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        left = '({})'.format(self.tree2str(root.left)) if root.right or root.left else ''
        right = '({})'.format(self.tree2str(root.right)) if root.right else ''
        return '{}{}{}'.format(str(root.val),left,right) 
        # return str(root.val) + helper(root.left,True) + helper(root.right,False)
# @lc code=end

