# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        # my solution - couldn't solve it but I think I got close - lol nope
        """
        left = 0; right = x//2
        while True:
            mid = (left+right+1)//2
            if x == (left*left):
                return left
            elif x == (mid*mid):
                return mid
            elif x == (right*right):
                return right
            elif (left*left) < x < (mid*mid):
                if mid-left<=1:
                    return left
                right = mid - 1
            elif (mid*mid) < x < (right*right):
                if right-mid<=1:
                    return mid
                left = mid + 1
        """

        # better solution
        """
        left = 0; right = x
        while left <= right:
            mid = (left+right)//2
            if x < (mid*mid):
                right = mid - 1
            elif x > (mid*mid):
                left = mid + 1
            else:
                return mid

        # When there is no perfect square, right is the the value on the left
        # of where it would have been (rounding down). If we were rounding up,
        # we would return left
        return right
        """

        # alternative solution (Newton's method)
        r = x
        while r*r > x:
            r = int((r + x/r) / 2)
        return r
