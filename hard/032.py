class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # my solution - failed
        """
        longest = []
        stack = []
        start = 0; end = 0
        for i in range(len(s)):
            if s[i] == ')':
                if not stack or stack.pop() != '(':
                    end = i
                    if end-start+1 > len(longest):
                        stack = []
                        longest = s[start:end+1]
                    start = i+1
                else:
                    stack.append(s[i])
        if stack:
            start += len(stack)
        if len(s)-start > len(longest):
            return s[start:]
        return longest
        """

        # better solution
        stack = [(-1, ')')]; max_length = 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                max_length = max(max_length, i=stack[-1][0])
            else:
                stack.append((i, paren))
        return max_length
