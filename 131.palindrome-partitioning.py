#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from re import S
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        str_len = len(s)
        cache = [[True] *str_len for i in range(str_len)]
        for l in range(2,str_len+1):
                for i in range(str_len - l+1):
                    cache[i][i+l-1] = cache[i+1][i+l-2] and s[i] == s[i+l-1]
        def generate_res(s:str,cache,start,res,track):
            if start == len(s):
                res.append(track.copy())
            for i in range(start,len(s)):
                if cache[start][i]:
                    track.append(s[start:i+1])
                    generate_res(s,cache,i+1,res,track)
                    track.pop()
            return res
        return generate_res(s,cache,0,[],[])
                
s = Solution()
print(s.partition("aab"))                  
                    
# @lc code=end

