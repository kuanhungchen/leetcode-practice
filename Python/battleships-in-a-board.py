class Solution:
    def countBattleships(self, board):
        if not len(board): return 0
        cols, rows = len(board[0]), len(board)
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'X' and (j == 0 or board[i][j-1] == '.') and (i == 0 or board[i-1][j] == '.'):
                    ans += 1
        return ans
