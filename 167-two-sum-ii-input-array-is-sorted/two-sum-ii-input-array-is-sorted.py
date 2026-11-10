class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Two pointer sol:
        n = len(numbers)
        l=0
        r=n-1
        while r>l:
           sum = numbers[l] + numbers[r]
           if sum > target:
            r-=1
           elif sum < target :
            l+=1
           else : 
            return [l+1,r+1]
        

        
        