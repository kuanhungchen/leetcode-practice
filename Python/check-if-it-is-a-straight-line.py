class Solution:
    def checkStraightLine(self, points):
        origin = points[0]
        if points[0][0] == points[1][0]:
            for point in points:
                if point[0] != origin[0]:
                    return False
            return True

        m = (points[1][1] - origin[1]) / (points[1][0] - origin[0])
        for point in points[1:]:
            if point[0] == origin[0] or (point[1] - origin[1]) / (point[0] - origin[0]) != m:
                return False
        return True
