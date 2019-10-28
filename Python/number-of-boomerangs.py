class Solution:
    def numberOfBoomerangs(self, points):
        ans = 0
        for center in points:
            distances = {}
            for p in points:
                distance = (p[0] - center[0]) ** 2 + (p[1] - center[1]) ** 2
                if distance in distances:
                    ans += distances[distance] * 2
                    distances[distance] += 1
                else:
                    distances[distance] = 1
        return ans
