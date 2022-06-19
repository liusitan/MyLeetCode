#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vs1 = version1.split(".")
        vs2 = version2.split(".")
        for i1,i2 in zip(vs1,vs2):
            if int(i1) > int(i2):
                return 1
            elif int(i1)<int(i2):
                return -1
        if len(vs1)> len(vs2):
            remaining = vs1[len(vs2):]
            for i in remaining:
                if int(i) > 0:
                    return 1
        elif len(vs1)== len(vs2):
            return 0
        else:
            remaining = vs2[len(vs1):]
            for i in remaining:
                if int(i) > 0:
                    return -1
        return 0
            
# @lc code=end

