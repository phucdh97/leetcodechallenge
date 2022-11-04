class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        
        n = len(nums)
        m = len(multipliers)

        dp = [[0]*(m+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                leftVal = nums[left]*multipliers[i] + dp[i+1][left+1]
                rightVal = nums[n-1-(i-left)]*multipliers[i] + dp[i+1][left]
                dp[i][left] = max(left, rightVal)
                
        return dp[0][0]
                
                
