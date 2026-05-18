class Solution:
    def lowerbond(self, nums: List[int], target: int) -> int:
        l=0 
        r=len(nums)-1 
        ans = len(nums)

        while l <= r :
            mid = (l+r)//2 

            if nums[mid]>=target:
                ans=min(ans,mid)
                r = mid-1 
            else : 
                l = mid + 1 
        
        return ans 
            
        
    def upperbond(self, nums: List[int], target: int) -> int:
        l=0 
        r=len(nums)-1 
        ans = len(nums)

        while l <= r :
            mid = (l+r)//2 

            if nums[mid]>target:
                ans=min(ans,mid)
                r = mid-1 
            else : 
                l = mid + 1 
        
        return ans 

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerbond(nums,target)
        ub = self.upperbond(nums,target)

        if lb == ub : 
            return [-1,-1]
        else :
            return [lb,ub-1]

        