import heapq


class Solution:
    def maxPerformance(self, n, speed, efficient, k):
        sq = []
        ans = sSum = 0
        teams = sorted([(e, s) for e, s in zip(efficient, speed)], reverse=True)
        for i, (e, s) in enumerate(teams):
            sSum += s
            if i >= k:
                sSum -= heapq.heappushpop(sq, s)
            else:
                heapq.heappush(sq, s)
            ans = max(ans, sSum * e)

        return ans % (10 ** 9 + 7)
