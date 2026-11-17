class Solution:
    def trap(self, height: list[int]) -> int:
        # Two pointers optimal solution 
        lp=0
        rp=len(height)-1

        leftmax = 0 
        rightmax = 0 
        totalwater = 0

        while lp < rp:
            leftmax = max(leftmax, height[lp])
            rightmax = max(rightmax,  height[rp])

            if leftmax < rightmax:
                totalwater += leftmax - height[lp]
                lp +=1 
            else :
                totalwater += rightmax - height[rp]
                rp -=1
            
        return totalwater
       
       
       
    #    Brute force 
       
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