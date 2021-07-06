class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # my solution - Kadane algorithm
        max_so_far = 0
        max_ending = 0
        # start = 0 # no need to keep indices
        # end = 0
        # s = 0
        max_index = -1

        for i in range(len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i
            max_ending += nums[i]

            if max_so_far < max_ending:
                max_so_far = max_ending
                # start = s
                # end = i

            if max_ending < 0:
                max_ending = 0
                # s = i + 1

        if nums[max_index] <= 0:
            return nums[max_index]
        return max_so_far
