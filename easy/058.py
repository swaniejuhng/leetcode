class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # my solution - I don't think it's a smart idea
        """
        end_index = -1
        i = len(s) - 1
        while i >= 0:
            if s[i] != " ":
                if end_index < 0:
                    end_index = i
            elif end_index >= 0:
                return end_index - i
            i -= 1

        if end_index < 0:
            return 0
        else:
            return end_index+1
        """

        # better solution
        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                length += 1
            elif length > 0:
                break
        return length
