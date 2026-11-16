class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Sliding Window method
        lt= 0
        res=[]
        cnt=1

        for rt in range(len(nums)):
            if rt > 0 and nums[rt-1]+1 == nums[rt]:
                cnt += 1
            if rt - lt + 1 > k :
                if nums[lt] + 1 == nums[lt + 1]:
                    cnt -= 1 
                lt += 1
            if rt -lt + 1 == k : 
                res.append(nums[rt] if cnt == k else -1)
        return res
        
