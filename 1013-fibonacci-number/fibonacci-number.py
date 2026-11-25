class Solution:
    def fib(self, n: int) -> int:
        #Recursion Method

        #base case
        if n==0 or n==1:
            return n 
        
        #Recursion case
        return self.fib(n-1) + self.fib(n-2)
