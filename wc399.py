class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [[1]*(n+1) for i in range(n+1)]
        dp[1][1] = 1
        for i in range(1,n+1):
            for j in range(1,n+1):
                if ( j) > (i - i//2):
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-2][j-1] + dp[i-1][j]
        res = 0
        max_plots_one_side = (n + 1)//2
        for total_houses in range(2*n+1):
            for p1 in range( max_plots_one_side+1):
                for p2 in range(max_plots_one_side+1):
                    if (p1+p2)==total_houses:
                        res += dp[n][p1] * dp[n][p2]

        return res
s = Solution()
print(s.countHousePlacements(1))