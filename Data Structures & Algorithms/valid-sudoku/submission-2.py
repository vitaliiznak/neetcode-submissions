class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS = len(board)
        if ROWS < 1:
            return False
        COLS = len(board[0])
        if ROWS != COLS:
            return False

        # #row_constrain
        # for row in board:
        #     set_dup = set()
        #     for cell in row:
        #         if cell == '.':
        #             continue
        #         else:
        #             if cell in set_dup:
        #                 return False
        #             set_dup.add(cell)
        #     if not len(set_dup):
        #         return False

        #row_constrain
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True



                