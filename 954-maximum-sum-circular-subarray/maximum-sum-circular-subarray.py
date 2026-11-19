class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # Kadane algorithm method
        globalmax, globalmin = nums[0], nums[0] #Intializing variables
        currMax, currMin = 0, 0 
        total = 0 

        for i in nums: #looping values of list 
            # taking max/min value by comparing 
            currMax = max(currMax + i, i ) 
            currMin = min(currMin + i, i ) 
            total += i  #taking sum of the values
            #comparing min/max values 
            globalmax = max(globalmax, currMax)
            globalmin = min(globalmin, currMin)

        # returning values by condition pass
        return max(globalmax, total - globalmin) if globalmax > 0 else globalmax
