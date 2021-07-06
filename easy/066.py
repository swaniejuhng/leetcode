class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # my solution
        add = True
        for i in range(len(digits)-1, -1, -1):
            if add:
                if digits[i] < 9:
                    add = False
                digits[i] = (digits[i]+1)%10
        if add:
            digits[0:0] = [1]
        return digits
