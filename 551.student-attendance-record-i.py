#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
from operator import countOf


class Solution:
    def checkRecord(self, s: str) -> bool:
        countL = 0
        totalA = 0
        maxCountL = 0
        for i in s:
            if i == 'A':
                totalA +=1
                countL += 0
            if i == 'L':
                countL += 1
            else:
                maxCountL = max(maxCountL, countL)
                countL =  0
        maxCountL = max(maxCountL, countL)

        return maxCountL < 3 and totalA< 2
# @lc code=end

