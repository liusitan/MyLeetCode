#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        s = [root]
        
        while s:
            cur = s.pop()
            if cur:
                res.append(cur.val)
                s.append(cur.right)
                s.append(cur.left)
        return res
            
# @lc code=end

