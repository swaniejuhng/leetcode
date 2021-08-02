# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # my solution - based on better solution of problem 015
        result = None
        nums.sort()
        min_diff = None
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1; r = len(nums)-1
            while l < r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == target:
                    return sum
                diff = sum-target
                if not min_diff or min_diff > abs(diff):
                    min_diff = abs(diff)
                    result = sum
                if diff < 0:
                    l += 1
                elif diff > 0:
                    r -= 1

        return result
