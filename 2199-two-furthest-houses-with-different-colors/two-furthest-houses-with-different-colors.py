class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l=0 
        n=len(colors)
        r=n-1

        while ( colors[r] == colors[0]):
            r -= 1
        while ( colors[l] == colors[n - 1]):
            l += 1
        return max(r, n - 1 - l)

