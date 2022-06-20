#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len (image)
        for i in range(rows):
            image[i] =[0 if i==1 else 1 for i in image[i][::-1] ]
        return image
            
# @lc code=end

