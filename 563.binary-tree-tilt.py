#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, Union


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def helper(root:Optional[TreeNode]) ->Union[int,int]:
            if root:
                tilt = 0
                sum = 0
                (lsum, ltilt) = helper(root.left)
                (rsum,rtilt) = helper(root.right)
                return (lsum+rsum+root.val,ltilt + rtilt + abs(lsum - rsum))
            else: 
                return (0,0)
        _,tilt = helper(root)
        return tilt
s = Solution()
root = TreeNode(1, TreeNode(2),TreeNode(3))
print(s.findTilt(root))
# @lc code=end

