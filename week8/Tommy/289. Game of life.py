from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows: int = len(board)
        cols: int = len(board[0])
        diff = {(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)}

        for row in range(rows):
            for col in range(cols):
                number_of_live = 0
                for dif in diff:
                    r = row + dif[0]
                    c = col + dif[1]
                    if (0 <= r < rows) and (0 <= c < cols) and abs(board[r][c]) == 1:
                        number_of_live += 1
                if (number_of_live < 2 and board[row][col] == 1) or (number_of_live > 3 and board[row][col] == 1):
                    board[row][col] = -1
                if number_of_live == 3 and board[row][col] == 0:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
