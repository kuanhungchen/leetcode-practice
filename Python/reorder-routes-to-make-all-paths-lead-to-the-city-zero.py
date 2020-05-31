import collections


class Solution:
    def minReorder(self, n, cs):

        self.ans = 0
        self.visited = set([0])
        self.path = collections.defaultdict(list)
        self.rev = collections.defaultdict(list)

        for u, v in cs:
            self.path[u].append(v)
            self.rev[v].append(u)

        def dfs(cur):

            for adj in self.path[cur]:
                if adj not in self.visited:
                    self.ans += 1
                    self.visited.add(adj)
                    dfs(adj)

            for adj in self.rev[cur]:
                if adj not in self.visited:
                    self.visited.add(adj)
                    dfs(adj)

        dfs(0)
        return self.ans
