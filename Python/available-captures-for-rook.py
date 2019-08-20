class Solution:
    def numRookCaptures(self, board):
        rook_i = -1
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 'R':
                    rook_i = i
                    rook_j = j
                    break
            if rook_i != -1: break

        ans = 0
        idx = rook_i - 1
        while idx != -1 and board[idx][rook_j] == '.':
            idx -= 1
        if idx != -1 and board[idx][rook_j] == 'p':
            ans += 1

        idx = rook_i + 1
        while idx != 8 and board[idx][rook_j] == '.':
            idx += 1
        if idx != 8 and board[idx][rook_j] == 'p':
            ans += 1

        idx = rook_j - 1
        while idx != -1 and board[rook_i][idx] == '.':
            idx -= 1
        if idx != -1 and board[rook_i][idx] == 'p':
            ans += 1

        idx = rook_j + 1
        while idx != 8 and board[rook_i][idx] == '.':
            idx += 1
        if idx != 8 and board[rook_i][idx] == 'p':
            ans += 1
        return ans
