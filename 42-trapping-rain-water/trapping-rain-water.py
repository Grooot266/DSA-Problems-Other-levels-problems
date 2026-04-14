#Grooot266
class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointers optimal solution 
        l=0
        r=len(height)-1

        leftmax = 0 
        rightmax = 0 
        totalwater = 0

        while l < r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax,  height[r])

            if leftmax < rightmax:
                totalwater += leftmax - height[l]
                l +=1 
            else :
                totalwater += rightmax - height[r]
                r -=1
            
        return totalwater
       
       
       
       
       
        # n = len(height)

        # if n < 1 :
        #     return 0
        
        # ans = 0 
        # left_max = [0] * n
        # right_max = [0] * n

        # left_max[0] = height[0]

        # for i in range(1, n):
        #     left_max[i]= max(left_max[i-1],height[i])
        
        # right_max[-1] = height[-1]

        # for i in range(n-2, -1, -1):
        #     right_max[i] = max(right_max[i+1], height[i])
        
        # for i in range(n):
        #     ans += min(left_max[i],right_max[i])-height[i]
        

        # return ans 


