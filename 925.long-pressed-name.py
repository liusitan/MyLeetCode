#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ln = 0
        rn = 0
        lt = 0
        rt = 0
        len_name = len(name)
        len_typed = len(typed)
        while ln < len_name and lt < len_typed:
            if name[ln] == typed[lt]:
                while rn < len_name and  name[rn] == name[ln]:
                    rn+=1
                while rt < len_typed and typed[lt]==typed[rt]:
                    rt +=1
                if (rn - ln > rt - lt):
                    return False
                else:
                    ln = rn
                    lt = rt
            else:
                return False
        if ln == len_name and lt == len_typed:
            return True
        
        return False
s = Solution()
print(s.isLongPressedName("alex",
"aaleex"))
# @lc code=end  

