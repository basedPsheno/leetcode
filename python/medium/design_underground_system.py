# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.journey = {}
        self.history = {}
        

    def checkIn(self, id: int, startStation: str, startTime: int) -> None:
        self.journey[id] = (startStation, startTime)
        

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        startStation, startTime = self.journey.pop(id)
        key = (startStation, endStation)
        allTime, allCount = self.history.get(key, (0, 0))
        self.history[key] = (allTime + (endTime - startTime), allCount + 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        allTime, allCount = self.history.get(key, (0, 0))
        return allTime / allCount
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
