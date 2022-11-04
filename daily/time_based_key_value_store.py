
class TimeMap:

    def __init__(self):
        self.dic = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        element = (timestamp, value)
        if key not in self.dic:
            self.dic[key] = [element]
        else:
            self.dic[key].append(element)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        values = self.dic[key]
        last_ts, last_val = values[-1]
        if last_ts <= timestamp:
            return last_val

        left = 0
        right = len(values)-1
        idx = -1
        while left <= right:
            mid = (left+right)//2
            ts , _ = values[mid] 
            if ts <= timestamp:
                left = mid+1
                idx = mid
            else:
                right = mid-1
        
        if idx == -1:
            return ""

        _, value = values[idx]
        return value





        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)