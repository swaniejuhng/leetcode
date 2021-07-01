# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # my solution - I don't think it's a smart approach
        """
        result = 0; temp = 0
        for i, curr in enumerate(s):
            if i == 0:
                temp = roman_dict[curr]
            else:
                if (prev == "I" and (curr == "V" or curr == "X")) \
                or (prev == "X" and (curr == "L" or curr == "C")) \
                or (prev == "C" and (curr == "D" or curr == "M")):
                    result += (roman_dict[curr] - roman_dict[prev])
                    temp = 0
                else:
                    result += temp # ex. III, XX, ...
                    temp = roman_dict[curr]
            prev = curr # update the prev
        result += temp # add up the remainder
        return result
        """

        # better solution
        result = 0; prev = 0
        for letter in s[::-1]: # reverse of s
            curr = roman_dict[letter]
            if curr >= prev:
                result += curr
            else:
                result -= curr
            prev = curr
        return result
