class Solution:
    def maxArea(self, height: list[int]) -> int:
        #Two pointer solution 
        lh=0
        rh=len(height)-1
        area=0

        while lh < rh : 

            area=max(area, (rh - lh) * min(height[lh],height[rh]))
            if height[lh] < height[rh]:
                lh +=1
            else:
                rh -=1
            
        return area

        
