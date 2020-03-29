class UndergroundSystem:

    def __init__(self):
        self.peo = {}
        self.times = {}

    def checkIn(self, id, stationName, t):
        self.peo[id] = tuple([stationName, t])

    def checkOut(self, id, stationName, t):
        start = self.peo[id][0]
        if start not in self.times:
            self.times[start] = {}
            self.times[start][stationName] = [t - self.peo[id][1]]
        else:
            if stationName not in self.times[start]:
                self.times[start][stationName] = [t - self.peo[id][1]]
            else:
                self.times[start][stationName].append(t - self.peo[id][1])
        self.peo[id] = None

    def getAverageTime(self, startStation, endStation):
        ttl = sum(self.times[startStation][endStation])
        cnt = len(self.times[startStation][endStation])
        return ttl / cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
