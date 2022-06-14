#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root:
            ld = self.minDepth(root.left)
            rd = self.minDepth(root.right)
            if ld == 0 and rd == 0:
                return 1
            elif ld != 0 and rd == 0:
                return ld+1
            elif ld == 0 and rd!= 0:
                return rd+1
            else:
                return min(ld,rd) + 1
        else:
            return 0
# @lc code=end

