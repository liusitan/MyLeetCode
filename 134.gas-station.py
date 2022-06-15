#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        stations = len(gas)
        tank = 0
        total = 0
        start = 0
        for i in range(stations):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i+1
            total +=  gas[i] - cost[i]
        return start if total >= 0 else -1
    
# @lc code=end

