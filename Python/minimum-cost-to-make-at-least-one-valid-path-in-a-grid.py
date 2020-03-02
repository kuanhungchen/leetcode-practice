class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        inf = 1000000
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(x, y, value):
            x2 = x + dirs[grid[y][x] - 1][0]
            y2 = y + dirs[grid[y][x] - 1][1]
            if 0 <= x2 < n and 0 <= y2 < m and dp[y2][x2] == inf:
                dp[y2][x2] = value
                bfs.append([x2, y2])
                dfs(x2, y2, value)

        bfs, value = [[0, 0]], 0
        dfs(0, 0, value)
        while dp[-1][-1] == inf:
            value += 1
            bfs, bfs2 = [], bfs
            for x, y in bfs2:
                for d in range(1, 5):
                    grid[y][x] = d
                    dfs(x, y, value)
        return dp[-1][-1]
