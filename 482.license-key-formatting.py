#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sc = s[:]
        scs = sc.split("-")
        wodash = ''.join(scs)
        wodash = wodash.upper()
        first_group_size = len(wodash ) %k
        res = []
        if first_group_size != 0:
            res = [wodash[:first_group_size]]

        for i in range(first_group_size,len(wodash),k):
            res.append(wodash[i:i+k])
        return '-'.join(res)
# @lc code=end

