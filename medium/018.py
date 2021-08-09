# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # my solution
        result = set()
        nums = sorted(nums)
        # differences = [nums[i]-nums[i-1] for i in range(1, len(nums))]
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                left = j+1; right = len(nums)-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1; right -= 1
                        while left < right and nums[left-1] == nums[left]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        return result

        # better solution
        # ????
