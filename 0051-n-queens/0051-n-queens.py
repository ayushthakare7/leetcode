

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        left_row = [0] * n
        lower_diag = [0] * (2 * n - 1)
        upper_diag = [0] * (2 * n - 1)

        board = ["." * n for _ in range(n)]

        self.solve(0, board, ans, left_row, upper_diag, lower_diag, n)
        return ans

    def solve(self, col, board, ans, left_row, upper_diag, lower_diag, n):
        if col == n:
            ans.append(board[:])
            return

        for row in range(n):
            if (left_row[row] == 0 and
                lower_diag[row + col] == 0 and
                upper_diag[n - 1 + col - row] == 0):

                board[row] = board[row][:col] + "Q" + board[row][col + 1:]

                left_row[row] = 1
                lower_diag[row + col] = 1
                upper_diag[n - 1 + col - row] = 1

                self.solve(col + 1, board, ans, left_row, upper_diag, lower_diag, n)

                board[row] = board[row][:col] + "." + board[row][col + 1:]

                left_row[row] = 0
                lower_diag[row + col] = 0
                upper_diag[n - 1 + col - row] = 0