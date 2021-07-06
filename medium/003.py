# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # my solution - failed to solve it
        """
        if s:
            start = 0
            max_len = 0
            for i, c in enumerate(s):
                if c not in s[start:i+1]:
                    if max_len < (end-start+1):
                        max_len = i - start + 1
                else:
                    start = s[start:i].index(c) + 1

            return max(1, max_len)

        else:
            return 0
        """

        # better solution - similar to mine!
        used = {}
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_len = max(max_len, i-start+1)
            used[c] = i

        return max_len
