class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Two pointer Sol\
        s = str(x)
        lp = 0 
        rp = len(s)-1

        while lp < rp :
            if s[lp] != s[rp]:
                return False
    
            lp += 1
            rp -= 1
        return True



