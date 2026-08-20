class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1)
        j = 0
        
        for i in range(m,k):
            if j<n:
                nums1[i] = nums2[j]
                j += 1

        nums1.sort()

