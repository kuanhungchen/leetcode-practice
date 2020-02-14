class Solution:
    def uniquePathsWithObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1: return 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: grid[i][j] = 1
                elif grid[i][j] == 1: grid[i][j] = 0
                elif i == 0: grid[i][j] = grid[i][j-1]
                elif j == 0: grid[i][j] = grid[i-1][j]
                else: grid[i][j] = grid[i][j-1] + grid[i-1][j]
        return grid[-1][-1]

