class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
                return False 
            
        ds = s + s 

        return goal in ds 
    

        