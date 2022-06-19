#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0 
        prime = [True] * (n+1)
        count = 0
        
        for i in range(2,n):
            if prime[i]:
                count+=1
                prime[i*i:n:i] = [False] *len(prime[i*i:n:i])
        return count
# @lc code=end

