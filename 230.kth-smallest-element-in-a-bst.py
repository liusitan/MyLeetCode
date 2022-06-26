#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root:Optional[TreeNode],k:int) -> int:
            if not root:
                return 0,0
            vl,sl = helper(root.left,k)
            if sl < 0:
                return vl,sl
            elif sl == k - 1:
                return root.val,-1
            else:
                vr,sr = helper(root.right,k-sl-1 )
                if sr < 0:
                    return vr,sr
                else:
                    return vl,sl + sr + 1
        return helper(root,k)[0]
s = Solution()
print(s.kthSmallest(TreeNode(5,TreeNode(3,TreeNode(2,TreeNode(1)),TreeNode(4)),TreeNode(6)),3) )   
# @lc code=end

