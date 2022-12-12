class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0,1,2]
        i = 3
        while i <= n:
            dp.append(dp[i-2]+dp[i-1])
            i+=1
        return dp[n]