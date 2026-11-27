class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #Binary Search Method
        #Defining left and right side pointers    
        l, r = 1, max(piles)    #taking maximum pile present in the list
        res = r         
        while l <= r :          #Looping from left to the right 
            k = (l+r)//2        #Taking k as a count of banaas could be eaten 
            hours = 0            #defining hours  as 0 initially
            for p in piles :    #now looping through the piles 
                hours += math.ceil(p / k)       #dividing the pile bananas with the count of the bananas to increment the n_bananas/hours
            if hours <= h :     #Checking by condition if the calculated hours taken to eat bananas is less or greater than the specified hours  
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1
        
        return res 