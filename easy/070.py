# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # my solution
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if (n-1) in pairs_dict.keys():
                first = pairs_dict[n-1]
            else:
                first = pairs_dict[n-1] = self.climbStairs(n-1)
            if (n-2) in pairs_dict.keys():
                second = pairs_dict[n-2]
            else:
                second = pairs_dict[n-2] = self.climbStairs(n-2)
            return first + second

        # alternative solution - but mine is faster and more space-efficient
        """
        a = b = 1
        for i in range(n):
            a, b = b, a + b
        return a
        """

pairs_dict = {}
