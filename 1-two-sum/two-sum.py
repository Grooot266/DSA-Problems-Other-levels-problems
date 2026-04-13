class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       num_map={}
       n=len(nums)

       for i in range(n) :
            rem = target-nums[i]
            if rem in num_map:
                return [num_map[rem],i]
            num_map[nums[i]]=i



            