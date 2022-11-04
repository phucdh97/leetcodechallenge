class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        length = len(colors)

        ans = 0
        cur = 0
        for i in range(length-1):
            if colors[i] == colors[i+1]:
                t1, t2 = neededTime[i], neededTime[i+1]
                if t1 <= t2:
                    ans += t1
                else:
                    ans += t2
                    neededTime[i+1] = t1
        return ans
