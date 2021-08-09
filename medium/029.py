# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # my solution - time exceeded
        """
        if dividend == 0: return 0
        negative = False
        if dividend*divisor < 0:
            negative = True
            dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        return quotient if not negative else -1*quotient
        """

        # better solution
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += i
                i <<= 1
                temp <<= 1
        if not positive:
            quotient = -quotient
        return min(max(-(2**31), quotient), 2**31-1)
