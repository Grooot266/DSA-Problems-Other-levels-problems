class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pointer sol
        start = 0 
        ptr = len(nums)

        for i in range(ptr) :
            if nums[i]!=0 :
                nums[i],nums[start] = nums[start],nums[i]
                start+=1
        
