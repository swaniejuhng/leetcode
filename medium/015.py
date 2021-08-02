# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # my solution - failed b/c of time limit
        """
        result = set()
        for i in range(len(nums)-2):
            for j in range(i, len(nums)-1):
                if i == j: continue
                if (-nums[i]-nums[j]) in nums[j+1:]:
                    k = nums[j+1:].index(-nums[i]-nums[j])+j+1
                else: continue
                if i != k and j != k:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return result
        """


        # better solution
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1; r = len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return result
