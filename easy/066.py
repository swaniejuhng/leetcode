class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # my solution
        carry = True
        for i in range(len(digits)-1, -1, -1):
            if carry:
                if digits[i] < 9:
                    carry = False
                digits[i] = (digits[i]+1)%10
        if carry:
            digits[0:0] = [1]
        return digits
