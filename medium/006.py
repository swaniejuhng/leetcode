# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # my solution - failed
        """
        numCols = len(s)//(2*numRows-2)*(numRows-1)
        if 0 < len(s)%(2*numRows-2) <= numRows:
            numCols += 1
        else:
            numCols += (len(s)%(2*numRows-2)-numRows)
        result = [" "] * (numRows * numCols)

        for i in range(1, len(s)+1):
            if 0 < i%(2*numRows-2) <= numRows:
                row = i%(2*numRows-2)
                col =
                result[i%(2*numRows-2)*numCols+(i//(2*numRows-2)-1)*(numRows-1)+1] = s[i-1]
            else:
                row = i%(2*numRows-2)%
                col =
                result[(numRows-1-i%(2*numRows-2))*numCols+i%(2*numRows-2)] = s[i-1]

        return "".join(result).rstrip()
        """

        # better solution
        if numRows == 1 or len(s) <= numRows:
            return s

        L = [""] * numRows
        index = 0; step = 1

        for c in s:
            L[index] += c
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return "".join(L)
