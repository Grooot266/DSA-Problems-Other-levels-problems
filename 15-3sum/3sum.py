class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #Two pointer solution method :- 

        nums.sort()     #Sorting the List(array) 
        n=len(nums)     #taking the length of the list
        res = []        #declaring res list for founded triplets to be stored

        for i in range(n):  #Now looping through the list length
            if nums[i] > 0: # checking the condition whether index value is greater than 0 then it will break loop otherwise if the duplicates are found then it will continue
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1,n-1       #Declaring left and right pointers by assigning the 1st index value and last index value
            while left < right:   #Using while loop till it satisfy the condition
                total = nums[i] + nums[left] + nums[right] #Taking the sum of those index's values 
                if total == 0 : #if the sum value is equal to 0 then it will append this value to the result and increase the left pointer by 1 and decrease right pointer by 1
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1 
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: #Again looping with condition whether the current left pointer holds the previous right pointer value or not if it is then increamenting the left pointer by one and vice versa
                        left += 1
                    while left < right and nums[right] == nums[right+1]: 
                        right -= 1
                elif total < 0 : # if the sum is less than 0 then it will increase left pointer or if it is more than 0 then right pointer
                    left += 1
                else : 
                    right -= 1
        return res

