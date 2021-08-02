# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        # my solution - what a shitty problem - failed
        """
        positive = False
        negative = False
        numeric = False
        result = []

        for c in s:
            print(c, c.isnumeric())
            if c == " " or c == "\t":
                if numeric:
                    break
            elif c == "-":
                if numeric or positive:
                    return 0
                negative = True
            elif c == "+":
                if numeric or negative:
                    return 0
                positive = True
            elif c == ".":
                break
            elif c.isnumeric():
                numeric = True
                result.append(c)
            else:
                break

        if len(result) == 0:
            return 0

        result = int("".join(result))

        if negative:
            result = (-1) * result

        if result >= 2**31:
            return 2**31-1
        elif result < -2**31:
            return -2**31
        return result
        """

        # better solution
        if len(s) == 0:     return 0
        ls = list(s.strip())
        if len(ls) == 0:    return 0

        if ls[0] == '-':    sign = -1
        else:               sign = 1

        if ls[0] in ['-', '+']:
            del ls[0]

        result = 0; i = 0

        while i < len(ls) and ls[i].isdigit():
            # ord() accepts a string of unit length as san argument and
            # returns the Unicode equivalence of the passed argument
            result = result*10 + (ord(ls[i]) - ord('0'))
            i += 1

        return max(-2**31, min(sign*result, 2**31-1))
