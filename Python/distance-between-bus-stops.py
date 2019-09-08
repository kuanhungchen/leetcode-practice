class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        if len(distance) == 1:
            return distance[0]
        if start > destination:
            start, destination = destination, start
        total = sum(distance)
        clockwise = sum(distance[start:destination])
        return min(clockwise, total - clockwise)


class Solution2:
    def distanceBetweenBusStops(self, distance, start, destination):
        # two lines
        start, destination = sorted([start, destination])
        return distance[0] if len(distance) == 1 else min(sum(distance[start:destination]), sum(distance[:start])+sum(distance[destination:]))
