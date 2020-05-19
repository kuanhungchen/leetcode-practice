class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        ans = 0
        for s, e in zip(startTime, endTime):
            ans += s <= queryTime <= e
        return ans
