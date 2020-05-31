import collections


class Solution:
    def checkIfPrerequisite(self, n, ps, qs):

        self.mp = collections.defaultdict(list)
        for u, v in ps:
            self.mp[u].append(v)

        cache = {}

        def dfs(cur, target):
            if target in cache and cur in cache[target]:
                return cache[target][cur]

            if cur == target:
                return True

            res = False
            for adj in self.mp[cur]:
                if dfs(adj, target):
                    res = True
                    break

            if target in cache:
                cache[target][cur] = res
            else:
                cache[target] = {}
                cache[target][cur] = res

            return res

        ans = []
        for u, v in qs:
            ans.append(dfs(u, v))

        return ans
