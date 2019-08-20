class Solution:
    def minCostClimbingStairs(self, cost):
        # dynamic programming method
        # so difficult, copy from discussion
        _array = [0] * len(cost)
        for idx in range(2, len(cost)):
            _array[idx] = min(_array[idx-1] + cost[idx-1], _array[idx-2] + cost[idx-2])
        return min(_array[-1] + cost[-1], _array[-2] + cost[-2])
