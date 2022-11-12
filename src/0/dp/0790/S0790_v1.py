class Solution:
    def numTilings(self, n: int) -> int:
        dp = [None] * 1001
        s, dp[0], dp[1] = 0, 1, 1
        for i in range(2, n+1):
            dp[i] = (s + dp[i-1] + dp[i-2]) % 1000000007
            s += dp[i-2] << 1
        return dp[n] 
