#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.depth(root)
        return self.res
    res = True;
    def depth(self, root:Optional[TreeNode]) -> int :
        if(root == None):
            return 0
        if(self.res):
            dl = self.depth(root.left)
            dr = self.depth(root.right)
            if abs(dl - dr) > 1:
                self.res = False        
            return max(dl,dr) + 1
        else:
            return 0
             
# @lc code=end

