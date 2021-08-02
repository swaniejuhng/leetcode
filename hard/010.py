# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # my solution - failed
        """
        s_list = []; p_list = []

        start = 0
        if len(s) == 1:
            s_list.append(s)
        else:
            for i in range(1, len(s)):
                curr = s[i]; prev = s[i-1]
                if curr != prev:
                    s_list.append(s[start:i])
                    start = i
                if i == len(s) - 1:
                    s_list.append(s[start:])

        for i in range(len(p)):
            if p[i].isalpha() or p[i] == ".":
                if i == len(p) - 1:
                    p_list.append(p[i:i+1])
                elif p[i+1] == "*":
                    p_list.append(p[i:i+2])
                else:
                    p_list.append(p[i:i+1])
            elif p[i] == "*":
                continue

        if len([elem for elem in p_list if len(elem) == 1]) > len(s):
            return False

        print(s_list, p_list)
        while s_list and p_list:
            while len(p_list[0]) == 1:
                if (s_list[0][0] == p_list[0]) or (p_list[0] == "."):
                    if len(s_list[0]) == 1:
                        s_list.pop(0)
                    else:
                        s_list[0] = s_list[0][1:]
                    p_list.pop(0)
                else:
                    return False
                if not s_list or not p_list: break
            print(s_list, p_list)
            if not s_list or not p_list: break
            while len(p_list[-1]) == 1:
                if (s_list[-1][-1] == p_list[-1]) or (p_list[-1] == "."):
                    if len(s_list[-1]) == 1:
                        s_list.pop(-1)
                    else:
                        s_list[-1] = s_list[-1][:-1]
                    p_list.pop(-1)
                else:
                    return False
                if not s_list or not p_list: break
            print(s_list, p_list)
            if not s_list or not p_list: break
            if len(p_list[0]) == 2:
                if p_list[0][0] == ".":
                    return len([elem for elem in p_list if len(elem) == 1]) <= len(s)
                elif s_list[0][0] == p_list[0][0]:
                    s_list.pop(0)
                p_list.pop(0)
            print(s_list, p_list)
        p_lengths = set([len(elem) for elem in p_list])

        return (not s_list) and ((not p_list) or (p_lengths == {2}))
        """

        # better solution
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            retrurn not s
        if p[-1] == "*":
            if self.isMatch(s, p[:-2]):
