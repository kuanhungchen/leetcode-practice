class Solution:
    def islandPerimeter(self, grid):
        def dfs(g, x, y, p):
            if x < 0 or y < 0 or x == len(g) or y == len(g[0]) or g[x][y] == 0: return p + 1
            if g[x][y] == -1: return p
            g[x][y] = -1
            p = dfs(g, x - 1, y, p)
            p = dfs(g, x, y + 1, p)
            p = dfs(g, x + 1, y, p)
            p = dfs(g, x, y - 1, p)
            return p

        cols, rows = len(grid[0]), len(grid)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: return dfs(grid, i, j, 0)
