import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # recursion method 1 : closed return 
        # return n
        #method 2 : from math library gcd function import

        sumOdd = n*n
        sumEven = n*(n+1) 

        return math.gcd(sumEven,sumOdd)

