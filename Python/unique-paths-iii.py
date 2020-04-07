class Solution:
    def uniquePathsIII(self, grid):
        m, n, empty = len(grid), len(grid[0]), 1
        for r, row in enumerate(grid):
            for c, ele in enumerate(row):
                if ele == 2:
                    dst_x, dst_y = r, c
                elif ele == 1:
                    src_x, src_y = r, c
                elif ele == 0:
                    empty += 1

        self.ans = 0

        def dfs(x, y, _empty):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0):
                return
            if x == dst_x and y == dst_y and _empty == 0:
                self.ans += 1
                return
            grid[x][y] = -2
            dfs(x, y - 1, _empty - 1)
            dfs(x, y + 1, _empty - 1)
            dfs(x - 1, y, _empty - 1)
            dfs(x + 1, y, _empty - 1)
            grid[x][y] = 0

        dfs(src_x, src_y, empty)
        return self.ans
