class Solution:
    def numEnclaves(self, A):
        # copy from others
        def dfs(A, rows, cols, x, y):
            if not 0 <= x < rows or not 0 <= y < cols:
                return
            elif A[x][y] == 0:
                return
            else:
                A[x][y] = 0
                dfs(A, rows, cols, x - 1, y)
                dfs(A, rows, cols, x + 1, y)
                dfs(A, rows, cols, x, y - 1)
                dfs(A, rows, cols, x, y + 1)
                return

        _rows, _cols = len(A), len(A[0])
        for i in range(_cols):
            if A[0][i] == 1:
                dfs(A, _rows, _cols, 0, i)
            if A[_rows - 1][i] == 1:
                dfs(A, _rows, _cols, _rows - 1, i)
        for i in range(_rows):
            if A[i][0] == 1:
                dfs(A, _rows, _cols, i, 0)
            if A[i][_cols - 1] == 1:
                dfs(A, _rows, _cols, i, _cols - 1)

        return sum([sum(x) for x in A])
