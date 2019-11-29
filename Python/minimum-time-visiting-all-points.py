class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        now = points[0]
        ans = 0
        for point in points[1:]:
            ans += max(abs(now[0] - point[0]), abs(now[1] - point[1]))
            now = point
        return ans
