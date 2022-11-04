class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
       
        data = {}
        for i in range(n):
            data[i] = i
        for i in range(m):
            invalidCount = 0
            for key, value in data.items():
                if value == -1:
                    invalidCount += 1
                    continue
                elif value == 0:
                    if grid[i][value] == -1:
                        data[key] = -1 #skip tracking
                    else:
                        data[key] = value+1
                elif value == n-1:
                    if grid[i][value] == 1:
                        data[key] = -1
                    else:
                        data[key] = value-1

                elif grid[i][value] == 1:
                    if grid[i][value+1] == -1:
                        data[key] = -1
                    else:
                        data[key] = value+1
                else:
                    if grid[i][value-1] == 1:
                        data[key] = -1
                    else:
                        data[key] = value-1
            if invalidCount == n:
                return [-1]*n
            print("\n", data)

        ans = []
        keys = list(data.keys())
        keys.sort()
        for key in keys:
            ans.append(data[key])

        return ans

sol = Solution()
sol.findBall([[1,-1,-1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1],
[-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1],
[1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1]])