class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ws =set()
        for i in range(len(nums)):
            if i > k :
                ws.remove(nums[i-k-1])
            
            if nums[i] in ws :
                return True
            
            ws.add(nums[i])

        return False
        
