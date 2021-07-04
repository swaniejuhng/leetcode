# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # my solution
        """
        if x < 0:
            return False

        num_max = 1<<31-1; num_min = -1<<31

        x = str(x)
        length = len(x)
        for i in range(length//2):
            if x[i] != x[length - i - 1]:
                return False
        return True
        """

        # better solution - faster
        if x < 0:
            return False
        return int(str(x)[::-1]) == x
