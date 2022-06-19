#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from typing import Deque, List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, t_color: int) -> List[List[int]]:
        image = [i.copy() for i in image]
        color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        s = set()
        q = Deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        q.append((sr,sc))
        while q:
            r,c = q.popleft()
            image[r][c] = t_color
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]#TODO please use c!!!!
                if nr >= 0 and nr < rows and nc >=0 and nc < cols and image[nr][nc] == color and (nr,nc) not in s:
                    q.append((nr,nc))
                    s.add((nr,nc))
        return image
s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
# @lc code=end

