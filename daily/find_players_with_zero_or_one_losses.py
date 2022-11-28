from collections import defaultdict
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        dic = defaultdict(int)
        for  winner, loser in matches:
            if dic[winner] >= 0:
                dic[winner] = 1
            if dic[loser] >= 0:
                dic[loser] = -1
            elif dic[loser] < 0:
                dic[loser] -= 1

        list1 = []
        list2 = []

        for key, value in dic.items():
            if value == 1:
                list1.append(key)
            if value == -1:
                list2.append(key)

        list1.sort()
        list2.sort()
        return [list1, list2]