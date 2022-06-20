#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = {}
        for i in bills:
            exchange = i - 5
            if exchange>0:
                if exchange == 15:
                    if wallet.get(10,0) > 0:
                        wallet[10] -=1
                        if wallet.get(5,0) > 0 :
                            wallet[5] -=1
                        else :
                            return False
                    else: 
                        if wallet.get(5,0) > 2:
                            wallet[5] -=3
                        else :
                            return False
                elif exchange == 5:
                    if wallet.get(5,0) > 0 :
                        wallet[5] -=1
                    else:
                        return False
            wallet[i] = wallet.get(i,0)+1
        return True
s= Solution()
print(s.lemonadeChange([5,5,5,10,20]))
# @lc code=end

