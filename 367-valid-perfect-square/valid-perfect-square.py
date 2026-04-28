class Solution:
    def isPerfectSquare(self, num: int) -> bool:
       r = int(num ** 0.5)
       return r * r == num 
