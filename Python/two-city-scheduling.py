class Solution:
    def twoCitySchedCost(self, costs):
        differences = [abs(x[1]-x[0]) for x in costs]
        quota = len(costs) // 2
        l, r = quota, quota
        ans = 0
        while len(differences) > 1:
            _max, _max_idx = -1, -1
            for idx in range(len(differences)):
                if differences[idx] > _max:
                    _max, _max_idx = differences[idx], idx
            if costs[_max_idx][0] > costs[_max_idx][1]:
                ans += costs[_max_idx][1]
                r -= 1
            else:
                ans += costs[_max_idx][0]
                l -= 1
            differences.pop(_max_idx)
            costs.pop(_max_idx)
            if l == 0:
                for cost in costs:
                    ans += cost[1]
                return ans
            if r == 0:
                for cost in costs:
                    ans += cost[0]
                return ans


example = [[100, 10], [500, 15]]
sln = Solution()
print(sln.twoCitySchedCost(example))
