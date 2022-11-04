class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        # lastRow = [0]*n
        for i in range(m):
            for j in range(n):
                if j > 0:
                    if i > 0 and matrix[i][j] != matrix[i-1][j-1]:
                        return False
                    # lastRow[j-1] = matrix[i][j-1]
            # lastRow[-1] = matrix[i][-1]

        return True

sol = Solution()
kq = sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
print(kq)