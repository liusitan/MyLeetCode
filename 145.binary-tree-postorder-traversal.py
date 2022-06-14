#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = [root] 
        res  = []
        while s: 
            cur = s.pop()
            if cur: 
                res.append(cur.val)
                s.append(cur.left)
                s.append(cur.right)
        res.reverse()
        return res
# @lc code=end

