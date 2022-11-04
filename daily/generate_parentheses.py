class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        def dp(n):
            print("n:", n)
            if n == 1:
                return ["()"]
            if n == 2:
                return ["(())", "()()"]
            ans = set()
            for i in range(1, n):
                left = dp(i)
                right = dp(n-i)
                for l in left:
                    for r in right:
                        val = l + r
                        ans.add(val)
                if i == 1:
                    for r in right:
                        val = "(" + r + ")"
                        ans.add(val)
            return list(ans)  
                        
        ans = dp(n)
        print(ans)
        return ans

    def test(self):
        data = "bot"
        sub1 = data[:0]
        sub2 = data[0:]
        print("sub1: ", sub1)
        print("sub2: ", sub2)
    
sol = Solution()
# sol.generateParenthesis(4)
sol.test()