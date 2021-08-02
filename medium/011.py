# tps://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # my solution - couldn't solve it
        """
        first, second = 0, 0

        print(len(height))
        for i in range(1, len(height)):
            if height[i] >= height[first]:
                second = first
                first = i

        print(first, second)
        return height[second]*abs(first-second)
        """

        # better solution
        L = 0; R = len(height)-1
        width = len(height)-1
        result = 0

        for w in range(width, 0, -1):
            if height[L] < height[R]:
                result = max(result, height[L]*w)
                L += 1
            else:
                result = max(result, height[R]*w)
                R -= 1
        return result
