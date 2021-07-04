# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # my solution - quite fast but not space-efficient
        """
        p_dict = {}
        for i, p in enumerate("(){}[]"):
            p_dict[p] = i # "(": 0, ")": 1, "{": 2

        stack = []
        for i, c in enumerate(s):
            curr = p_dict[c]
            if curr % 2 == 0:
                stack.append(curr)

            elif curr % 2 == 1:
                # stack is null but right parenthesis came in
                if not stack:
                    return False
                # stack does not contain corresponding left parenthesis at the top
                elif stack[-1] != (curr - 1):
                    return False
                # parenthesis match
                else:
                    stack.pop()

        if stack:
            return False
        return True
        """

        # better solution
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in match:
                if not stack:
                    return False
                elif stack.pop() != match[c]:
                    return False
            else:
                stack.append(c)

        return not stack
