#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [(i,j) for i in [0,-1,1] for j in [0,-1,1]]
        rows = len(img)
        cols = len(img[0])
        res = []
        for i in range(rows):
            col_list = []
            for j in range(cols):
                win_sum = []
                for direction in directions:
                    x = i + direction[0]
                    y = j + direction[1]
                    if x >=0  and x < rows and y >= 0 and y <cols:
                        win_sum.append(img[x][y])
                col_list.append(sum(win_sum)//len(win_sum))
            res.append(col_list)
        return res
            
# @lc code=end

