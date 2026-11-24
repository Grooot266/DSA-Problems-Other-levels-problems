class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Two pointer method

        #Initialize pointers by assign the values and a empt list
        lt = 0
        rt = len(nums)-1
        ans=[]

        while lt <= rt :    #looping till the condition not satisfy
            if abs(nums[lt]) > abs(nums[rt]):    #if absolute value of left pointer is greater than the absolute value right pointer then ans empty list is appended by its value and left pointer will increase by one 
                ans.append(nums[lt] ** 2)
                lt +=1
            else:       #otherwise the right pointer value will appended into the list and right pointer will be decremented
                ans.append(nums[rt] ** 2)
                rt-=1
        ans.reverse()       #In the end will reverse the ans list 
        return ans