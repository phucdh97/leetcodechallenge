from collections import deque
import math

class Solution:
    def trap(self, height: list[int]) -> int:
        def getMaxSum(data, maxVal) -> int:
            sumVal = 0
            count = 0
            for s, _, c in data:
                sumVal += s
                count += c
            rs = count * maxVal - sumVal
            return rs

        def getSum(data) -> int:
            sumVal = 0
            rs = 0
            for s, m, c in data:
                rs += c * m - s
            return rs

        stack = deque()
        ans = 0
        values = []
        for h in height:
            if len(stack) == 0 or h <= stack[-1]:
                stack.append(h)
                continue

            sumValues = 0
            localMax = 0
            count = 0
            while len(stack) != 0 and stack[-1] <= h:
                topValue = stack.pop()
                sumValues += topValue
                count += 1
                localMax = topValue

            if len(stack) == 0:
                stack.append(h)
                rs = localMax*count - sumValues
                rs += getMaxSum(values, localMax)
                ans += rs
                # reset
                values = []
            else:
                stack.append(h)
                localMax = h
                values.append((sumValues, localMax, count))
                # if globalMax == -math.inf:
                #     globalMax = localMax
                # elif localMax >= globalMax:
                #     globalMax = localMax
                #     newS, newM, newC = 0, localMax ,0
                #     for s, _, c in values:
                #         newS += s
                #         newC += c
                #     values = [(newS, newM, newC)]

                if len(values) > 1 and localMax >= values[-1][1]:
                    newS, newM, newC = 0, localMax , 0
                    while len(values) > 0 and localMax >= values[-1][1]:
                        s, _, c = values.pop()
                        newS += s
                        newC += c
                    values.append((newS, newM, newC))


        rs = getSum(values)
        ans += rs
        return ans

sol = Solution()
ans = sol.trap([7,9,8,5,0,0,4,2,7,6,0,8,1,2,3])
print("ans: ",ans)
                    


                    

#[7,9,8,5,0,0,4,2,7,6,0,8,1,2,3]
#[9,2,4,0,3,4]
#[9,2,9,3,2,2,1,4,8]


