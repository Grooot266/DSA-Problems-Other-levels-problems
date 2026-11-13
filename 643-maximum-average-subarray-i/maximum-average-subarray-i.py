class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Sliding Window sol : 

        cs=0
        n=len(nums)

        for i in range(k):
            cs+=nums[i]

        ans = cs/k

        for i in range(k,n):
            cs+=nums[i]
            cs-=nums[i-k]

            ans=max(ans,cs/k)
        
        return ans