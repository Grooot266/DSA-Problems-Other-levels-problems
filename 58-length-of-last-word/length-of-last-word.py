class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip().split()

        if not s : 
            return 0 
        
        else : 
            return len(s[-1])
