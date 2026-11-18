class Solution:
    def minimumSteps(self, s: str) -> int:
        # Two pointer method sol
        ans, lt = 0, 0 #pointers defined 
        for ch in s :     #looping with every character present in string
            if ch == '1':  #if the char is 1 then left pointer will be incremented by 1 
                lt += 1
            else:
                ans += lt   #else the ans will get assigned by the left pointer value

        return ans