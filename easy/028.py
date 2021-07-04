# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP Algorithm
        # https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
        # haystack: text, needle: pattern

        M = len(needle)
        N = len(haystack)

        if M == 0:
            return 0
        elif N == 0:
            return -1

        # Create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = [0]*M
        j = 0 # index for pat[]

        # Preprocess the pattern (calculate lps[] array)
        computeLPSArray(needle, M, lps)

        i = 0 # index for txt[]
        while i < N:
            if needle[j] == haystack[i]:
                i += 1
                j += 1

            if j == M:
                return (i-j)
                j = lps[j-1] # ???

            # mismatch after j matches
            elif i < N and needle[j] != haystack[i]:
                # do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1

def computeLPSArray(pat, M, lps):
    length = 0 # length of the previous longest prefix suffix

    lps[0] # lps[0] is always 0
    i = 1

    # The loop calculates lps[i] for i = 1 ~ M-1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 8. The idea is similar
            # to search step.
            if length != 0:
                length = lps[length-1]
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
