class Solution:
    def countServers(self, grid):

        def fill(net, pos):
            x, y = pos

            net[y] = [net[y][i] + 1 for i in range(len(net[0]))]
            for row in net:
                row[x] += 1
            net[y][x] -= 1

            return net

        m = len(grid)
        n = len(grid[0])
        network = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    network = fill(network, [j, i])

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and network[i][j] > 1:
                    ans += 1
        return ans
