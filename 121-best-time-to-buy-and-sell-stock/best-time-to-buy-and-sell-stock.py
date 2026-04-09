class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_prf = prices[0]
        ans = 0
        for i in range(1,n):
            curr_prf = prices[i] - min_prf  
            ans = max(curr_prf,ans)
            min_prf = min(min_prf,prices[i])

        return ans 
    
        