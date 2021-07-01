# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # my solution
        # short = strs[0]
        # for s in strs:
        #     if len(s) == 0:
        #         return ""
        #     if len(s) < len(short):
        #         short = s

        # strs_new = [s for s in strs if s != short]

        # for i in range(len(short)):
        #     flag = False
        #     for s in strs_new:
        #         if s[i] != short[i]:
        #             flag = True

        #     if flag:
        #         if i > 0:
        #             return short[:i]
        #         else:
        #             return ""
        # return short


        # better solution
        if not strs:
            return ""

        short = min(strs, key=len)
        for i, c in enumerate(short):
            for other in strs:
                if other[i] != c:
                    return short[:i]

        return short
