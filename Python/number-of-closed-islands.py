class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == 1: return
            grid[x][y] = 1
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
                    dfs(i, j)
        return ans
