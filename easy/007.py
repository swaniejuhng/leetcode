# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        # my solution - mine is faster?????
        num_max = 2**31 - 1; num_min = -2**31
        if x < 0:
            neg = True; x = abs(x)
        else:
            neg = False

        x_reverse = []
        while True:
            if x % 10 > 0 or x // 10 > 0:
                x_reverse.append(str(x % 10))
                x = x // 10
            if x == 0:
                break
        if len(x_reverse) > 0:
            result = int("".join(x_reverse))
            if neg is True:
                result = result * (-1)
        else:
            result = 0
        if result < num_min or result > num_max:
            return 0
        else:
            return result

        # better solution
        """
        sign = int(x>0) - int(x<0)
        result = sign*int(str(abs(x))[::-1])
        if result < -2**31 or result > (2**31 - 1):
            return 0
        else:
            return result
        """
