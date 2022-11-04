class Solution:
    def search(self, nums: list[int], target: int) -> int:
        length = len(nums)
        if length == 1:
            if nums[0] == target:
                return 0
            return -1

        left = 0
        right = length-1

        split_idx = length
        rotated_value = nums[0]

        while left <= right:
            mid = (left+right)//2

            if (mid == length -1) or (nums[mid+1] < nums[mid]):
                split_idx = mid+1
                break
            elif nums[mid] > rotated_value:
                left = mid+1
            elif nums[mid] < rotated_value:
                right = mid
            else:
                break
                

        left, right = 0, length - 1
        if  split_idx != length:
            if target < rotated_value:
                left = split_idx
            else:
                right = split_idx-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return -1

sol = Solution()
sol.search([8,9,2,3,4], 9)
        
            


                   