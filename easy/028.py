# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP Algorithm
        # https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
        # haystack: text, needle: pattern
        M = len(needle); N = len(haystack)
        if M == 0:
            return 0

        lps = [0]*M
        j = 0 # index for pat[] (needle[])

        # Preprocess the pattern (calculate lps[])
        computeLPSArray(needle, M, lps)

        i = 0 # index for haystack[]
        while i < N:
            if needle[j] == haystack[i]:
                i += 1
                j += 1

            if j == M:
                return i-j

            elif i < N and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1

        return -1

def computeLPSArray(needle, M, lps):
    length = 0 # length of the previous longest prefix suffix

    # lps[0] = 0 always
    i = 0

    while i < M:
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
