class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        countDiff = 0
        length = len(dominoes)
        dominoes =[i for i in dominoes]
        pre = 0
        cur = 0
        next = 1
        while True:
            countDiff = 0
            lastState = dominoes.copy()
            for i in range(length):
                cur = i
                pre = i-1
                next = i+1

                if lastState[cur] == '.':
                    isvalid_next = next <= length-1
                    isvalid_pre = pre >= 0
                    if isvalid_pre and lastState[pre] == 'R':
                        next_is_left = isvalid_next and lastState[next] == 'L'
                        if not next_is_left:
                            dominoes[cur] = 'R'
                            countDiff += 1
                    elif isvalid_next and lastState[next] == 'L': #pre != R
                        dominoes[cur] = 'L'
                        countDiff += 1
            print("cur:", dominoes)
            print("\n")
            if countDiff == 0:
                break
        print("last:", dominoes)
        ans = ''.join(dominoes)
        return ans

sol = Solution()
data = str(input())
sol.pushDominoes(data)
            

            
                        
