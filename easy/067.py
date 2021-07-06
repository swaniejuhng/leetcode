class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # my solution
        """
        if len(a) >= len(b):
            max_len = len(a)
            a = [int(n) for n in a]
            b = [0]*(max_len-len(b)) + [int(n) for n in b]
        else:
            max_len = len(b)
            a = [0]*(max_len-len(a)) + [int(n) for n in a]
            b = [int(n) for n in b]

        result = ""
        carry = 0
        for i in range(max_len-1, -1, -1):
            temp = a[i] + b[i] + carry
            result = str(temp%2) + result
            carry = temp//2

        if carry == 1:
            result = "1" + result

        return result
        """

        # better solution
        carry = 0
        result = ""

        a = list(a); b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += str(carry%2)
            carry //= 2

        return result[::-1]
