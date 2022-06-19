#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
from typing import List


class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.topk = [float('-inf')] * k
        nums = sorted(nums)
        length =len(nums)
        if length > k:
            self.topk = nums[-k:]
        elif length!=0:
            self.topk[-length:] = nums

    def add(self, val: int) -> int:
        # if val > self.topk[-1]:
        #     self.topk = self.topk[1:]+ [val]
        if val > self.topk[0]:
            i = 1
            while i < self.k and val > self.topk[i] :
                self.topk[i-1] =self.topk[i]
                i+=1
            self.topk[i-1]= val
        
        return self.topk[0]
        
            

kl = KthLargest(3,[4,5,8,2])
kl.add(3)
print(kl.topk)
kl.add(5)
print(kl.topk)
kl.add(10)
print(kl.topk)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

