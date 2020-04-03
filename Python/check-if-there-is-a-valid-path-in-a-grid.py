class Solution:
    def hasValidPath(self, grid):
        def dfs(x, y, d):
            if x == m or y == n:
                return True
            if grid[x][y] == 1:
                if d == 1:
                    return dfs(x, y + 1, d)
                elif d == 3:
                    return dfs(x, y - 1, d)
            elif grid[x][y] == 2:
                if d == 0:
                    return dfs(x + 1, y, d)
                elif d == 2:
                    return dfs(x - 1, y, d)
            elif grid[x][y] == 3:
                if d == 1:
                    return dfs(x + 1, y, 0)
                elif d == 2:
                    return dfs(x, y - 1, 3)
            elif grid[x][y] == 4:
                if d == 3:
                    return dfs(x + 1, y, 0)
                elif d == 2:
                    return dfs(x, y + 1, 1)
            elif grid[x][y] == 5:
                if d == 1:
                    return dfs(x - 1, y, 2)
                elif d == 0:
                    return dfs(x, y - 1, 3)
            elif grid[x][y] == 6:
                if d == 3:
                    return dfs(x - 1, y, 2)
                elif d == 0:
                    return dfs(x, y + 1, 1)
            return False

        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True
        elif grid[0][0] == 5:
            return False
        elif grid[0][0] in [1, 6]:
            return n >= 2 and dfs(0, 1, 1)
        elif grid[0][0] in [2, 3]:
            return m >= 2 and dfs(1, 0, 0)
        elif grid[0][0] == 4:
            return n >= 2 and dfs(0, 1, 1) or m >= 1 and dfs(1, 0, 0)
