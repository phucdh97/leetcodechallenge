from collections import Counter
import heapq
from itertools import count


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counter = Counter(words)
        
        def compare(obj):
            key, val = obj
            return val[0], key[0]

        values = []
        for key, val in counter.items():
            values.append((key, val))
        values.sort(key=compare)

        ans = []
        for i in range(k):
            ans.append(values[i])
        
        return ans


        

            