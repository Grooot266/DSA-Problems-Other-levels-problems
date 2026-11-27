class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #Binary Search Algorithm

        n = len(nums)   #Defined length of array
        l,r = 0,n-1     #Defined left and right pointer with values assigned

        while l<=r :    #for i in range (n):    #Can be used for or while too 
            mid = (l+r)//2          #Defining middle value of the array 

            if target>nums[mid]:    #if the target value is higher than mid value then shifting left pointer with next of middle value 
                l = mid+1                     
            elif target<nums[mid]:      #if the target value is lower than mid value then shifting right pointer with previous of middle value 
                r = mid-1

            else:           #if the target value is matched then returing mid value or else return -1
                return mid
        return -1 


