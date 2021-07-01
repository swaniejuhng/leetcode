# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while True:
            if i == len(nums):
                break
            if nums[i] == val:
                del nums[i:i+1]
            else:
                i = i + 1
        return len(nums)
