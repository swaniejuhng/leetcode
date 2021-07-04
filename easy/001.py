# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # my solution
        """
        n = len(nums)
        for i in range(n-1): # i = 0 ~ (n-2)
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """

        # better solution
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen: # not sure what the time complexity of this line would be
                return [i, seen[remaining]]
            else:
                seen[value] = i # index of the other value
