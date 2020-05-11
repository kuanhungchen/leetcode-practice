class Solution:
    def floodFill(self, grid, sr, sc, newColor):

        m, n = len(grid), len(grid[0])
        self.target = grid[sr][sc]

        def dfs(x, y):
            grid[x][y] = newColor
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (0 <= x + i < m and 0 <= y + j < n) and grid[x + i][y + j] == self.target:
                    dfs(x + i, y + j)

        if self.target == newColor:
            return grid
        dfs(sr, sc)
        return grid
