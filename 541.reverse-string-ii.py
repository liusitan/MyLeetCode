#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        remaining = len(s) %( 2* k)
        last = ''
        if remaining > k: 
            last = s[-remaining:-remaining + k][::-1] + s[-remaining + k:] 

        elif remaining == k:
            
            last = s[-remaining:][::-1]
        elif remaining > 0:
            last = s[-remaining:][::-1]
        res = ''
        for i in range(0, len(s) - remaining,2*k):
            rev = s[i:i+k][::-1]
            res  += rev + s[i+k:i+2*k]
        res += last
        return res
s = Solution()
print(s.reverseStr("abcd",4))
# @lc code=end


