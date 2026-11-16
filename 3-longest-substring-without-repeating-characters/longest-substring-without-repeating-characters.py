class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding Window method
        lt,longest=0,0
        st = set()
        n=len(s)

        for rt in range(n):
            while s[rt] in st:
                st.remove(s[lt])
                lt += 1 
            
            window = (rt-lt)+1
            longest = max(longest,window)
            st.add(s[rt])
        
        return longest


        