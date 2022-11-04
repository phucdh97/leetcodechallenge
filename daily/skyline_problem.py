from distutils.command.build import build


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        max_right = 0
        max_height = 0
        last_height = 0
        last_left = 0

        ans = []
        for l, r, h in buildings:
            cur = []
            if h > max_height or r > max_right:
                if r > right_most:
                    right_most = r

