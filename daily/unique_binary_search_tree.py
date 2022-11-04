

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        if n <= 2:
            return n

        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            rs = 0
            for j in range(1, i+1):
                right = i - j
                left = j-1
                if right == 0:
                    rs += dp[left]
                elif left == 0:
                    rs += dp[right]
                else:
                    rs += dp[left] * dp[right]
            dp[i] = rs
        return dp[n]




