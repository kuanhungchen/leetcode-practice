class Solution:
    def maxAreaOfIsland(self, grid):
        def dfs(x, y):
            if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0: return 0
            grid[x][y] = 0
            return 1 + dfs(x - 1, y) + dfs(x, y - 1) + dfs(x + 1, y) + dfs(x, y + 1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, dfs(i, j))
        return ans
