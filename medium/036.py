# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # my solution - high time & space complexity
        """
        import numpy as np
        from collections import Counter

        board = np.array(board)
        for i in range(9):
            # rows
            unit = [v for v in board[i, :] if v != "."]
            if len(set(unit)) != len(unit):
                return False

            # columns
            unit = [v for v in board[:, i] if v != "."]
            if len(set(unit)) != len(unit):
                return False

        # squares
        for i in range(3):
            for j in range(3):
                temp = np.ravel(board[i*3:i*3+3, j*3:j*3+3])
                unit = [v for v in temp if v != "."]
                if len(set(unit)) != len(unit):
                    return False

        return True
        """

        # better solution
        def is_unit_valid(unit):
            unit = [v for v in unit if v != "."]
            return len(set(unit)) == len(unit)

        # rows
        for row in board:
            if not is_unit_valid(row):
                return False

        # columns
        for col in zip(*board):
            if not is_unit_valid(col):
                return False

        # squares
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not is_unit_valid(square):
                    return False

        return True
