#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        if (not root.left) and (not root.right):
            return [str(root.val)]
        def helper(root,s):
            if not root:
                return
            if (not root.left) and (not root.right):
                self.res.append(s + "->" + str(root.val))
                return
            else:
                helper(root.left,s + "->" + str(root.val))
                helper(root.right,s + "->" + str(root.val))
        helper(root.left, str(root.val))
        helper(root.right,str(root.val))
        return self.res
            
# @lc code=end

