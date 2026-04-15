class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int) 
        res = 0 
        l=0 
        # maxf = 0 
        for i in range(len(s)):
            letterJ = s[i]
            count[letterJ] += 1

            maxfreq = max(count.values())
            curlen = i - l + 1
            if curlen - maxfreq > k :
                count[s[l]] -= 1  
                l += 1
                curlen = i - l + 1

            res = max(res, curlen)
        
        return res 



            # count[s[i]] = 1 + count.get(s[i],0)
            # maxf=max(maxf,count[s[i]])

           
            
        #     res = max(res,i-l + 1)
        # return res 




