class Solution:
    def longestPalindrome(self, s: str) -> str:
        # my solution - definitely not the best
        """
        import numpy as np

        start = 0
        end = 0
        max_len = 0

        for i in np.arange(0.5, len(s)-1, 0.5):
            if i % 1 > 0:
                temp = 0.5
            else:
                temp = 1

            for j in np.arange(temp, min(i, len(s)-i-1)+1, 1):
                if s[int(i-j)] != s[int(i+j)]:
                    break
                if max_len < 2*j+1:
                    max_len = 2 * j + 1
                    start = int(i-j)
                    end = int(i+j)
        return s[start:end+1]
        """

        # better solution
