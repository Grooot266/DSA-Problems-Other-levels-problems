class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #Using Kadane's Algorithm

        ans = nums[0]           # assigning ans var with first index value of nums
        curr_sum = 0            # initializing curr_sum with 0

        for i in nums:          #going with every element value
            curr_sum+=i         #adding value of nums in curr_sum
            if curr_sum > ans:  #checking if current sum is grater than ans then ans value will replace with current sum value
                ans = curr_sum
            if curr_sum < 0:    #if current sum value is less than 0 then assign current sum value as 0
                curr_sum =0
        return ans
