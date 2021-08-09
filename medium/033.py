# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, left, right, target):
            # my solution - failed
            """
            mid = (left+right)//2
            if nums[left] == target:    return left
            elif nums[right] == target: return right
            elif nums[mid] == target:   return mid
            # elif left == right and nums[left] == target:
            #     return left
            if nums[left] > nums[right]:
                helper(nums, left+1, mid-1, target)
            else:
                helper(nums, mid+1, right-1, target)

        index = helper(nums, 0, len(nums)-1, target)
        print(index)
        if not index:
            return -1
        return index
        """

        # better solution
        if not nums:    return -1
        left = 0; right = len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
