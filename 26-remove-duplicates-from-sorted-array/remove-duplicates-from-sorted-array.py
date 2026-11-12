class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

    # brute force:- 

        pt=1
        while pt < len(nums):
            if nums[pt] == nums[pt-1]:
                nums.pop(pt)
            else:
                pt+=1
        return pt 
    # #   Sort

    #     nums[:] =   sorted(set(nums))
    #     return len(nums)

    # #    Two pointers
        # lt=1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[lt-1]:
        #         nums[lt]= nums[i]
        #         lt+=1
        # return lt