#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
from os import times


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time = 0; 
        if(len(timeSeries)== 1):
            return duration
        for i in range(0,len(timeSeries)-1):
            time += min(duration,timeSeries[i+1] - timeSeries[i])
        return time + duration
# @lc code=end

