#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        def helper(root, p, q)->bool:
            if root == None:
                return False
            if root.val == p.val or root.val == q.val:
                if helper(root.left, p, q) or helper(root.right, p, q):
                    self.lca = root
                return True
            else:
                h1 = helper(root.left, p, q);
                h2 = helper(root.right, p, q)
                if h1 and h2 :
                    self.lca = root
                if h1 or h2:
                    return True
                return False
        helper(root,p,q)
        return self.lca
# @lc code=end

