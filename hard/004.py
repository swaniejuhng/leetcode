# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # my solution
        """
        merged = []
        sum_length = len(nums1)+len(nums2)
        odd_flag = sum_length % 2 > 0

        target_length = (sum_length+2)//2
        while len(merged) < target_length:
            if not nums1:
                merged.append(nums2.pop())
            elif not nums2:
                merged.append(nums1.pop())
            else:
                if nums1[-1] >= nums2[-1]:
                    merged.append(nums1.pop())
                elif nums2[-1] > nums1[-1]:
                    merged.append(nums2.pop())

        if odd_flag:
            return merged[-1]
        else:
            return (merged[-2]+merged[-1])/2
        """

        # better solution
