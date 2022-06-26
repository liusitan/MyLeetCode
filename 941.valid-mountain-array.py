#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
            i = 0
            while (i < len(arr)-1 and arr[i] < arr[i+1]):
                i +=1
            if i == len(arr)-1 or i == 0:
                return False
            while(i < len(arr)-1 and arr[i] > arr[i+1]):
                i+=1
            if i == len(arr) - 1:
                return True
            return False
# @lc code=end

