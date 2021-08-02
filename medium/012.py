# https://leetcode.com/problems/integer-to-roman/submissions/

class Solution:
    def intToRoman(self, num: int) -> str:
        # my solution - I think mine is okay
        roman_dict = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        result = ""
        keys = sorted(roman_dict.keys(), reverse=True)
        while num > 0:
            if num >= 1000:
                i = 0
            else:
                for i in range(1, len(keys)):
                    if keys[i] <= num < keys[i-1]:
                        break

            if str(num)[0] == '4':
                result += roman_dict[keys[i]]+roman_dict[keys[i-1]]
                num -= (keys[i-1]-keys[i])
                continue
            elif str(num)[0] == '9':
                result += roman_dict[keys[i+1]]+roman_dict[keys[i-1]]
                num -= (keys[i-1]-keys[i+1])
                continue

            result += roman_dict[keys[i]]
            num -= keys[i]

        return result
