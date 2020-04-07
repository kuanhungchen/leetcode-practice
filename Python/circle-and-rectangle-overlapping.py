class Solution:
    def checkOverlap(self, rad: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xc + rad < x1:
            return False
        elif xc - rad > x2:
            return False
        elif yc + rad < y1:
            return False
        elif yc - rad > y2:
            return False
        xcc = (x1 + x2) // 2
        ycc = (y1 + y2) // 2
        return abs(xcc - xc) ** 2 + abs(ycc - yc) ** 2 <= (rad + (x2 - x1)) ** 2
