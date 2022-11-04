class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        def firstBitPos(n) -> int:
            rs = 0
            for i in range(32):
                if (1 << i) & n:
                    rs = i+1
            # print("n - rs ", n, i+1)
            return rs
        
        memo = {}
        
        def dp(n):
            if n in memo:
                return memo[n]
            
            if n == 1:
                return 1
            
            pos = firstBitPos(n)
            ans = dp(n-1)
            ans = (ans << pos) + n
            memo[n] = ans
            return ans
        ans = dp(n)
        return ans % (10**9+7)
        
            