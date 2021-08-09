# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # my solution
        left = 0; right = len(nums)-1; found = False
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                found = True; break
        if not found:
            return [-1, -1]
        left = right = mid
        while left - 1 >= 0 and nums[left-1] == target:
            left -= 1
        while right + 1 <= len(nums)-1 and nums[right+1] == target:
            right += 1
        return [left, right]
