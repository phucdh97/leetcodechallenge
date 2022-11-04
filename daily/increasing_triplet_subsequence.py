import math
from collections import deque

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        length = len(nums)
        cur_min_val= nums[0]
        cur_medium_val = math.inf

        for i in range(1, length):
            if nums[i] > cur_medium_val:
                return True
            else:
                if nums[i] < cur_min_val:
                    # cur_medium_val = min(cur_medium_val, cur_min_val)
                    cur_min_val = nums
                elif nums[i] > cur_min_val:
                    cur_medium_val = min(cur_medium_val, nums[i])
                        
        return False

    def rob(self, nums: list[int]) -> int:

#[1,1,-2,6]
