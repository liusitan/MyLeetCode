#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return 
        if(s==goal):
            return len(set(s))!=len(s)
        record = []
        for i ,j in zip(s,goal):
            if i !=j:
                record.append(i)
                record.append(j)
                if len(record) > 4:
                    return False
        if len(record)==2:
            return False
        if len(record) == 0:
            return True
        return record[0] == record[-1] and record[1] == record[-2]
                
# @lc code=end

