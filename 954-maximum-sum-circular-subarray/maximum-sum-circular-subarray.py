class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax, globalmin = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = 0 

        for i in nums: 
            currMax = max(currMax + i, i )
            currMin = min(currMin + i, i )
            total += i
            globalmax = max(globalmax, currMax)
            globalmin = min(globalmin, currMin)

        return max(globalmax, total - globalmin) if globalmax > 0 else globalmax

