import collections


class Solution:
    def canFinish(self, A, ps):

        def dfs(node):
            if self.visited[node] == -1: return False
            self.visited[node] = -1

            for adj in self.graph[node]:
                if self.visited[adj] != 1 and not dfs(adj):
                    return False

            self.visited[node] = 1

            return True

        self.graph = collections.defaultdict(list)
        for u, v in ps:
            self.graph[v].append(u)

        self.visited = [0 for _ in range(A)]  # 0: not, -1: ing, 1: done

        for node in range(A):
            if self.visited[node] != 1 and not dfs(node):
                return False
        return True
