class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        #Sliding window grows or size 

        
        count = collections.defaultdict(int) #This dictionary maps each fruit type in the current window to how many of it are there.

        l,total,res = 0,0,0 #initial left edge of the window, total is the number of fruits in current window and res is best total so far

        for r in range(len(fruits)): #r is the right edge of the window 
            count[fruits[r]]+=1    #This picks the fruit at tree r: it adds one to that type's count and to the window size.
            total +=1 

            while len(count) > 2: #If the window now has 3 types, it need a third basket, which isn't allowed. The window has to shrink from the left until only 2 types remain.

                f = fruits[l] #the fruit type at the left edge, which is about to leave the window.

                count[f] -= 1   
                total -= 1
                l+=1
                #It removes that fruit and lowers its count, also shrinks the window size, and moves the left edge right.
            
                if not count[f]: #checking if the count is reached 0 then it will be no longer in the window and the key should be removed
                    count.pop(f)
                
            res = max(res,total) #taking the better maximum count so far and returning the result

        return res 
