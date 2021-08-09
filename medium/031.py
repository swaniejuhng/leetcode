# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # my solution - failed
        """
        result = []; sorted_flag = False
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                if i == 1:
                    nums[0:0] = [nums.pop()]
                else:
                    nums[i-1:] = sorted(nums[i-1:], reverse=True)
                # print(nums)
                sorted_flag = True
                break
        if not sorted_flag:
            nums.sort()
        """

        # better solution
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0: # nums are in descending order
            nums.reverse()
            return
        k = i - 1 # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[j], nums[k] = nums[k], nums[j]
        l, r = k+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
