#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root.left and not root.right:
                return root,root
            elif not root.left and root.right:
                l,h = helper(root.right)
                root.right = l
                return root, h
            elif not root.right and root.left:
                l,h = helper(root.left)
                root.left = None

                h.right = root
                return l, root
            else:
                ll,lh = helper(root.left)
                root.left = None
                rl,rh = helper(root.right)
                lh.right = root
                root.right = rl
            return ll,rh
        ll,_ = helper(root)
        return ll
s = Solution()

# @lc code=end

