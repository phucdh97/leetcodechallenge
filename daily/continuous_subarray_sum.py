class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        length = len(nums)
        d = 2
        mm = set()
        mm.add(0) # for case: first 2 elements are satisfied
        preSum = 0
        curSum  = 0
        for i in range(length):
            if i >= d:
                preSum += nums[i-d]
                mm.add(preSum)
            curSum = (curSum + nums[i]) % k
            if curSum in mm:
                return True
        return False

    def checkSubarraySum2(self, nums: list[int], k: int) -> bool:
        length = len(nums)
        prefixSum = [0]*length
        d = 2

        prefixSum[0] = nums[0]
        for i in range(1, length):
            prefixSum[i] = prefixSum[i-1] + nums[i] 
        
        for i in range(length-d+1):
            for j in range(i+d-1, length):
                val = prefixSum[j]  
                if i > 0:
                    val -= prefixSum[i-1]
                if val % k == 0:
                    return True

        return False

                

sol = Solution()
sol.checkSubarraySum([5, 0, 0, 0], 3) 

        

        