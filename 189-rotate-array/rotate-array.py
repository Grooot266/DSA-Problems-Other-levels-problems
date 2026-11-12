class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pointer solution :- 
        def two_pointer(arr,lt,rt):
            while lt < rt:
                arr[lt],arr[rt]=arr[rt],arr[lt]
                lt += 1
                rt-= 1
            return arr
        
        if k > len(nums):
            k %= len(nums)
        
        if  k > 0 :
            two_pointer(nums,0,len(nums)-1)
            two_pointer(nums,0,k-1)
            two_pointer(nums,k,len(nums)-1)
