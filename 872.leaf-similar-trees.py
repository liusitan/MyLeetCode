#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafnode(root,stat):
            if root:
                if not root.left and not root.right:
                    stat.append(root.val)
                else:
                    leafnode(root.left,stat)
                    leafnode(root.right,stat)
        res1 = []
        res2 = []
        leafnode(root1,res1)
        leafnode(root2,res2)
        return res1 == res2
# @lc code=end

