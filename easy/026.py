# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # my solution
        """
        i = 0
        while True:
            if i >= len(nums) - 1:
                break
            if nums[i] == nums[i+1]:
                del nums[i:i+1] # I think this del operation takes some time
            else:
                i = i + 1
        return len(nums)
        """

        # better solution
        x = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x+=1
        return x
