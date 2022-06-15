#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root:Optional[TreeNode],left:bool):
            if(root== None):
                return 0
            if(root.left == None and root.right == None):
                if left:
                    return root.val
            return helper(root.left,True) + helper(root.right,False)
        return helper(root.left,True) + helper(root.right,False)

# @lc code=end

