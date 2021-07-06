class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # my solution
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)
        """

        # my solution 2
        i = 0
        for n in nums:
            if target <= nums[i]:
                return i
            i += 1
        return i
