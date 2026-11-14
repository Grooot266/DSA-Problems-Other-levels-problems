class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Sliding Window Sol
        dt={}
        sz = len(nums)
        
        for i in range(sz):
            rem = target - nums[i]
            if rem in dt:
                return [dt[rem],i]
            dt[nums[i]]=i
        