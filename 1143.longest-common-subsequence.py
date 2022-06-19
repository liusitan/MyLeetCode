#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
import functools


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def method2( text1: str, text2: str) -> int:
            dp = [[0]*(len(text2)+1) for j in range(len(text1)+1)]
            for i in range(1,len(text1)+1):
                for j in range(1,len(text2)+1):
                    if text1[i-1]==text2[j-1]:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j]= max(dp[i-1][j],dp[i][j-1])
            return dp[len(text1)][len(text2)]
        def method1( text1: str, text2: str) -> int:
            if text1=="" or text2 =="":
                return 0
            self.memory = [[-1]*len(text2) for j in range(len(text1))]
            def helper(text1:str, p1:int, text2:str, p2:int) ->int:
                if p1< 0 or p2 < 0:
                    return 0
                if self.memory[p1][p2] >=0:
                    return self.memory[p1][p2]
                if text1[p1] == text2[p2]:
                    res =  1 + helper(text1,p1-1,text2,p2-1)
                    self.memory[p1][p2] = res
                else:
                    res = max(helper(text1,p1,text2,p2-1),helper(text1,p1-1,text2,p2))
                    self.memory[p1][p2] = res
                return res
            helper(text1,len(text1)-1,text2,len(text2)-1)
            # print(self.memory)

            return self.memory[len(text1)-1][len(text2)-1]
        return method2(text1,text2)

s= Solution()
print(s.longestCommonSubsequence("ezupkr","ubmrapg"))
# @lc code=end

