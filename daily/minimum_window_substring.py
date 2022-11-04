class CustomDict:
    def __init__(self, t: str) -> None:
        self.data = {}
        self.count = 0 
        for c in t:
            self.data[c] = 0
        self.target  = len(t)
        print("data- target: ", self.data, self.target)
        
    def add(self, val):
        x = self.data.get(val, 0)
        self.data[val] = x+1
        self.count += 1
        print("add - count: ", val, self.count)
        
    def remove(self, val):
        x = self.data.get(val, 0)
        self.data[val] = x-1
        self.count -= 1
        print("remove - count: ", val, self.count)

    def contain(self, val) ->bool:
        return val in self.data
    
    def isValid(self) -> bool:
        print("testsssss")
        print("isValid: ", self.count == self.target)
        return self.count == self.target

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def findNext(s: str, d: CustomDict, start: int, end:int):
            while start <= end:
                if  d.contain(s[start]):
                    print("find next:", start)
                    return start
                start += 1
            return end+1 #if can't find value, return out of range to break while loop

        dic = CustomDict(t)
        length = len(s)
        left = findNext(s, dic, 0, length-1)
        right = left
        dic.add(s[right])
        
        ans = ""
        while left <= right and right < length:
            print("left: {}, right: {}".format(left, right))
            if dic.isValid:
                if right-left+1 < len(ans) or ans == "":
                    ans = s[left:right+1]
                dic.remove(s[left])
                left = findNext(s, dic, left+1, length-1)
            else:
                right = findNext(s, dic, right+1, length-1)
                dic.add(s[right])
        
        return ans
            

sol = Solution()
rs = sol.minWindow("ADOBECODEBANC", "ABC")

