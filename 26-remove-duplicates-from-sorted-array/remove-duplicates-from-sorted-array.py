class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        lt=1
        for i in range(1, len(nums)):
            if nums[i] != nums[lt-1]:
                nums[lt]= nums[i]
                lt+=1
        return lt