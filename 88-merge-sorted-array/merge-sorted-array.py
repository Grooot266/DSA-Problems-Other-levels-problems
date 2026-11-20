class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Two pointers method sol
        #Setup pointers 
        m_idx = m-1
        n_idx = n-1
        right = m+n-1

        #looping till the nums2 has numbers
        while n_idx >=0 :
            #picking-up max number and put it to the right position
            if m_idx >=0 and nums1[m_idx] > nums2[n_idx]:
                nums1[right] = nums1[m_idx]
                m_idx -= 1
            else:
                nums1[right]=nums2[n_idx]
                n_idx -= 1
            #moving right position to the left 
            right -= 1
