# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # my solution
        if digits == "":
            return []

        phone_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        output = product(*[phone_dict[int(d)] for d in digits])
        output = ["".join(o) for o in output]
        return output
