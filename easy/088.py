# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # my solution

        i = m-1
        while i >= 0 and nums2:
            if nums1[i] < nums2[-1]:
                nums1[i+1:i+1] = [nums2.pop()]
            else:
                i -= 1
        if nums2:
            nums1[0:0] = nums2
        nums1[m+n:] = []
        

        # better solution
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        """
