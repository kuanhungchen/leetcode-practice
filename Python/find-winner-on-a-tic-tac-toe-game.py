class Solution:
    def tictactoe(self, moves):

        def whoWins(rs, cs, ds):
            if 3 in rs or 3 in cs or 3 in ds:
                return "A"
            elif -3 in rs or -3 in cs or -3 in ds:
                return "B"
            return "X"

        rows, cols, dias = [0] * 3, [0] * 3, [0] * 2
        for i in range(9):
            if not len(moves): return "Pending"
            x, y = moves.pop(0)
            rows[x] += -1 if i % 2 else 1
            cols[y] += -1 if i % 2 else 1
            if (x, y) in [(0, 0), (1, 1), (2, 2)]: dias[0] += -1 if i % 2 else 1
            if (x, y) in [(0, 2), (1, 1), (2, 0)]: dias[1] += -1 if i % 2 else 1
            if whoWins(rows, cols, dias) != "X": return whoWins(rows, cols, dias)
        return "Draw"
